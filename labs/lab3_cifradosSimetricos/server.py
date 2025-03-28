import socket

SERVER_IP = "0.0.0.0"  # Escucha en todas las interfaces
SERVER_PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, SERVER_PORT))
server.listen(5)
print(f"Servidor escuchando en {SERVER_IP}:{SERVER_PORT}")

conn, addr = server.accept()
print(f"Conexión establecida con {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"Mensaje cifrado recibido: {data.decode()}")

conn.close()
server.close()
