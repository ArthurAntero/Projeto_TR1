import socket

host = '127.0.0.1'
port = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

def lidar_com_cliente(host, port):
    conn, addr = server.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))
        conn.sendall(data)
    conn.close()

lidar_com_cliente(host, port)