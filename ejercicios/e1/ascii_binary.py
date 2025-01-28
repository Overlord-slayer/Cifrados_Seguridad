def ascii_to_binary(text):
    binary = ' '.join(format(ord(char), '08b') for char in text)
    return binary

# Ejemplo de uso
texto = "Hola"
print(ascii_to_binary(texto))  # Salida: 01001000 01101111 01101100 01100001