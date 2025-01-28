def cifrar_ascii_dinamico(texto, llave):
    # Repetir la llave si es más corta que el texto
    llave_repetida = (llave * (len(texto) // len(llave))) + llave[:len(texto) % len(llave)]
    # Aplicar XOR entre el texto y la llave repetida
    cifrado = ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(texto, llave_repetida))
    return cifrado

# Ejemplo de uso
texto = "HolaMundo"
llave = "abc"
print(cifrar_ascii_dinamico(texto, llave))  # Salida: un texto cifrado