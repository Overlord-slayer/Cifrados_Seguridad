# 3. Investigar porque al aplicar XOR con una llave de texto la imagén se corrompe.
Cuando aplicas la operación XOR (⊕) a una imagen con una llave de texto, la imagen resultante puede parecer 
"corrupta" por varias razones técnicas. Aquí te explico los posibles problemas y cómo solucionarlos.

1. Diferencias en la longitud de la clave y los datos de la imagen

Si la clave de texto que usas para el XOR es más corta que los datos de la imagen, el patrón de cifrado se 
repetirá, lo que puede generar artefactos visuales en la imagen cifrada.

🔹 Solución:

    Usa una clave de longitud igual o mayor que la imagen.
    Usa una clave pseudoaleatoria basada en un generador de números aleatorios criptográficamente seguro.


# Referencias
https://chatgpt.com/share/67a55744-4930-8010-ad74-e6992af5c04d
