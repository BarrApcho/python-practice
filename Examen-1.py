# funcion para obtener precio
def obtener_precio(tipo):

    if tipo == 1:
        return 2.15
    elif tipo == 2:
        return 3.15
    elif tipo == 3:
        return 4.10
    elif tipo == 4:
        return 3.90


# funcion para calcular descuento
def calcular_descuento(compra, cantidad):

    if cantidad <= 4:
        return compra * 0.03
    elif cantidad <= 8:
        return compra * 0.05
    elif cantidad <= 12:
        return compra * 0.07
    else:
        return compra * 0.09


ventas = []
seguir = "s"

while seguir == "s":

    print("1. Piqueo Snack")
    print("2. Mexi Nachos")
    print("3. Chifles Sabor Norteño")
    print("4. Chizitos Fiesta")

    tipo = int(input("Tipo de golosina: "))
    cantidad = int(input("Cantidad de bolsas: "))

    precio = obtener_precio(tipo)

    compra = precio * cantidad

    descuento = calcular_descuento(compra, cantidad)

    pagar = compra - descuento

    print("Importe compra:", compra)
    print("Descuento:", descuento)
    print("Total a pagar:", pagar)

    ventas.append(pagar)

    seguir = input("Otra venta? (s/n): ")

print("Venta promedio:", sum(ventas)/len(ventas))
print("Venta maxima:", max(ventas))
print("Venta minima:", min(ventas))