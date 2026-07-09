nombre = input("¿Cómo te llamas? ")

print("Hola", nombre)

while True:
    mensaje = input("Tú: ").lower()

    if mensaje == "quien soy":
        print("IA: Tu nombre es", nombre)

    elif mensaje == "adios":
        print("IA: Hasta luego", nombre)
        break

    else:
        print("IA: No entiendo eso todavía")