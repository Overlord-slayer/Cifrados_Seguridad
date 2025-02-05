from const import BASE64_ALPHABET

def base64_to_text_manual(base64_text):
    # Eliminar '=' y contar el padding
    padding_chars = base64_text.count('=')
    base64_text = base64_text.rstrip('=')

    # Convertir caracteres Base64 a sus valores binarios de 6 bits
    binary_string = ''.join(format(BASE64_ALPHABET.index(c), '06b') for c in base64_text)

    # Eliminar los bits de padding
    if padding_chars:
        binary_string = binary_string[:-padding_chars * 2]

    # Convertir cada 8 bits a caracteres ASCII
    text = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))

    return text

# Ejemplo
print(base64_to_text_manual("SG9sYQ=="))  # Salida esperada: 'Hola'
