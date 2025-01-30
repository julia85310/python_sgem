archivo = open("ejercicios5/servidor.log")
contenido = archivo.readlines()
archivo.close()

countIPs = {}
lineasError = []

for linea in contenido:
    valores = linea.split()
    
    evento = valores[3]
    if(evento == "ERROR:"):
        lineasError.append(linea)
        
    direccionIP = valores[2]
    countIPs[direccionIP] = countIPs.get(direccionIP, 0) + 1

print(countIPs)
archivo = open("ejercicios5/errores.log", "w")
archivo.writelines(lineasError)
archivo.close()
    


