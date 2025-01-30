archivo = open('ejercicios5/numeros.txt')
numeros = [int(linea.strip()) for linea in archivo.readlines()]
archivo.close()
suma = 0
for numero in numeros:
    suma += numero

print(f"Suma: {suma}")
print(f"Máximo: {max(numeros)}")
print(f"Mínimo: {min(numeros)}")
print(f"Media: {suma/len(numeros)}")
