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
    msg = f"{username} entrou no chat!"
    enviar_msg(bytes(msg, "utf8"))  # Notifica todos os clientes que um novo usuário entrou no chat

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

def enviar_msg(msg):
    """Envia uma mensagem para todos os clientes conectados."""
    for client in clients:
        client.send(msg)

while True:
    client, client_address = server.accept()
    threading.Thread(target=lidar_cliente, args=(client,)).start()
