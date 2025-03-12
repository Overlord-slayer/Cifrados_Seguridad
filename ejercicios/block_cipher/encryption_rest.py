from Crypto.Cipher import DES3, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_3des_key():
    """
    Genera una clave aleatoria válida de 24 bytes para 3DES con ajuste de paridad.
    
    Returns:
        bytes: Clave de 24 bytes para 3DES.
    """
    while True:
        key = get_random_bytes(24)  # 3DES usa una llave de 24 bytes (192 bits)
        try:
            DES3.adjust_key_parity(key)
            return key
        except ValueError:
            continue

def triple_des_encrypt(plaintext):
    """
    Cifra un texto plano usando 3DES en modo CBC.
    
    Args:
        plaintext (str): Texto a cifrar.
    
    Returns:
        tuple: Clave, IV y texto cifrado.
    """
    key = generate_3des_key()
    iv = get_random_bytes(8)  # IV de 8 bytes para CBC
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), DES3.block_size))
    return key, iv, ciphertext

def triple_des_decrypt(key, iv, ciphertext):
    """
    Descifra un texto cifrado con 3DES en modo CBC.
    
    Args:
        key (bytes): Clave de 24 bytes.
        iv (bytes): Vector de inicialización de 8 bytes.
        ciphertext (bytes): Texto cifrado.
    
    Returns:
        str: Texto descifrado.
    """
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), DES3.block_size).decode()

def generate_aes_key():
    """
    Genera una clave aleatoria de 32 bytes para AES-256.
    
    Returns:
        bytes: Clave de 32 bytes.
    """
    return get_random_bytes(32)

def aes_encrypt(plaintext, mode=AES.MODE_CBC):
    """
    Cifra un texto plano usando AES en modo CBC o ECB.
    
    Args:
        plaintext (str): Texto a cifrar.
        mode (int, optional): Modo de operación (CBC por defecto).
    
    Returns:
        tuple: Clave, IV (None si ECB) y texto cifrado.
    """
    key = generate_aes_key()
    iv = get_random_bytes(16) if mode == AES.MODE_CBC else None
    cipher = AES.new(key, mode, iv) if iv else AES.new(key, mode)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return key, iv, ciphertext

def aes_decrypt(key, iv, ciphertext, mode=AES.MODE_CBC):
    """
    Descifra un texto cifrado con AES en modo CBC o ECB.
    
    Args:
        key (bytes): Clave de 32 bytes.
        iv (bytes or None): Vector de inicialización de 16 bytes (None si ECB).
        ciphertext (bytes): Texto cifrado.
        mode (int, optional): Modo de operación (CBC por defecto).
    
    Returns:
        str: Texto descifrado.
    """
    cipher = AES.new(key, mode, iv) if iv else AES.new(key, mode)
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()

def aes_encrypt_image(input_path, output_path, mode=AES.MODE_CBC):
    """
    Cifra una imagen usando AES en modo CBC o ECB y la guarda en un archivo.
    
    Args:
        input_path (str): Ruta del archivo de imagen de entrada.
        output_path (str): Ruta del archivo de imagen cifrado.
        mode (int, optional): Modo de operación AES (CBC por defecto).
    
    Returns:
        tuple: Clave y IV utilizados para el cifrado.
    """
    key = generate_aes_key()
    iv = get_random_bytes(16) if mode == AES.MODE_CBC else None
    cipher = AES.new(key, mode, iv) if iv else AES.new(key, mode)
    
    with open(input_path, "rb") as f:
        header = f.read(54)  # BMP header
        image_data = f.read()
    
    encrypted_data = header + cipher.encrypt(pad(image_data, AES.block_size))
    
    with open(output_path, "wb") as f:
        f.write(encrypted_data)
    
    return key, iv

def aes_decrypt_image(input_path, output_path, key, iv, mode=AES.MODE_CBC):
    """
    Descifra una imagen cifrada con AES y la guarda en un archivo.
    
    Args:
        input_path (str): Ruta del archivo de imagen cifrado.
        output_path (str): Ruta del archivo de imagen descifrado.
        key (bytes): Clave AES utilizada para el cifrado.
        iv (bytes or None): Vector de inicialización (None si ECB).
        mode (int, optional): Modo de operación AES (CBC por defecto).
    """
    cipher = AES.new(key, mode, iv) if iv else AES.new(key, mode)
    
    with open(input_path, "rb") as f:
        header = f.read(54)
        encrypted_data = f.read()
    
    decrypted_data = header + unpad(cipher.decrypt(encrypted_data), AES.block_size)
    
    with open(output_path, "wb") as f:
        f.write(decrypted_data)

# Ejemplo de uso
if __name__ == "__main__":
    
    with open("3des.txt", "r", encoding="utf-8") as file:
        contenido = file.read()
    print(contenido)

    # 3DES
    print("\n--- 3DES ---")
    key_3des, iv_3des, encrypted_3des = triple_des_encrypt(contenido)
    print(f"TEXTO CIFRADO 1 3DES {encrypted_3des}")
    decrypted_3des = triple_des_decrypt(key_3des, iv_3des, encrypted_3des)
    print(f"3DES: {decrypted_3des}")
    

    # AES CBC
    print("\n--- AES CBC ---")
    key_aes, iv_aes, encrypted_aes_cbc = aes_encrypt(contenido, AES.MODE_CBC)
    print(f"TEXTO CIFRADO 2, AES CBC {encrypted_aes_cbc}")
    decrypted_aes_cbc = aes_decrypt(key_aes, iv_aes, encrypted_aes_cbc, AES.MODE_CBC)
    print(f"AES CBC: {decrypted_aes_cbc}")
    
    # AES ECB
    print("\n--- AES ECB ---")
    key_aes_ecb, _, encrypted_aes_ecb = aes_encrypt(contenido, AES.MODE_ECB)
    print(f"TEXTO CIFRADO PARA , AES ECB {encrypted_aes_ecb}")
    decrypted_aes_ecb = aes_decrypt(key_aes_ecb, None, encrypted_aes_ecb, AES.MODE_ECB)
    print(f"AES ECB: {decrypted_aes_ecb}")

    print("\n--- Cifrado de Imagen ---")
    key_img, iv_img = aes_encrypt_image("pic.png", "pic_encrypted.png", AES.MODE_CBC)
    aes_decrypt_image("pic_encrypted.png", "pic_decrypted.png", key_img, iv_img, AES.MODE_CBC)
    print("Imagen cifrada y descifrada correctamente.")
    