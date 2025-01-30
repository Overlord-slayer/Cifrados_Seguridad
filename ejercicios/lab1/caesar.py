desplazamiento = 3
abecedario ="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cesar(mensaje: str):
    lista = []
    for i in range(len(mensaje)):
        lista.append((mensaje.index(mensaje[i])+desplazamiento)%len(abecedario))
    print(lista)

mensaje = "Hola"
cesar(mensaje.lower())
