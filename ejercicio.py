def saludar (nombre):
    print(f"Hola {nombre}, bienvenido a Python!")
saludar("Eduardo")

def calcular_promedio(nota_1, nota_2, nota_3):
    promedio = (nota_1 + nota_2 + nota_3) / 3
    return promedio
resultado = calcular_promedio(17, 18, 19)
print(f"Tu promedio es {resultado:.2f}")

def es_aprobado(promedio):
    return promedio >= 11

if es_aprobado(resultado):
    print("¡Felicidades! Has aprobado.")
else:
    print("No has aprobado.")