from const import BASE64_CHARS

def base64_to_binary(text):
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