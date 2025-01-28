def xor_binary(binary1, binary2):
    # Asegurarse de que ambos binarios tengan la misma longitud
    if len(binary1) != len(binary2):
        raise ValueError("Los binarios deben tener la misma longitud")
    # Aplicar XOR bit a bit
    result = ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(binary1, binary2))
    return result

# Ejemplo de uso
binario1 = "10101010"
binario2 = "11001100"
print(xor_binary(binario1, binario2))  # Salida: 01100110