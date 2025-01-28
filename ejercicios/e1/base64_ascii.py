from base64_binary import base64_to_binary
from binay_ascii import binary_to_ascii

def base64_to_ascii(text):
    """
    Convierte una cadena en formato BASE64 a su representación en texto ASCII.

    Esta función toma una cadena codificada en BASE64, la convierte a su representación binaria
    y luego la transforma en texto ASCII.

    Parámetros:
    -----------
    text : str
        La cadena en formato BASE64 que se desea convertir a texto ASCII.

    Retorna:
    --------
    str
        Una cadena que representa el texto ASCII resultante de la conversión.

    Ejemplo:
    --------
    >>> texto_base64 = "SG9sYQ=="
    >>> base64_to_ascii(texto_base64)
    'Hola'
    """
    # Convertir BASE64 a binario
    binary = base64_to_binary(text)
    # Convertir binario a ASCII
    ascii_text = binary_to_ascii(binary)
    return ascii_text

# Ejemplo de uso
texto_base64 = "SG9sYQ=="
print(base64_to_ascii(texto_base64))  # Salida: Hola