import socket
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

host = '127.0.0.1'
port = 12345

class ClienteGTK(Gtk.Window):
    def __init__(self):
        super().__init__(title="Cliente")

        self.set_border_width(10)
        self.set_default_size(300, 100)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

        self.entry = Gtk.Entry()
        self.box.pack_start(self.entry, True, True, 0)

        self.button = Gtk.Button(label="Enviar")
        self.button.connect("clicked", self.enviar)
        self.box.pack_start(self.button, True, True, 0)

        self.textview = Gtk.TextView()
        self.textview.set_editable(False)
        self.box.pack_start(self.textview, True, True, 0)

    def enviar(self, widget):
        msg = self.entry.get_text()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((host, port))
            client.sendall(msg.encode('utf8'))
            data = client.recv(1024)
            self.exibir_resposta(data.decode('utf8'))

    def exibir_resposta(self, resposta):
        buffer = self.textview.get_buffer()
        buffer.set_text(resposta)

win = ClienteGTK()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()

