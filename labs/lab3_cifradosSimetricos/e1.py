"""
AES Image Encryption

Este script cifra imágenes en escala de grises utilizando el algoritmo AES en modos ECB y CBC.
La imagen es convertida en bytes, cifrada y guardada en disco.

@author: Autor del código
@version: 1.0
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import numpy as np
import cv2

# Configuración de clave y vector de inicialización
KEY = b'1234567890abcdef'  # Clave de 16 bytes (AES-128)
IV = b'abcdef1234567890'   # Vector de inicialización para CBC (16 bytes)

def load_image(image_path: str) -> np.ndarray:
    """
    Carga una imagen en escala de grises.

    @param image_path: Ruta de la imagen.
    @return: Imagen cargada como un array de NumPy.
    """
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Error al cargar la imagen. Verifica el formato y la ruta.")
    return img

def save_image(image: np.ndarray, output_path: str) -> None:
    """
    Guarda la imagen en el disco.

    @param image: Imagen en formato NumPy array.
    @param output_path: Ruta donde se guardará la imagen.
    """
    cv2.imwrite(output_path, image)

def encrypt_ecb(image: np.ndarray, key: bytes) -> np.ndarray:
    """
    Cifra una imagen usando AES en modo ECB.

    @param image: Imagen en formato NumPy array.
    @param key: Clave AES de 16 bytes.
    @return: Imagen cifrada como NumPy array.
    """
    cipher = AES.new(key, AES.MODE_ECB)
    img_bytes = image.tobytes()
    encrypted_bytes = cipher.encrypt(pad(img_bytes, AES.block_size))
    return np.frombuffer(encrypted_bytes, dtype=np.uint8)[:image.size].reshape(image.shape)

def encrypt_cbc(image: np.ndarray, key: bytes, iv: bytes) -> np.ndarray:
    """
    Cifra una imagen usando AES en modo CBC.

    @param image: Imagen en formato NumPy array.
    @param key: Clave AES de 16 bytes.
    @param iv: Vector de inicialización de 16 bytes.
    @return: Imagen cifrada como NumPy array.
    """
    cipher = AES.new(key, AES.MODE_CBC, iv)
    img_bytes = image.tobytes()
    encrypted_bytes = cipher.encrypt(pad(img_bytes, AES.block_size))
    return np.frombuffer(encrypted_bytes, dtype=np.uint8)[:image.size].reshape(image.shape)

# --- Carga de Imagen ---
image_path = "diagrama.png"  # Cambia esto por la ruta de la imagen deseada
output_ecb = "diagrama_ecb.png"
output_cbc = "diagrama_cbc.png"

tux = load_image(image_path)

# --- Cifrado ---
tux_ecb = encrypt_ecb(tux, KEY)
save_image(tux_ecb, output_ecb)

tux_cbc = encrypt_cbc(tux, KEY, IV)
save_image(tux_cbc, output_cbc)

print(f"Cifrado completado. Se generaron {output_ecb} y {output_cbc}.")
