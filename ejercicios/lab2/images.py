from PIL import Image
import numpy as np

# Cargar imagen
imagen = Image.open("imagen.png").convert("L")  # Convertir a escala de grises
matriz_bits = np.array(imagen)

# Mostrar la matriz de bits de la imagen
print(matriz_bits)
