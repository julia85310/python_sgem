archivo1 = open("ejercicios5/archivo1.txt")
archivo2 = open("ejercicios5/archivo2.txt")

contenido1 = archivo1.readlines()
contenido2 = archivo2.readlines()

archivo1.close()
archivo2.close()


archivoCombinado = open("ejercicios5/combinado.txt", "w")
for i in range(0, min([len(contenido1), len(contenido2)])):
    archivoCombinado.write(contenido1[i])
    archivoCombinado.write(contenido2[i])
    
#Si sobran lineas las escribo al final
if(len(contenido1) > len(contenido2)):
    archivoCombinado.write("\n") #Lo último que se escribió no tenía salto de línea
    archivoCombinado.writelines(contenido1[len(contenido2):])
elif(len(contenido1) < len(contenido2)):
    archivoCombinado.write("\n")
    archivoCombinado.writelines(contenido2[len(contenido1):])

archivoCombinado.close()

