from base64_binary import base64_to_binary
from binay_ascii import binary_to_ascii


def base64_to_ascii(text):
    # Convertir BASE64 a binario
    binary = base64_to_binary(text)
    # Convertir binario a ASCII
    ascii_text = binary_to_ascii(binary)
    return ascii_text

# Ejemplo de uso
texto_base64 = "SG9sYQ=="
print(base64_to_ascii(texto_base64))  # Salida: Hola