def ascii_to_binary(text):
    """
    Convierte un texto en su representación binaria, utilizando el valor ASCII de cada carácter.

    Esta función toma un texto y convierte cada carácter en su equivalente binario de 8 bits,
    basado en su valor ASCII. Los valores binarios se separan por espacios.

    Parámetros:
    -----------
    text : str
        El texto que se desea convertir a su representación binaria.

    Retorna:
    --------
    str
        Una cadena que representa el texto en formato binario, donde cada carácter está
        representado por su valor binario de 8 bits, separado por espacios.

    Ejemplo:
    --------
    >>> texto = "Hola"
    >>> ascii_to_binary(texto)
    '01001000 01101111 01101100 01100001'
    """
    binary = ' '.join(format(ord(char), '08b') for char in text)
    return binary

# Ejemplo de uso
texto = "Hola"
print(ascii_to_binary(texto))  # Salida: 01001000 01101111 01101100 01100001