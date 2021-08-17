import math
def main():
    #escribe tu código abajo de esta línea
    alturaCasa = int(input("Altura de la casa: "))
    angulo = int(input("Angulo en grados: "))
    largoescalera = round(alturaCasa/ math.sin(math.radians(angulo)))
    print("Largo de la escalera: " + str(largoescalera))
if __name__ == '__main__':
    main()
