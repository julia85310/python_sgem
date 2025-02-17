dictHexadecimalToDecimal = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F":15
}

dictHexadecimalToBinario = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

def hexadecimalToDecimal(hexadecimal):
    letras = list(str(hexadecimal))
    suma = 0
    indice = len(letras) - 1
    for letra in letras:
        suma = suma + caracterHexadecimalToNumber(letra) * (16 ** indice)
        indice -= 1
    return suma

def caracterHexadecimalToNumber(caracter):
    try:
        number = int(caracter)
        return number
    except Exception:
        return dictHexadecimalToDecimal[caracter]
    
def maxHexadecimalToDecimal(hexadecimales):
    numMaxDecimal = 0
    numMaxHexadecimal = 0
    for numHexadecimal in hexadecimales:
        numDecimal = hexadecimalToDecimal(numHexadecimal)
        if (numDecimal > numMaxDecimal):
            numMaxDecimal = numDecimal
            numMaxHexadecimal = numHexadecimal
    return (numMaxHexadecimal, numMaxDecimal)

def hexadecimalToBinario(hexadecimal):
    letras = list(str(hexadecimal))
    stringDecimal = ""
    for letra in letras:
        stringDecimal += dictHexadecimalToBinario[letra]
    return stringDecimal

def binarioADecimal(binario):
    numeros = list(binario)
    decimal = 0
    try:
        for indice in range(0, len(binario)):
            if (int(numeros[len(binario) - 1 - indice]) == 1):
                decimal = decimal + (2 ** indice)
        return decimal
    except Exception:
        print("Error: binario esperado")

def main():
    hexadecimales = ["1", "A", "2F", "B3", "FFA", "1111"]
    print(maxHexadecimalToDecimal(hexadecimales))
    print(hexadecimalToBinario(hexadecimales[3]))
    print(binarioADecimal("1010010"))

main()