import socket
import threading
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

class Host(Gtk.Window):
    def __init__(self):
        super().__init__(title="Host")
        self.set_default_size(900, 900)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.client_socket = None
        self.username = None

        self.chatbox = Gtk.TextView()
        self.chatbox.set_editable(False)
        self.chatbox.set_wrap_mode(Gtk.WrapMode.WORD)
        self.chat_scroll = Gtk.ScrolledWindow()
        self.chat_scroll.set_vexpand(True)
        self.chat_scroll.add(self.chatbox)

        # Primeiro terminal de entrada de mensagem
        self.message_entry1 = Gtk.Entry()
        self.message_entry1.set_hexpand(True)

        # Segundo terminal de entrada de mensagem (opcional)
        self.message_entry2 = Gtk.Entry()
        self.message_entry2.set_hexpand(True)

        # Botão de enviar
        self.send_button = Gtk.Button(label="Enviar")
        self.send_button.connect("clicked", self.enviar_msg)

        # Layout da interface
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.box.set_margin_top(20)
        self.box.set_margin_bottom(20)
        self.box.set_margin_start(20)
        self.box.set_margin_end(20)

        self.box.pack_start(self.chat_scroll, True, True, 0)

        # Adicionando o primeiro terminal à interface
        self.entry_box1 = Gtk.Box(spacing=5)
        self.entry_box1.pack_start(self.message_entry1, True, True, 0)
        self.box.pack_start(self.entry_box1, False, False, 0)

        # Adicionando o segundo terminal à interface
        self.entry_box2 = Gtk.Box(spacing=5)
        self.entry_box2.pack_start(self.message_entry2, True, True, 0)
        self.box.pack_start(self.entry_box2, False, False, 0)

        # Adicionando o botão de envio
        self.box.pack_start(self.send_button, False, False, 0)

        self.add(self.box)

        self.connect("destroy", self.on_closing)
        self.show_all()

        self.conectar_ao_servidor()

    def conectar_ao_servidor(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            IP_ADDRESS = '127.0.0.1'
            PORT = 12345
            self.client_socket.connect((IP_ADDRESS, PORT))

            dialog = Gtk.MessageDialog(
                parent=self, 
                modal=True,
                destroy_with_parent=True,
                message_type=Gtk.MessageType.QUESTION,
                buttons=Gtk.ButtonsType.OK_CANCEL,
                text="Username"
            )            
            dialog.format_secondary_text("Por favor, insira seu nome de usuário.")
            dialog.set_default_response(Gtk.ResponseType.OK)
            entry = Gtk.Entry()
            dialog.vbox.pack_end(entry, False, False, 0)
            entry.show()
            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                self.username = entry.get_text()
                self.client_socket.send(self.username.encode())
                threading.Thread(target=self.receber_msg).start()
            dialog.destroy()
        except:
            error_dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, "Erro")
            error_dialog.format_secondary_text("Não foi possível se conectar ao servidor.")
            error_dialog.run()
            error_dialog.destroy()
            self.destroy()

    def enviar_msg(self, widget):
        message1 = self.message_entry1.get_text()
        message2 = self.message_entry2.get_text()

        # Construa a mensagem concatenando os campos de entrada
        if message2:
            formatted_message = f"{self.username} : {message1} : {message2}"
        else:
            formatted_message = f"{self.username} : {message1}"

        if message1:
            self.client_socket.send(formatted_message.encode())
            self.message_entry1.set_text("")
            self.message_entry2.set_text("")  # Limpa o segundo campo também

    def receber_msg(self):
        while True:
            try:
                message = self.client_socket.recv(2048).decode()
                GLib.idle_add(self.update_chatbox, message)
            except:
                info_dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Informação")
                info_dialog.format_secondary_text("Desconectado do servidor.")
                info_dialog.run()
                info_dialog.destroy()
                break

    def update_chatbox(self, message):
        buffer = self.chatbox.get_buffer()
        buffer.insert(buffer.get_end_iter(), message + "\n")
        self.chatbox.scroll_mark_onscreen(buffer.get_insert())

    def on_closing(self):
        if self.client_socket:
            self.client_socket.close()
        Gtk.main_quit()

if __name__ == "__main__":
    app = Host()
    Gtk.main()
