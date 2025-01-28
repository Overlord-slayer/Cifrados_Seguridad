def binary_to_ascii(binary):
    # Dividir el binario en grupos de 8 bits
    groups = [binary[i:i+8] for i in range(0, len(binary), 8)]
    # Convertir cada grupo a su carácter ASCII correspondiente
    text = ''
    for group in groups:
        text += chr(int(group, 2))
    return text

# Ejemplo de uso
binario = "01001000011011110110110001100001"
print(binary_to_ascii(binario))  # Salida: Hola