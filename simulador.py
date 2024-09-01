import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))
server.listen(5)

clients = {}  # Armazena os clientes e seus nomes de usuário

def lidar_cliente(client):
    username = client.recv(1024).decode()  # Recebe o nome de usuário
    clients[client] = username  # Adiciona o cliente à lista de clientes conectados
    client.send(bytes(f"Você está logado como {username}!\nDigite /help no primeiro terminal com o segundo vazio para ajuda com comandos.\n", "utf8"))
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
                    
                    send_message = f"{sender}: {message}"
                    enviar_msg(bytes(send_message, "utf8"))

                    if commands != "":
                        if commands.split(" ")[3][-1] == "1":
                            #bit_de_paridade_par()
                            print("Bit de paridade par")
                        elif commands.split(" ")[3][-1] == "2":
                            #crc()
                            print("CRC")

                        # Hamming
                        print("Hamming")

                        if commands.split(" ")[2][-1] == "1":
                            #Contagem de caracteres
                            print("Contagem de caracteres")
                        elif commands.split(" ")[2][-1] == "2":
                            #Insercao de bytes ou caracteres
                            print("Insercao de bytes ou caracteres")

                        if commands.split(" ")[0][-1] == "1":
                            #NRZ Polar
                            print("NRZ Polar")
                        elif commands.split(" ")[0] == "2":
                            #Manchester
                            print("Manchester")
                        elif commands.split(" ")[0][-1] == "3":
                            #Bipolar
                            print("Bipolar")

                        if commands.split(" ")[1][-1] == "1":
                            #ASK
                            print("ASK")
                        elif commands.split(" ")[1][-1] == "2":
                            #FSK
                            print("FSK")
                        elif commands.split(" ")[1][-1] == "3":
                            #8-QAM
                            print("8-QAM")

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
