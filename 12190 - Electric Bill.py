'''
Tarea 1: Electric Bill
Juan Pablo Ovalles Ceron
8971870
'''

from sys import stdin

def main():
    line = list(map(int, stdin.readline().split()))
    while line != [0,0]:
        A, B = line
        myWatts = bisection(A, B)
        print(convertCosto(myWatts))
        line = list(map(int, stdin.readline().split()))

def convertWatts(precio):
    rangos = [(100, 2),(9900, 3),(990000, 5),(float('inf'), 7)]
    consumo = 0
    for limite, tarifa in rangos:
        if precio > limite * tarifa:
            precio -= limite * tarifa
            consumo += limite
        else:
            consumo += precio / tarifa
            break

    return int(consumo)

def convertCosto(consumo):
    rangos = [(100, 2), (9900, 3),(990000, 5),(float('inf'), 7)]

    costo = 0
    for limite, tarifa in rangos:
        if consumo > limite:
            costo += limite * tarifa
            consumo -= limite
        else:
            costo += consumo * tarifa
            break

    return int(costo)

def bisection(A, B):
    y = convertWatts(A)
    lo = 0
    hi = y//2   # El maximo consumo va a ser la mitad, puesto que se sabe que no consume mas que el vecino
    mid = (hi+lo)//2
    wattsVecino = -1
    while wattsVecino+mid != y:
        mid = (hi+lo)//2
        precioOpcion = convertCosto(mid)
        costoVecino = precioOpcion+B
        wattsVecino = convertWatts(costoVecino)
        if wattsVecino+mid > y: hi = mid
        else: lo = mid
    return lo

main()
