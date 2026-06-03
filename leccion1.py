#variables y tipos de datos
# una variable es como una caja con nombre donde guardas informacion.
nombre = "carlos"
edad = 19
altura = 1.75
#nombre es la caja y "carlos" es lo que guardas dentro

#Tipos de datos principales
# 1.string(texto): cualquier texto va entre comillas:
nombre = "carlos"
universidad = "UNI"
mensaje = "hola mundo"

# 2.integer(numero entero): numeros sin decimales
edad = 19
ciclo = 1
year = 2026

# 3.float(numero decimal): numeros con decimales
nota = 16.5
altura = 1.75
precio = 29.90

# 4.booleano(verdadero o falso): solo puede ser verdadero o falso
es_estudiante = True
tiene_trabajo = False

# Como ver el contenido de una variable: usas print() para mostrar el valor
nombre = "carlos"
edad = 19
print(nombre) #esto mostrara "carlos"
print(edad) #esto mostrara 19 

# print con mensaje
nombre = "eduardo"
edad = 17
universidad = "UTP"

print("Nombre:", nombre)
print("Edad:", edad)
print("Universidad:", universidad)

#F-strings — la forma profesional de mostrar variablesF-strings — la forma profesional de mostrar variables
# pones un f antes de las comillas y metes tus variables dentro de {}:
nombre = "eduardo"
edad = 17
universidad = "UTP"

print(f"Hola, me llamo {nombre} y tengo {edad} años")
print(f"Estudio en {universidad}")

# Comparacion-- las 3 formas de hacer print
nombre = "eduardo"
edad = 17

#forma basica
print("Nombre", nombre)

#con coma y variable
print("Tengo", edad, "años")

#F-string  la mas usada en la industria
print(f"Hola {nombre}, tienes {edad} años")

#tambien puedes hacer operaciones dentro del {}
edad = 17
ciclo = 1

print(f"En 4 años tendra {edad + 4}años")
print(f"Me falta {10 - ciclo} ciclos para terminar")

#f-strings con formato: puedes darle formato a los numeros dentro del {}
nota = 15
altura = 1.65

#mostrar float con solo 1 decimal
print(f"Mi altura es {altura:.1f} metros")

#mostrar promedio con 2 decimales
nota1 = 15
nota2 = 16
promedio = (nota1 + nota2) / 2
print(f"Mi promedio es {promedio:.2f}")
#el :.2f significa "muestrame este numero con 2 decimales"

#+   → suma
#-   → resta
#*   → multiplicación
#/   → división
#**  → potencia  (2**3 = 8)
#%   → módulo, el resto de una división  (10%3 = 1)
#//  → división entera  (10//3 = 3)


#Lecion 2 - Condicionales
#condicionales: le permites a tu codigo tomar decisiones segun una condicion. como en la vida real

#Estructura basica
#if condicion:
    #codigo si la condicion es True
#else:
    #codigo si la condicion es False    

#Los Operadores de compraracion
#>    # mayor que
#<    # menor que
#>=   # mayor o igual
#<=   # menor o igual
#==   # igual a (ojo: doble signo =)
#!=   # diferente a

#Ejemplo
edad = 17
print(edad > 18) #False
print(edad < 18) #True
print(edad == 17) #True
print(edad != 17) #false

#Cuando hay mas de 2 opciones -- elif
nota = 15

if nota >= 18:
    print("Excelente")
elif nota >= 14:
    print("Bien")
elif nota >= 11:
    print("aprobado")
else:
    print("reprobado")
# elif significa "si no se cumplio lo anterior, intenta esta condicion"

#Puedes combinar condiciones con (and) y (or)
#and → las DOS condiciones deben ser True
#if edad >= 18 and ciclo >= 4:
    #print("mayor de edad y en ciclos avanzados")

# or → al menos UNA condición debe ser True
#if nota >= 18 or ciclo == 1:
    #print("o sacaste buena nota o eres de primer ciclo")
                            
#Leccion 3 - Bucles
# es cuando le dices a tu codigo "repite esto varias veces". sin bucles tendrias que escribir varias veces lo mismo

#El bucle (for)
for i in range(5):
    print(i)
#range(5) genera los numeros del 0 al 4 - siempre empieza en 0 y el ultimo numero no se incluye

#se puede controlar el rango
#range(1, 6) # del 1 al 5
#range(1, 11)
#range(0, 10, 2) # del 0 al 9 de 2 en 2 (0,2,4,6,8)

#ejm
for i in range(1, 6):
   print(f"ciclo {i} de 5")
#ciclo 1 de 5
#ciclo 2 de 5
#ciclo 3 de 5
#ciclo 4 de 5
#ciclo 5 de 5

#bucle con listas
cursos = ["matematicas", "programacion", "fisica"]

for curso in cursos:
    print(f"tengo el curso de {curso}")

#Bucle while
# el (for) repite un numero fijo de veces, el (while) repite mientras una condicion sea True

#ejm
dinero = 100
while dinero > 0:
  dinero = dinero - 25
  print(f"gaste 25, me queda: {dinero}")


# Leccion 4 - Funciones
# Es un bloque de codigo con nombre que puedes reutilizar cuantas veces quieras. sin funciones tendrias que repetir el mismo codigo una y otra vez
#Sin función — código repetido 
print(f"Hola Eduardo, bienvenido")
print(f"Hola Carlos, bienvenido")
print(f"Hola María, bienvenido")
#Con función — código reutilizable
def saludar(nombre):
    print(f"Hola {nombre}, bienvenido")

saludar("Eduardo")
saludar("Carlos")
saludar("María")

#Estructura Basica
def nombre_funcion(parametros):
    #codigo de la funcion
#def = indica que estas creando una funncion
#nombre_funcion = el nombre que le das
#parametro = informacion que le pasas a la funcion
#la indentacion es obligatoria igual que en los bucles
#Funciones con y sin parámetros
#Sin parámetros
def saludar():
    print("Hola!")

saludar()  # la llamas así

#Con un parámetro
def saludar(nombre):
    print(f"Hola {nombre}!")

saludar("Eduardo")

#Con varios parámetros
def presentar(nombre, edad, universidad):
    print(f"Me llamo {nombre}, tengo {edad} años y estudio en {universidad}")

presentar("Eduardo", 17, "UTP")

#Funciones que devuelven un valor — return
#Hasta ahora las funciones solo imprimen. Pero también pueden devolver un resultado para usarlo después:
def calcular_promedio(nota1, nota2):
    promedio = (nota1 + nota2) / 2
    return promedio

resultado = calcular_promedio(16, 18)
print(f"tu promedio es {resultado:.2f}")

#print → solo muestra en pantalla
#return → devuelve el valor para usarlo en el código