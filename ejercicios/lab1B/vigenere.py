"""
En este caso, se toma en cuenta que es mediante una matriz, no se hace como matriz
pero como una sopa de palabras, se tiene una tabla de la a-z, vertical y horizontalmente
ejemplo
abcdefg
bcdefgh
cdefghi
defghij
efghijk
fghijkl
ghijklm

donde las columnas son la entrada de texto plano. Las filas, la entrada clave

@see https://youtu.be/SkJcmCaHqS0?si=m9n2Tn5-DfrGV1u3
@see https://youtu.be/XT6zIHXhFO4?si=DbbSzhVA_12lCAXp
"""
import string

# Leer el contenido del archivo vigenere.txt
with open("./Cifrados/vigenere.txt", "r", encoding="utf-8") as file:
    ciphertext = file.read().strip().lower()

# Alfabeto español
ALPHABET = "abcdefghijklmn\u00f1opqrstuvwxyz"
MODULO = len(ALPHABET)

# Frecuencia de letras en español (en porcentaje)
SPANISH_FREQ = {
    'a': 11.525, 'b': 2.215, 'c': 4.019, 'd': 5.010, 'e': 12.181, 'f': 0.692,
    'g': 1.768, 'h': 0.703, 'i': 6.247, 'j': 0.493, 'k': 0.011, 'l': 4.967,
    'm': 3.157, 'n': 6.712, '\u00f1': 0.311, 'o': 8.683, 'p': 2.510, 'q': 0.877,
    'r': 6.871, 's': 7.977, 't': 4.632, 'u': 2.927, 'v': 1.138, 'w': 0.017,
    'x': 0.215, 'y': 1.008, 'z': 0.467
}

# Bigrama y trigramas frecuentes en español
COMMON_BIGRAMS = ["de", "la", "el", "en", "es", "un", "se", "al", "lo", "le"]
COMMON_TRIGRAMS = ["que", "los", "del", "las", "por", "con", "una", "sus", "mas"]

def decrypt_vigenere(text, key):
    """
    Descifra un texto cifrado con el cifrado de Vigenère.
    
    :param text: Texto cifrado.
    :param key: Clave utilizada para el descifrado.
    :return: Texto descifrado o None si la clave contiene caracteres no válidos.
    """
    key = key.lower()
    if not all(k in ALPHABET for k in key):
        return None  
    
    key_indices = [ALPHABET.index(k) for k in key]
    key_length = len(key)
    decrypted_text = ""
    
    for i, c in enumerate(text):
        if c in ALPHABET:
            idx = (ALPHABET.index(c) - key_indices[i % key_length]) % MODULO
            decrypted_text += ALPHABET[idx]
        else:
            decrypted_text += c
    
    return decrypted_text

def frequency_score(text):
    """
    Calcula la puntuación de frecuencia de un texto comparándolo con la distribución esperada en español.
    
    :param text: Texto a analizar.
    :return: Puntuación de frecuencia basada en la desviación de la distribución esperada.
    """
    text_freq = {}
    total_chars = 0
    
    for char in text:
        if char in SPANISH_FREQ:
            text_freq[char] = text_freq.get(char, 0) + 1
            total_chars += 1
    
    score = 0
    for char, count in text_freq.items():
        observed_freq = (count / total_chars) * 100
        expected_freq = SPANISH_FREQ.get(char, 0)
        score += abs(observed_freq - expected_freq)
    
    return score

def bigram_trigram_score(text):
    """
    Calcula la puntuación basada en la cantidad de bigramas y trigramas comunes en español dentro del texto.
    
    :param text: Texto a analizar.
    :return: Suma de ocurrencias de bigramas y trigramas comunes.
    """
    bigram_count = sum(text.count(bigram) for bigram in COMMON_BIGRAMS)
    trigram_count = sum(text.count(trigram) for trigram in COMMON_TRIGRAMS)
    return bigram_count + trigram_count

def generate_keys(prefix, length):
    """
    Genera todas las posibles claves con un prefijo dado y una longitud específica.
    
    :param prefix: Prefijo fijo para las claves generadas.
    :param length: Longitud total de las claves generadas.
    :return: Lista de claves generadas.
    """
    keys = []
    
    def generate_recursive(current_key):
        if len(current_key) == length:
            keys.append(current_key)
            return
        for letter in ALPHABET:
            generate_recursive(current_key + letter)
    
    generate_recursive(prefix)
    return keys

def brute_force_attack(ciphertext, prefix, length, top_n=10):
    """
    Realiza un ataque de fuerza bruta sobre un cifrado Vigenère, probando claves con un prefijo específico.
    
    :param ciphertext: Texto cifrado.
    :param prefix: Prefijo para las claves generadas.
    :param length: Longitud total de las claves generadas.
    :param top_n: Número de mejores resultados a devolver.
    :return: Lista de las mejores claves y sus textos descifrados.
    """
    possible_keys = generate_keys(prefix, length)
    results = []
    
    for key in possible_keys:
        decrypted = decrypt_vigenere(ciphertext, key)
        if decrypted:
            freq_score = frequency_score(decrypted)
            struct_score = bigram_trigram_score(decrypted)
            results.append((key, decrypted, freq_score, struct_score))
    
    results.sort(key=lambda x: (-x[3], x[2]))
    return results[:top_n]

PREFIX = "pa"
KEY_LENGTH = 6
TOP_RESULTS = 10

top_keys = brute_force_attack(ciphertext, PREFIX, KEY_LENGTH, TOP_RESULTS)

print(f"\nTop {TOP_RESULTS} mejores claves encontradas:")
for i, (key, text, freq_score, struct_score) in enumerate(top_keys, start=1):
    print(f"\n {i}. Clave: {key}")
    print(f"Puntuación de estructuras comunes en español: {struct_score}")
    print(f"Métrica de similitud: {freq_score:.3f}")
    print(f"Texto descifrado:\n{text[:300]}...\n")

best_key, best_text, best_freq_score, best_struct_score = top_keys[0]
print(f"\nMejor clave según estructura en español: {best_key}")
print(f"Puntuación de estructuras comunes en español: {best_struct_score}")
print(f"Métrica de similitud: {best_freq_score:.3f}")
print(f"Texto descifrado:\n{best_text[:300]}...\n")
