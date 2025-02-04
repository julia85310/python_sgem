#Almacena la información en una lista de diccionarios.
with open("ejRepaso/datos-ventas.txt") as fichero:
    ventasTotales = [venta.split(", ") for venta in fichero.readlines()]
   
#Calcula el total de ventas por producto.
ventasProducto = {}
for venta in ventasTotales:
    producto = venta[0].split()[1]
    ventas = int(venta[1].split()[1])
    if producto in ventasProducto:
        ventasProducto[producto] = ventasProducto[producto] + ventas
    else:
        ventasProducto.update({producto: ventas})


#Escribe un informe con los resultados en un nuevo archivo de texto.
with open("ejRepaso/informe-ventas.txt", "w") as fichero:
    for producto, ventas in ventasProducto.items():
        fichero.write(f"Producto: {producto}, Total Vendido: {ventas}\n")
