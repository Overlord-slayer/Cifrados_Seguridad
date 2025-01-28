def cifrar_ascii(texto, llave):
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