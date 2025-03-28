from PIL import Image
import numpy as np

def xor_two_images(image1_path, image2_path, output_path):
    """
    Aplica la operación XOR entre dos imágenes.

    Args:
        image1_path (str): Ruta de la primera imagen (imagen original).
        image2_path (str): Ruta de la segunda imagen (imagen llave).
        output_path (str): Ruta donde se guardará la imagen resultante.

    Returns:
        None
    """
    # Cargar las imágenes y redimensionarlas al mismo tamaño
    img1 = Image.open(image1_path).convert("RGB")
    img2 = Image.open(image2_path).convert("RGB").resize(img1.size)

    # Convertir las imágenes a arreglos de numpy
    img1_array = np.array(img1)
    img2_array = np.array(img2)

    # Aplicar la operación XOR entre las dos imágenes
    xor_result = np.bitwise_xor(img1_array, img2_array)

    # Convertir el resultado de XOR a una imagen
    result_img = Image.fromarray(xor_result)

    # Guardar la imagen resultante
    result_img.save(output_path)
    print(f"La imagen XOR se ha guardado como '{output_path}'.")

    # Mostrar las imágenes utilizadas y el resultado
    img1.show(title="Imagen Original")
    img2.show(title="Imagen Llave")
    result_img.show(title="Imagen XOR Resultante")

# Rutas de las imágenes
image1_path = "argus.jpeg"
image2_path = "yin.jpeg"
output_path = "yin_y_argus.jpeg"

# Aplicar XOR entre las dos imágenes
xor_two_images(image1_path, image2_path, output_path)
