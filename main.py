from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QProgressBar
from PyQt5.QtCore import QObject, pyqtSignal
from tela_backup_ui import Ui_Form
from tkinter import filedialog
import subprocess
import datetime
import os
import threading
import mysql.connector
from PyQt5.QtCore import Qt

class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(str)
    progress = pyqtSignal(int)

class TesteConexaoThread(threading.Thread):
    def __init__(self, parent, ip_banco, porta, usuario, senha, banco):
        threading.Thread.__init__(self)
        self.parent = parent
        self.ip_banco = ip_banco
        self.porta = porta
        self.usuario = usuario
        self.senha = senha
        self.banco = banco
        self.signals = WorkerSignals()

    def run(self):
        try:
            # Tenta estabelecer uma conexão com o banco de dados
            conexao = mysql.connector.connect(
                host=self.ip_banco,
                port=self.porta,
                user=self.usuario,
                password=self.senha,
                database=self.banco
            )

            # Se a conexão for bem-sucedida, emite o sinal de conexão bem-sucedida
            self.signals.finished.emit()

            # Fecha a conexão
            conexao.close()

        except mysql.connector.Error as e:
            self.signals.error.emit(f"Erro ao testar a conexão: {str(e)}")

class BackupThread(threading.Thread):
    def __init__(self, parent, ip_banco, porta, usuario, senha, banco, pasta_selecionada):
        threading.Thread.__init__(self)
        self.parent = parent
        self.ip_banco = ip_banco
        self.porta = porta
        self.usuario = usuario
        self.senha = senha
        self.banco = banco
        self.pasta_selecionada = pasta_selecionada
        self.signals = WorkerSignals()
        self.cancelado = False  # Adicionado para verificar se o backup foi cancelado
        self.process = None

    def run(self):
        try:
            # Define o comando mysqldump
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            arquivo_backup = f'{self.pasta_selecionada}\\{timestamp}.sql'
            comando = f'mysqldump -h {self.ip_banco} -P {self.porta} -u {self.usuario} -p{self.senha} --column-statistics=0 {self.banco} > "{arquivo_backup}"'

            # Executa o comando no terminal (como se fosse no CMD)
            self.process = subprocess.Popen(comando, shell=True)

            while self.process.poll() is None:
                # Aguarde até que o processo seja concluído ou o backup seja cancelado
                if self.cancelado:
                    self.cancelar_backup()
                    return

            if self.process.poll() == 0:
                self.signals.finished.emit()
            else:
                self.signals.error.emit("Erro ao realizar o backup!")

        except Exception as e:
            self.signals.error.emit(f"Erro ao realizar o backup: {str(e)}")

    def cancelar_backup(self):
        if self.process:
            try:
                # Obtém o PID (Process ID) do processo CMD
                pid = self.process.pid
                processo_cmd = psutil.Process(pid)
                
                # Termina o processo CMD
                processo_cmd.terminate()
                
                self.signals.error.emit("Backup cancelado!")

            except Exception as e:
                self.signals.error.emit(f"Erro ao cancelar o backup: {str(e)}")

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configura a UI criada no Qt Designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Conecte um sinal de botão a uma função
        self.ui.but_backup.clicked.connect(self.botao_backup)
        self.ui.but_local.clicked.connect(self.escolher_pasta)
        self.ui.but_cancelar.clicked.connect(self.cancelar_backup)
        self.ui.test_conexao.clicked.connect(self.teste_conexao)
        self.backup_andamento = False
        self.backup_thread = None
        self.arquivo_backup = None
        self.ui

        # Configurar o tamanho fixo da janela
        self.setFixedSize(563, 270)  # Substitua os valores pelos desejados

        # Impedir maximização da janela
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)

    # ... (código anterior)
    
    def teste_conexao(self):
        ip_banco = self.ui.bd_ip.text()
        porta = self.ui.bd_porta.text()
        banco = self.ui.bd_banco.text()
        usuario = self.ui.bd_ususario.text()
        senha = self.ui.bd_senha.text()

        if not ip_banco or not porta or not banco or not usuario or not senha:
            self.mostrar_mensagem(QMessageBox.Critical, "Preencha todos os campos.")
            return

        try:
            # Inicie a thread de teste de conexão
            teste_conexao_thread = TesteConexaoThread(self, ip_banco, porta, usuario, senha, banco)
            teste_conexao_thread.signals.finished.connect(lambda: self.mostrar_mensagem(QMessageBox.Information, "Teste de conexão bem-sucedido!"))
            teste_conexao_thread.signals.error.connect(lambda msg: self.mostrar_mensagem(QMessageBox.Critical, f"Erro: {msg}"))
            teste_conexao_thread.start()

        except Exception as e:
            self.mostrar_mensagem(QMessageBox.Critical, f"Erro ao iniciar o teste de conexão: {str(e)}")

    def mostrar_dados(self, mensagem):
        self.ui.bd_andamento.append(mensagem)

    def escolher_pasta(self):
        self.pasta_selecionada = filedialog.askdirectory()
        if self.pasta_selecionada:
            self.ui.bd_local_salvar.setText(self.pasta_selecionada)
            print(f'Pasta selecionada: {self.pasta_selecionada}')

    def mostrar_mensagem(self, tipo, mensagem):
        self.ui.bd_andamento.append(mensagem)
        msg = QMessageBox()
        msg.setIcon(tipo)
        msg.setText(mensagem)
        msg.setWindowTitle("Mensagem")
        msg.exec_()

    def cancelar_backup(self):
        if self.backup_andamento and self.backup_thread:
            self.backup_thread.cancelar_backup()
            self.mostrar_mensagem(QMessageBox.Warning, "Cancelando backup. Aguarde...")
            self.backup_thread.join()  # Aguarde a conclusão da thread
            self.mostrar_mensagem(QMessageBox.Information, "Backup cancelado com sucesso!")

    def botao_backup(self):
        if self.backup_andamento:
            self.mostrar_mensagem(QMessageBox.Warning, "Backup já em andamento.")
            return

        ip_banco = self.ui.bd_ip.text()
        porta = self.ui.bd_porta.text()
        banco = self.ui.bd_banco.text()
        usuario = self.ui.bd_ususario.text()
        senha = self.ui.bd_senha.text()

        if not ip_banco or not porta or not banco or not usuario or not senha:
            self.mostrar_mensagem(QMessageBox.Critical, "Preencha todos os campos.")
            return

        try:
            # Inicie a thread de backup
            self.backup_thread = BackupThread(self, ip_banco, porta, usuario, senha, banco, self.pasta_selecionada)
            self.backup_thread.signals.finished.connect(lambda: self.mostrar_dados("Backup realizado com sucesso!"))
            self.backup_thread.signals.error.connect(lambda msg: self.mostrar_dados(f"Erro: {msg}"))
            self.backup_thread.start()
            self.backup_andamento = True
            self.mostrar_mensagem(QMessageBox.Information, "Backup em andamento. Aguarde...")

        except Exception as e:
            self.mostrar_mensagem(QMessageBox.Critical, f"Erro ao iniciar o backup: {str(e)}")

if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec_()
