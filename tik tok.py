import time
import os

def escribir(texto, velocidad=0.04):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidad)
    print()

os.system("cls" if os.name == "nt" else "clear")

print("Iniciando...\n")

for barra, porcentaje in [
    ("█░░░░░░░░░", "10%"),
    ("███░░░░░░░", "30%"),
    ("██████░░░░", "60%"),
    ("██████████", "100%")
]:
    print(f"{barra} {porcentaje}")
    time.sleep(0.7)

time.sleep(1)
print("\nPreparando la sorpresa...")
time.sleep(2)

os.system("cls" if os.name == "nt" else "clear")

rosa = r"""
                    .-.
                 .-'   `-.
               .'  .-. .-.`.
              /   (   Y   ) \
             |     `-^-'     |
              \             /
               `.         .'
                 `-.___.-'
                     |
                   \ | /
                    \|/
                     |
                    / \
                   /___\

          🌹 Una rosa que nunca se marchita 🌹
"""

print(rosa)

escribir("Para: __________ ❤️\n")
time.sleep(1)

escribir("Quizá esta rosa no tenga aroma,")
escribir("pero nunca se marchitará.\n")

time.sleep(1)

escribir("Solo quería recordarte")
escribir("que eres una persona increíble.\n")

time.sleep(1)

escribir("Gracias por existir. 🌹")

input("\nPresiona ENTER para cerrar...")