archivo = open("ejercicios5/grande.txt", encoding="utf-8") #Me han dado problemas las tildes
contenido = archivo.readlines()
archivo.close()

for i in range(0, int(len(contenido)/100)):
    archivo = open("ejercicios5/division" + str(i) + ".txt", "w")
    archivo.writelines(contenido[i*100: (i+1)*100])
    archivo.close()

if len(contenido) % 100 != 0:
    archivo = open("ejercicios5/division" + str(int(len(contenido)/100)) +  ".txt", "w")
    archivo.writelines(contenido[int(len(contenido)/100) * 100:])
    archivo.close()