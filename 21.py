import sys
import socket
import cmd
import time
import threading
import chat

SERVER = "larc.inf.furb.br"
TCP_PORT = 1012
UDP_PORT = 1011
MSG_LEN  = 2048

help = """
help                            - mostra essa mensagem
login <userid> <passwd>         - faz o login
logout                          - faz o logout
game <[enter, [stop, [quit]]]>  - comandos do jogo
msg  <to> <message>             - manda uma mensagem para o usuário com o id <to>
users                           - lista os usuários
messages                        - lista suas mensagens
players                         - lista os jogadores
card                            - solicita uma carta
enter                           - solicita a participação no jogo de cartas 21
stop                            - avisa que não quer mais nenhuma carta
quit                            - solicita sair do jogo de cartas 21
exit                            - sai do jogo
"""

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((SERVER, TCP_PORT))

def create_larc_tcp_socket():
    return tcp

def create_larc_udp_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return s

def get_response_from_server(msg):
    chuncks = []
    msg += '\r\n'
    s = create_larc_tcp_socket()
    s.send(msg.encode('ascii'))
    while True:
        data = s.recv(MSG_LEN)
        chuncks.append(data.decode('utf-8'))
        if b'\n' in data:
            return ''.join(chuncks)

def send_udp_command(msg):
    s = create_larc_udp_socket()
    msg += '\r\n'
    s.sendto(msg.encode('ascii'), (SERVER, UDP_PORT))

def get_users(userid, passwd):
    return get_response_from_server("GET USERS {0}:{1}".format(userid, passwd))

def get_messages(userid, passwd):
    return get_response_from_server("GET MESSAGE {0}:{1}".format(userid, passwd))

def get_players(userid, passwd):
    return get_response_from_server("GET PLAYERS {0}:{1}".format(userid, passwd))

def get_card(userid, passwd):
    return get_response_from_server("GET CARD {0}:{1}".format(userid, passwd))

def send_message(userid1, passwd, userid2, msg):
    send_udp_command("SEND MESSAGE {0}:{1}:{2}:{3}".format(userid1, passwd, userid2, msg))

def send_game(userid, passwd, msg):
    send_udp_command("SEND GAME {0}:{1}:{2}".format(userid, passwd, msg))

alive = dict()
alivetimer = None

def keepalive():
    global alivetimer
    alivetimer = threading.Timer(5.0, keepalive)
    for u,p in alive.items():
        get_users(u, p)
    alivetimer.start()

class Repl(cmd.Cmd):
    def do_help(self, line):
        print(help)

    def do_login(self, line):
        user = line.split(' ')
        self.userid = user[0]
        self.passwd = user[1]
        alive[self.userid] = self.passwd

    def do_logout(self, line):
        del alive[self.userid]
        self.userid = None
        self.passwd = None

    def do_game(self, line):
        send_game(self.userid, self.passwd, line.strip().upper())

    def do_msg(self, line):
        message = line.split(' ')
        send_message(self.userid, self.passwd, message[0], message[1])

    def do_users(self, line):
        print(get_users(self.userid, self.passwd))

    def do_messages(self, line):
        print(get_messages(self.userid, self.passwd))

    def do_players(self, line):
        print(get_players(self.userid, self.passwd))

    def do_card(self, line):
        print(get_card(self.userid, self.passwd))

    def do_enter(self, line):
        send_game(self.userid, self.passwd, "ENTER")

    def do_stop(self, line):
        send_game(self.userid, self.passwd, "STOP")

    def do_quit(self, line):
        if self.userid in alive:
            del alive[self.userid]
        send_game(self.userid, self.passwd, "QUIT")

    def do_rodrigo(self, line):
        self.userid = "8598"
        self.passwd = "lmyhn"
        alive[self.userid] = self.passwd

    def do_ronan(self, line):
        self.userid = "6244"
        self.passwd = "pkuod"
        alive[self.userid] = self.passwd

    def do_ricardo(self, line):
        self.userid = "1231"
        self.passwd = "lcarn"
        alive[self.userid] = self.passwd

    def do_nykolas(self, line):
        self.userid = "9324"
        self.passwd = "yvyfc"
        alive[self.userid] = self.passwd

    def do_rai(self, line):
        self.userid = "4942"
        self.passwd = "bnhke"
        alive[self.userid] = self.passwd

    def do_exit(self, line):
        print("Good Bye. =)")
        if (alivetimer): alivetimer.cancel()
        import sys; sys.exit()

    def do_log(self, line):
        print(users)

def init_gui():
    from PyQt5 import QtCore, QtGui, QtWidgets
    class MainWindow(QtWidgets.QMainWindow, chat.Ui_MainWindow):
        def __init__(self, parent=None):
            QtWidgets.QMainWindow.__init__(self)
            self.setupUi(self)
            self.btLogin.clicked.connect(self.login)

        def login(self):
            self.userid = self.edUsuario.text()
            self.passwd = self.edSenha.text()
            alive[self.userid] = self.passwd
            self.edUsuario.setText("")
            self.edSenha.setText("")
            self.setWindowTitle(self.userid)


    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow(None)
    mainwindow.show()
    app.exec_()

if __name__ == '__main__':
    keepalive()
    try:
        if (len(sys.argv) >= 2):
            init_gui()
        else:
            Repl().cmdloop()
    except:
        alivetimer.cancel()
