def xor_strings(text, key):
    """
    Aplica la operación XOR entre una cadena de texto y una clave.

    La función cifra o descifra un texto aplicando la operación XOR (`^`) entre
    cada carácter del texto y la clave proporcionada. Si se aplica dos veces 
    con la misma clave, el texto vuelve a su estado original.

    Parámetros:
        text (str): La cadena de texto a cifrar/descifrar.
        key (str): La clave utilizada para la operación XOR.

    Retorna:
        str: La cadena resultante después de aplicar XOR.

    Ejemplo:
        >>> xor_strings("Hola", "key")
        '\x03\n\x00\x0c'

        >>> xor_strings('\x03\n\x00\x0c', "key")
        'Hola'
    """

    # Paso 1: Ajustar la clave al tamaño del texto
    key = (key * (len(text) // len(key) + 1))[:len(text)]
    print("Paso 1 - Clave ajustada al tamaño del texto:", key)

    # Paso 2: Aplicar XOR entre cada carácter del texto y la clave
    xor_result = [chr(ord(a) ^ ord(b)) for a, b in zip(text, key)]
    print("Paso 2 - Resultado en valores ASCII después de XOR:", [ord(c) for c in xor_result])

    # Paso 3: Convertir la lista en una cadena final
    result = ''.join(xor_result)
    print("Paso 3 - Texto cifrado/descifrado:", result)

    return result

# Ejemplo de uso
mensaje = "Hola papa"
llave = "key"

# Cifrar
resultado = xor_strings(mensaje, llave)
print("Texto cifrado:", resultado)

# Descifrar (aplicamos XOR de nuevo con la misma clave)
texto_descifrado = xor_strings(resultado, llave)
print("Texto descifrado:", texto_descifrado)
