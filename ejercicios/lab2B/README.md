# 3. Investigar porque al aplicar XOR con una llave de texto la imagén se corrompe.
Cuando aplicas la operación XOR (⊕) a una imagen con una llave de texto, la imagen resultante puede parecer 
"corrupta" por varias razones técnicas. Aquí te explico los posibles problemas y cómo solucionarlos.

### 1. Diferencias en la longitud de la clave y los datos de la imagen

Si la clave de texto que usas para el XOR es más corta que los datos de la imagen, el patrón de cifrado se 
repetirá, lo que puede generar artefactos visuales en la imagen cifrada.

🔹 Solución:

    Usa una clave de longitud igual o mayor que la imagen.
    Usa una clave pseudoaleatoria basada en un generador de números aleatorios criptográficamente seguro.

### 3. Investigar porque al aplicar XOR con una llave de texto la imagén se corrompe.
1. Desalineación de la llave con los datos de la imagen
La operación XOR es sensible al alineamiento entre los datos y la llave. Si la llave no tiene un patrón específico o su longitud no es adecuada, el resultado puede parecer aleatorio o "corrupto".
Por ejemplo, se puede dar el caso de tener una llave más corta que la imagen, aplicar la misma por repetición, los píxeles de la imagen resultante pueden no mostrar un patrón legible.

2. Cambios en la información de metadatos
Muchas imágenes tienen cabeceras o metadatos (por ejemplo, cabeceras PNG o JPEG) que contienen información importante sobre el formato de la imagen.
Si aplicar XOR indiscriminadamente a estos metadatos, es posible que el programa de visualización no pueda interpretar correctamente la imagen resultante. Lo mejor es aplicar XOR únicamente a los datos de píxeles, dejando la cabecera intacta.

3. Alteración de la paleta de colores
El aplicar XOR, altera los bits de cada canal de color (RGB). Esto puede resultar en combinaciones de color inesperadas o no deseadas, haciendo que la imagen se vea distorsionada.
Algunos patrones de llaves pueden causar que los colores se inviertan o se distorsionen de forma no uniforme.

4. Efecto de Padding y relleno
Si la longitud de los datos no es un múltiplo exacto de la longitud de la llave, el patrón de XOR puede repetirse de forma desalineada, produciendo efectos visuales inesperados.

5. No revertir correctamente el proceso
El no aplicar la misma llave exactamente para revertir el proceso XOR, los datos de la imagen no se restaurarán a su estado original.
Propiedad del XOR: Si aplicas A XOR B XOR B, el resultado vuelve a ser A. Por lo tanto, usar la misma llave es esencial para recuperar la imagen original.

# Inciso 3
![image](https://github.com/user-attachments/assets/2d7d7915-68ca-4fbf-a184-079b33105d79)

# Inciso 4
![image](https://github.com/user-attachments/assets/00c273fa-487a-4105-90d6-f83e5f015847)

### Referencias
https://chatgpt.com/share/67a55744-4930-8010-ad74-e6992af5c04d
https://chatgpt.com/share/67ac1a00-3eb0-8010-93ea-76f1fbc6e22f
