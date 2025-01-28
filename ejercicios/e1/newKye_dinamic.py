def cifrar_ascii_dinamico(texto, llave):
    """
    Cifra un texto utilizando una clave dinámica mediante la operación XOR a nivel de caracteres ASCII.

    Esta función toma un texto y una clave, y repite la clave si es más corta que el texto.
    Luego, aplica la operación XOR entre cada carácter del texto y el carácter correspondiente
    de la clave repetida, generando un texto cifrado.

    Parámetros:
    -----------
    texto : str
        El texto que se desea cifrar.
    llave : str
        La clave que se utilizará para cifrar el texto. Si la clave es más corta que el texto,
        se repetirá hasta que coincida en longitud.

    Retorna:
    --------
    str
        El texto cifrado resultante de aplicar la operación XOR entre el texto y la clave.

    Ejemplo:
    --------
    >>> texto = "HolaMundo"
    >>> llave = "abc"
    >>> cifrar_ascii_dinamico(texto, llave)
    'un texto cifrado'
    """
    # Repetir la llave si es más corta que el texto
    llave_repetida = (llave * (len(texto) // len(llave))) + llave[:len(texto) % len(llave)]
    # Aplicar XOR entre el texto y la llave repetida
    cifrado = ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(texto, llave_repetida))
    return cifrado

# Ejemplo de uso
texto = "HolaMundo"
llave = "abc"
print(cifrar_ascii_dinamico(texto, llave))  # Salida: un texto cifrado