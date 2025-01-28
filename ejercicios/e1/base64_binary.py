from const import BASE64_CHARS

def base64_to_binary(text):
    """
    Convierte una cadena en formato BASE64 a su representación binaria.

    Esta función toma una cadena codificada en BASE64, elimina el relleno '=' si está presente
    y convierte cada carácter BASE64 en su valor binario de 6 bits correspondiente.

    Parámetros:
    -----------
    text : str
        La cadena en formato BASE64 que se desea convertir a binario.

    Retorna:
    --------
    str
        Una cadena binaria que representa la conversión de la cadena BASE64.

    Lanza:
    ------
    ValueError
        Si la cadena contiene un carácter no válido para BASE64.

    Ejemplo:
    --------
    >>> texto_base64 = "SG9sYQ=="
    >>> base64_to_binary(texto_base64)
    '01001000011011110110110001100001'
    """
    # Eliminar relleno '=' si está presente
    text = text.rstrip('=')
    # Convertir cada carácter BASE64 a su valor binario de 6 bits
    binary = ''
    for char in text:
        if char in BASE64_CHARS:
            index = BASE64_CHARS.index(char)
            binary += format(index, '06b')
        else:
            raise ValueError(f"Carácter no válido en BASE64: {char}")
    return binary

# Ejemplo de uso
texto_base64 = "SG9sYQ=="
print(base64_to_binary(texto_base64))  # Salida: 01001000011011110110110001100001