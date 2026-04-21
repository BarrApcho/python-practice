# funcion para calcular puntaje de puntualidad
def puntaje_puntualidad(minutos):

    if minutos == 0:
        return 10
    elif minutos <= 2:
        return 8
    elif minutos <= 5:
        return 6
    elif minutos <= 9:
        return 4
    else:
        return 2


# funcion para calcular puntaje de rendimiento
def puntaje_rendimiento(obs):

    if obs == 0:
        return 10
    elif obs == 1:
        return 8
    elif obs == 2:
        return 6
    elif obs == 3:
        return 4
    else:
        return 2


# funcion para calcular bonificacion
def calcular_bono(total):

    if total >= 18:
        return 500
    elif total >= 15:
        return 300
    elif total >= 12:
        return 200
    else:
        return 100


# programa principal
minutos = int(input("Minutos de tardanza: "))
obs = int(input("Número de observaciones: "))

p_puntualidad = puntaje_puntualidad(minutos)
p_rendimiento = puntaje_rendimiento(obs)

total = p_puntualidad + p_rendimiento

bono = calcular_bono(total)

print("Puntaje puntualidad:", p_puntualidad)
print("Puntaje rendimiento:", p_rendimiento)
print("Puntaje total:", total)
print("Bonificación:", bono)