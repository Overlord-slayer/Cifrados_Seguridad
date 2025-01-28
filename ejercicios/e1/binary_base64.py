from const import BASE64_CHARS

def binary_to_base64(binary):
    """
    Convierte una cadena binaria a su representación en formato BASE64.

    Esta función toma una cadena binaria, la divide en grupos de 6 bits y convierte cada grupo
    en su carácter BASE64 correspondiente. Si la longitud del binario no es múltiplo de 6,
    se rellena con ceros. Además, se añade relleno '=' al final si es necesario para que la
    longitud de la cadena BASE64 sea múltiplo de 4.

    Parámetros:
    -----------
    binary : str
        La cadena binaria que se desea convertir a formato BASE64.

    Retorna:
    --------
    str
        Una cadena en formato BASE64 que representa la conversión de la cadena binaria.

    Ejemplo:
    --------
    >>> binario = "01001000011011110110110001100001"
    >>> binary_to_base64(binario)
    'SG9sYQ=='
    """
    # Asegurarse de que la longitud del binario sea múltiplo de 6
    padding = len(binary) % 6
    if padding != 0:
        binary += '0' * (6 - padding)  # Rellenar con ceros
    # Dividir el binario en grupos de 6 bits
    groups = [binary[i:i+6] for i in range(0, len(binary), 6)]
    # Convertir cada grupo a su carácter BASE64 correspondiente
    base64_text = ''
    for group in groups:
        index = int(group, 2)
        base64_text += BASE64_CHARS[index]
    # Añadir relleno '=' si es necesario
    padding = len(base64_text) % 4
    if padding != 0:
        base64_text += '=' * (4 - padding)
    return base64_text

# Ejemplo de uso
binario = "01001000011011110110110001100001"
print(binary_to_base64(binario))  # Salida: SG9sYQ==