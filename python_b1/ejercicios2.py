fibonnacci = [0, 1]
while(len(fibonnacci) < 10):
   num1 = fibonnacci[len(fibonnacci) - 1]
   num2 = fibonnacci[len(fibonnacci) - 2]
   fibonnacci.append(num1 + num2) 
print(fibonnacci)