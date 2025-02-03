import json
fichero = open("ejercicios6/empleados.json")
empleados = json.load(fichero)
fichero.close()
deps = []
for empleado in empleados:
    departamento = empleado["departamento"]
    salario = empleado["salario"]
    existe = False
    for dep in deps:
        if(dep["departamento"] == departamento):
            existe = True
            dep["empleados"] = dep["empleados"] + 1
            dep["totalSalarios"] = dep["totalSalarios"] + salario
            break
    if (not existe):
        deps.append({"departamento": departamento, "empleados": 1, "totalSalarios": salario})

mediaDeps = {}
for dep in deps:
    mediaDeps.update({dep["departamento"]:dep["totalSalarios"]/dep["empleados"]})
fichero = open("ejercicios6/resumen_departamentos.json", "w")
json.dump(mediaDeps, fichero)
fichero.close()
    
    