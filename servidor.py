import socket
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

host = '127.0.0.1'
port = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

def lidar_com_cliente():
    conn, addr = server.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
    conn.close()

def iniciar_servidor():
    lidar_com_cliente()

win = Gtk.Window(title="Servidor")
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()
