def listaNumeros():
    numeros = input("Ingresa enteros separados por comas: ").split(",")
    suma = 0
    for numero in numeros:
        try:
            numero = int(numero.strip())
            suma += numero
        except:
            print("Error: caracter diferente de entero")
            return

    print(f"Numeros: {numeros}")
    print(f"Suma: {suma}")
    print(f"Media: {suma/len(numeros)}")

listaNumeros()
