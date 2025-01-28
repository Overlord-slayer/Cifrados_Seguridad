from const import BASE64_CHARS

def binary_to_base64(binary):
    # Asegurarse de que la longitud del binario sea múltiplo de 6
    padding = len(binary) % 6
    if padding != 0:
        binary += '0' * (6 - padding)  # Rellenar con ceros
    # Dividir el binario en grupos de 6 bits
    groups = [binary[i:i+6] for i in range(0, len(binary), 6)]
    # Convertir cada grupo a su carácter BASE64 correspondiente
    base64_text = ''
    for group in groups:
        index = int(group, 2)
        base64_text += BASE64_CHARS[index]
    # Añadir relleno '=' si es necesario
    padding = len(base64_text) % 4
    if padding != 0:
        base64_text += '=' * (4 - padding)
    return base64_text

# Ejemplo de uso
binario = "01001000011011110110110001100001"
print(binary_to_base64(binario))  # Salida: SG9sYQ==