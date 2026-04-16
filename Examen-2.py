def leer_edades(n):
    lista = []
    for i in range(n):
        edad = int(input("Edad: "))
        while edad < 1 or edad > 100:
            edad = int(input("Edad inválida, ingrese otra: "))
        lista.append(edad)
    return lista


def mayor(lista):
    return max(lista)


def menor(lista):
    return min(lista)


def promedio(lista):
    return sum(lista)/len(lista)


n = int(input("Cantidad de personas: "))

edades = leer_edades(n)

print("Mayor edad:", mayor(edades))
print("Menor edad:", menor(edades))
print("Promedio:", promedio(edades))