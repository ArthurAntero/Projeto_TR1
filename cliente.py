import socket

host = '127.0.0.1'
port = 12345
addr = (host, port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

def enviar(msg):
    bin_msg = msg.encode('utf8')
    status = client.send(bin_msg)
    
    if status>0:
        data = client.recv(1024)
        print('Recebido', repr(data))

    client.close()

enviar(input())
