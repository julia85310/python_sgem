import json 
datos = '''{
    "Nuevo": "CreaNuevoDocumento()",
    "Abrir": "AbrirDocumento()",
    "Cerrar": "CerrarDocumento()"
    }'''
dicc = json.loads(datos)
dicc["Cerrar"] = "CloseDocumento()"
datos = json.dumps(dicc)
print(datos)