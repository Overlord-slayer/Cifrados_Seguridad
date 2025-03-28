import socket
import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Configuración del servidor
SERVER_IP = '127.0.0.1'  # Cambia esto si el servidor está en otra máquina
PORT = 4444

# Clave y IV (deben ser de 16, 24 o 32 bytes para AES)
KEY = b'Sixteen byte key'  # 16 bytes
IV = os.urandom(16)        # Generar IV aleatorio

def encrypt_message(message, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(message.encode(), AES.block_size))
    return iv + encrypted  # Enviar IV + datos cifrados

# Crear socket y conectarse al servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

# Mensaje a enviar
mensaje = "Mensaje Secreto"
encrypted_message = encrypt_message(mensaje, KEY, IV)

# Enviar datos cifrados
client_socket.sendall(encrypted_message)
print(f"[*] Mensaje cifrado enviado: {encrypted_message.hex()}")

client_socket.close()
