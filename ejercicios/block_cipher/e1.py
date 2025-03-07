from Crypto.Cipher import DES
import os

def pad(text):
    """
    Aplica PKCS7 padding manualmente.
    
    Args:
        text (bytes): Texto a rellenar.
    
    Returns:
        bytes: Texto con padding aplicado.
    """
    pad_len = 8 - (len(text) % 8)
    return text + bytes([pad_len] * pad_len)

def unpad(text):
    """
    Remueve el padding PKCS7.
    
    Args:
        text (bytes): Texto con padding.
    
    Returns:
        bytes: Texto sin padding.
    """
    pad_len = text[-1]
    return text[:-pad_len]

def generate_key():
    """
    Genera una clave aleatoria de 8 bytes para DES.
    
    Returns:
        bytes: Clave de 8 bytes.
    """
    return os.urandom(8)

def des_encrypt(plain_text, key):
    """
    Cifra un mensaje usando DES en modo ECB.
    
    Args:
        plain_text (str): Mensaje en texto plano.
        key (bytes): Clave de 8 bytes.
    
    Returns:
        bytes: Mensaje cifrado.
    """
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text.encode())
    return cipher.encrypt(padded_text)

def des_decrypt(cipher_text, key):
    """
    Descifra un mensaje cifrado con DES en modo ECB.
    
    Args:
        cipher_text (bytes): Mensaje cifrado.
        key (bytes): Clave de 8 bytes.
    
    Returns:
        str: Mensaje descifrado.
    """
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(cipher_text)
    return unpad(decrypted_text).decode()

# Ejemplo de uso
key = generate_key()
with open("des.txt", "r", encoding="utf-8") as file:
    contenido = file.read()
print(contenido)

# message = "Hola, mundo!"
cipher_text = des_encrypt(contenido, key)
print("Mensaje cifrado:", cipher_text)
decrypted_message = des_decrypt(cipher_text, key)
print("Mensaje descifrado:", decrypted_message)
