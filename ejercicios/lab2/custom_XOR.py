def xor_strings(text, key):
    key = (key * (len(text) // len(key) + 1))[:len(text)]  # Ajustamos la clave al tamaño del texto
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(text, key))

# Ejemplo
mensaje = "Hola"
llave = "key"
resultado = xor_strings(mensaje, llave)
print(resultado)  # Texto cifrado con XOR

# Para descifrar, solo se aplica XOR de nuevo
print(xor_strings(resultado, llave))  # Debería devolver "Hola"
