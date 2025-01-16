suma = 0
numeros = 0
num = 0
while(num != -1):
   num = int(input('Dame numeros(- 1 para finalizar): '))
   if (num != -1):
      suma = suma + num
      numeros += 1
print(suma/numeros)