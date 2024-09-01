import socket
import threading

# Camada de Enlace - Detecção de erros
from camada_enlace.deteccao_erros.bit_paridade_par import *
from camada_enlace.deteccao_erros.crc import *

# Camada de Enlace - Correção de erros
from camada_enlace.correcao_erros.hamming import *

# Camada de Enlace - Enquadramento
from camada_enlace.enquadramento.contagem_caracteres import *
from camada_enlace.enquadramento.insercao_bytes import *

# Camada Física - Modulação Digital
from camada_fisica.mod_digital.bipolar import *
from camada_fisica.mod_digital.manchester import *
from camada_fisica.mod_digital.nrz_polar import *

# Camada Física - Modulação de Portadora
from camada_fisica.mod_portadora.ask import *
from camada_fisica.mod_portadora.fsk import *
from camada_fisica.mod_portadora.qam import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))
server.listen(5)

clients = {}  # Armazena os clientes e seus nomes de usuário

def lidar_cliente(client):
    username = client.recv(1024).decode()  # Recebe o nome de usuário
    clients[client] = username  # Adiciona o cliente à lista de clientes conectados
    client.send(bytes(f"Você está logado como {username}!\n", "utf8"))
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
                    
                    if commands != "":
                        cmd_mod_dig,cmd_mod_port,cmd_enquad, cmd_det = commands.split(" ")

                        client.send(bytes(f'Bits: {transformar_para_bit(message)}\n',"utf8"))

                        # Enquadramento - Transmissor
                        if cmd_enquad[-1] == "1": #Contagem de caracteres
                            msg_enquadrada = Transmissor_contagem_caractere_bytes(transformar_para_bit(message))
                        elif cmd_enquad[-1] == "2": #Insercao de bytes ou caracteres
                            msg_enquadrada = Transmissor_insercao_bytes(transformar_para_bit(message))

                        client.send(bytes(f'Enquadramento: {msg_enquadrada}\n',"utf8"))
                            
                            
                        # Detecção de erros - Transmissor
                        if cmd_det[-1] == "1": #Bit de paridade par
                            det_err_trans = Transmissor_bit_paridade_par(msg_enquadrada)
                        elif cmd_det[-1] == "2": #CRC
                            det_err_trans = Transmissor_crc(msg_enquadrada)

                        client.send(bytes(f'Detecção de erros: {det_err_trans}\n',"utf8"))

                        # Hamming - Transmissor
                        corr_err_trans = Transmissor_hamming_par(det_err_trans)

                        client.send(bytes(f'Hamming: {corr_err_trans}\n',"utf8"))

                        # Modulação digital
                        if cmd_mod_dig[-1] == "1": #NRZ Polar
                            Transmissor_nrz_polar(corr_err_trans)
                        elif cmd_mod_dig == "2": #Manchester
                            Transmissor_manchester(corr_err_trans)
                        elif cmd_mod_dig[-1] == "3": #Bipolar
                            Transmissor_bipolar(corr_err_trans)

                        # Modulação por portadora
                        if cmd_mod_port[-1] == "1": #ASK
                            Transmissor_ask(corr_err_trans)
                        elif cmd_mod_port[-1] == "2": #FSK
                            Transmissor_fsk(corr_err_trans)
                        elif cmd_mod_port[-1] == "3": #8-QAM
                            Transmissor_8QAM(corr_err_trans)

                        # Hamming - Receptor
                        corr_err_rec = Receptor_hamming_par(corr_err_trans)

                        # Detecção de erros - Receptor
                        if cmd_det[-1] == "1": #Bit de paridade par
                            (eh_valido, det_err_rec) = Receptor_bit_paridade_par(corr_err_rec)
                            if not eh_valido:
                                break
                        elif cmd_det[-1] == "2": #CRC
                            (eh_valido, det_err_rec) = Receptor_crc(corr_err_rec)
                            if not eh_valido:
                                break 

                        # Enquadramento - Receptor
                        if cmd_enquad[-1] == "1": #Contagem de caracteres
                            msg_desenquadrada = Receptor_contagem_caractere_bytes(det_err_rec)
                        elif cmd_enquad[-1] == "2": #Insercao de bytes ou caracteres
                            msg_desenquadrada = Receptor_insercao_bytes(det_err_rec)

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

def transformar_para_bit(msg):
  bits = ""
  for char in msg:
    bits += format(ord(char), "08b")
  return bits

def transformar_para_ascii(bits):
    msg = ""
    for byte_index in range(0, len(bits), 8):
        msg += chr(int(bits[byte_index:byte_index + 8], 2))
    return msg

def commands_help(client):
    client.send(bytes("\nAjuda com comandos:\n", "utf-8"))
    client.send(bytes("O segundo terminal é apenas para comandos!\n\n", "utf-8"))
    client.send(bytes("Para escolher modulação digital: md[1-3]\n1- NRZ-Polar\n2- Manchester\n3- Bipolar\n\n", "utf-8"))
    client.send(bytes("Para escolher modulação de portadora: mp[1-3]\n1- ASK\n2- FSK\n3- 8-QAM\n\n", "utf-8"))
    client.send(bytes("Para escolher enquadramento de dados: e[1-2]\n1- Contagem de caracteres\n2- Inserção de bytes ou caracteres\n\n", "utf-8"))
    client.send(bytes("Para escolher detecção de erros: de[1-2]\n1- Bit de paridade par\n2- CRC\n\n", "utf-8"))
    client.send(bytes("Exemplo de uso no terminal de comando:\nmd1 mp2 e1 de2\n\n", "utf-8"))
    client.send(bytes("Siga a ordem mostrada!\n", "utf-8"))
    client.send(bytes("Não se esqueça dos espaços entre escolhas!\n", "utf-8"))

def enviar_msg(msg):
    for client in clients:
        client.send(msg)

while True:
    client, client_address = server.accept()
    threading.Thread(target=lidar_cliente, args=(client,)).start()
