import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))
server.listen(5)

clients = {}  # Armazena os clientes e seus nomes de usuário

def lidar_cliente(client):
    username = client.recv(1024).decode()  # Recebe o nome de usuário
    clients[client] = username  # Adiciona o cliente à lista de clientes conectados
    client.send(bytes(f"Você está logado como {username}! \n", "utf8"))
    

    while True:
        try:
            msg = client.recv(2048)
            if msg:
                # Decodifica a mensagem recebida e separa o remetente e a mensagem
                decoded_msg = msg.decode().split(": ", 1)  # Divide a string apenas uma vez
                if len(decoded_msg) == 2:
                    sender, message = decoded_msg
                    enviar_msg(bytes(f"{sender}: {message}", "utf8"))
                else:
                    # Se o cliente enviou "{quit}", desconecta
                    if msg.decode() == "{quit}":
                        client.send(bytes("{quit}", "utf8"))
                        client.close()
                        del clients[client]
                        enviar_msg(bytes(f"{username} saiu do chat.", "utf8"))
                        break
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

def trasnsformar_para_bit(msg):
    byte_msg = ""
    for i in list(msg):
        if len(bin(i).split("b")[1]) != 8:
            byte_msg = f'{byte_msg}0{bin(i).split("b")[1]}'
        else:
            byte_msg = f'{byte_msg}{bin(i).split("b")[1]}'
    if "01110100100000" in byte_msg:
        byte_msg = byte_msg.split("01110100100000")[1]
    return byte_msg

def enviar_msg(msg):
    for client in clients:
        client.send(msg)

while True:
    client, client_address = server.accept()
    threading.Thread(target=lidar_cliente, args=(client,)).start()
