import random
coches = [("Coche Rojo", 9), ("Coche Azul", 11), ("Coche Verde", 10)]
ganador = False
ronda = 1
distancias = [0, 0, 0]
while(not ganador):
    print(f"Ronda {ronda}:")
    for coche in range(0,3):
        distancia = random.uniform(0, 2)
        distancias[coche] = round(distancias[coche] + (distancia * coches[coche][1]), 2)
        print(f"\t{coches[coche][0]}: distancia recorrida total: {distancias[coche]}")
        if (distancias[coche] > 99):
            ganador = True
    if ganador:
        print(f"El ganador es el {coches[distancias.index(max(distancias))][0]}")
    ronda += 1

