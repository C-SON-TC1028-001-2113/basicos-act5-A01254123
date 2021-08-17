import math
def main():
    #escribe tu código abajo de esta línea
    area = float(input("Area a pintar en metros: "))
    litroPorMetro = float(input("Rendimiento (m2/l): ")) 
    litrosNecesarios = math.ceil(area/litroPorMetro)
    print("Litros a comprar: " + str(litrosNecesarios))
if __name__ == '__main__':
    main()
