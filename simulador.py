import socket
import threading

# Funções auxiliares
from aux import *

# Rotinas da Camada de Enlace
from camada_enlace.rotines import *

# Rotinas da Camada Física
from camada_fisica.rotines import *


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))
server.listen(5)

clients = {}  # Armazena os clientes e seus nomes de usuário

def lidar_cliente(client):
    username = client.recv(1024).decode()  # Recebe o nome de usuário
    clients[client] = username  # Adiciona o cliente à lista de clientes conectados
    client.send(bytes(f"Você está logado como {username}!\nCaso queria enviar uma mensagem sem passar pelos protocolos de rede, deixe o segundo terminal vazio.\n", "utf8"))
    commands_help(client)

    while True:
        try:
            msg = client.recv(2048)
            if msg:
                # Decodifica a mensagem recebida e separa o remetente e as mensagens
                decoded_msg = msg.decode().split(" : ")

                if len(decoded_msg) >= 2:
                    sender = decoded_msg[0]  # Nome de usuário
                    message = decoded_msg[1]  # Mensagem
                    commands = decoded_msg[2] if len(decoded_msg) > 2 else ""  # Comandos 
                    
                    if commands:
                        cmd_mod_digital, cmd_mod_portadora, cmd_enquadramento, cmd_deteccao_err = commands.split(" ")

                        bits = transformar_para_bits(message)
                        client.send(bytes(f'Bits -> {transformar_para_bits(message)}',"utf8"))

                        # Enquadramento - Transmissor
                        msg_enquadrada = enquadramento_transmissor(bits, cmd_enquadramento)
                        client.send(bytes(f'Enquadramento -> {msg_enquadrada}',"utf8"))

                        # Detecção de erros - Transmissor
                        msg_pos_deteccao_err_trans = deteccao_err_transmissor(msg_enquadrada, cmd_deteccao_err)
                        client.send(bytes(f'Detecção de erros -> {msg_pos_deteccao_err_trans}',"utf8"))

                        # Hamming - Transmissor
                        msg_pos_correcao_err_trans = hamming.transmissor_hp(msg_pos_deteccao_err_trans)
                        client.send(bytes(f'Hamming -> {msg_pos_correcao_err_trans}\n',"utf8"))

                        # Modulação digital
                        modulacao_digital(msg_pos_correcao_err_trans, cmd_mod_digital)

                        # Modulação por portadora
                        modulacao_portadora(msg_pos_correcao_err_trans, cmd_mod_portadora)

                        # Hamming - Receptor
                        msg_pos_correcao_err_rec = hamming.receptor_hp(msg_pos_correcao_err_trans)

                        # Detecção de erros - Receptor
                        eh_valido, msg_pos_deteccao_err_rec = deteccao_err_receptor(msg_pos_correcao_err_rec, cmd_deteccao_err)
                        if not eh_valido:
                            break

                        # Enquadramento - Receptor
                        msg_desenquadrada = enquadramento_receptor(msg_pos_deteccao_err_rec, cmd_enquadramento)

                        send_message = f"{sender}: {transformar_para_ascii(msg_desenquadrada)}"
                        enviar_msg(bytes(send_message, "utf8"))
                    else:
                        send_message = f"{sender}: {message}"
                        enviar_msg(bytes(send_message, "utf8"))
            else:
                # Conexão fechada abruptamente
                client.close()
                del clients[client]
                enviar_msg(bytes(f"{username} saiu do chat.", "utf8"))
                break
        except:
            # Em caso de erro, desconecta o cliente
            client.close()
            del clients[client]
            enviar_msg(bytes(f"{username} saiu do chat.", "utf8"))
            break

def commands_help(client):
    client.send(bytes("\nAjuda com comandos:\n", "utf8"))
    client.send(bytes("O segundo terminal é apenas para comandos!\n\n", "utf8"))
    client.send(bytes("Para escolher modulação digital: md[1-3]\n1- NRZ-Polar\n2- Manchester\n3- Bipolar\n\n", "utf8"))
    client.send(bytes("Para escolher modulação de portadora: mp[1-3]\n1- ASK\n2- FSK\n3- 8-QAM\n\n", "utf8"))
    client.send(bytes("Para escolher enquadramento de dados: e[1-2]\n1- Contagem de caracteres\n2- Inserção de bytes ou caracteres\n\n", "utf8"))
    client.send(bytes("Para escolher detecção de erros: de[1-2]\n1- Bit de paridade par\n2- CRC\n\n", "utf8"))
    client.send(bytes("Exemplo de uso no terminal de comando:\nmd1 mp2 e1 de2\n\n", "utf8"))
    client.send(bytes("Siga a ordem mostrada!\n", "utf8"))
    client.send(bytes("Não se esqueça dos espaços entre escolhas!\n", "utf8"))

def enviar_msg(msg):
    for client in clients:
        client.send(msg)

while True:
    client, client_address = server.accept()
    threading.Thread(target=lidar_cliente, args=(client,)).start()
