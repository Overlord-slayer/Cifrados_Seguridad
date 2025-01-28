def cifrar_ascii(texto, llave):
    """
    Cifra un texto utilizando una clave mediante la operación XOR a nivel de caracteres ASCII.

    Esta función toma un texto y una clave, y aplica la operación XOR entre cada carácter del texto
    y el carácter correspondiente de la clave. La clave debe tener la misma longitud que el texto.

    Parámetros:
    -----------
    texto : str
        El texto que se desea cifrar.
    llave : str
        La clave que se utilizará para cifrar el texto. Debe tener la misma longitud que el texto.

    Retorna:
    --------
    str
        El texto cifrado resultante de aplicar la operación XOR entre el texto y la clave.

    Lanza:
    ------
    ValueError
        Si la longitud de la clave no coincide con la longitud del texto.

    Ejemplo:
    --------
    >>> texto = "Hola"
    >>> llave = "abcd"
    >>> cifrar_ascii(texto, llave)
    'un texto cifrado'
    """
    # Asegurarse de que la llave tenga la misma longitud que el texto
    if len(texto) != len(llave):
        raise ValueError("La llave debe tener la misma longitud que el texto")
    # Aplicar XOR entre el texto y la llave
    cifrado = ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(texto, llave))
    return cifrado

# Ejemplo de uso
texto = "Hola"
llave = "abcd"
print(cifrar_ascii(texto, llave))  # Salida: un texto cifrado