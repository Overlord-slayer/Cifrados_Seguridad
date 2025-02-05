def bits_to_text(bits):
    return ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))

# Ejemplo
print(bits_to_text("0100100001101001"))  # Salida esperada: 'Hi'
