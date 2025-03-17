import socket
import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Configuración
SERVER_IP = "127.0.0.1"  # Cambia esto a la IP del servidor
SERVER_PORT = 12345
KEY = os.urandom(16)  # Clave AES de 16 bytes (128 bits)
IV = os.urandom(16)  # Vector de inicialización de 16 bytes

def encrypt_message(message):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return base64.b64encode(IV + ciphertext).decode()

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, SERVER_PORT))
    print("Conectado al servidor")
    
    while True:
        message = input("Mensaje: ")
        if message.lower() == "salir":
            break
        encrypted_message = encrypt_message(message)
        client.send(encrypted_message.encode())
        print("Mensaje cifrado enviado")
    
    client.close()
    print("Conexión cerrada")

if __name__ == "__main__":
    main()
