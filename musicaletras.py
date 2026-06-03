import requests
import os

def buscar_letra(artista, cancion):
    url = f"https://api.lyrics.ovh/v1/{artista}/{cancion}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json().get("lyrics")
    return None

def traducir_letra(letra, artista, cancion, api_key):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    
    prompt = f"""Traduce al español la letra de "{cancion}" de {artista}.
Mantén el formato original (versos y coros separados).
Al final agrega 2-3 datos curiosos sobre la canción bajo el título CURIOSIDADES.

Letra:
{letra[:3000]}"""

    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    respuesta = requests.post(url, json=body)
    if respuesta.status_code == 200:
        data = respuesta.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"Error al traducir: {respuesta.status_code} - {respuesta.text}"

def main():
    api_key = input("Pega tu Gemini API Key: ").strip()

    print("\n🎵 BUSCADOR DE LETRAS\n")

    artista = input("Artista: ").strip()
    cancion = input("Canción: ").strip()

    print("\nBuscando letra...")
    letra = buscar_letra(artista, cancion)

    if not letra:
        print(f"❌ No se encontró '{cancion}' de {artista}. Verifica la ortografía.")
        return

    print("Traduciendo...\n")
    traduccion = traducir_letra(letra, artista, cancion, api_key)

    separador = "─" * 50

    print(separador)
    print(f"  {cancion.upper()} — {artista}")
    print(separador)

    print("\n📄 LETRA ORIGINAL:\n")
    print(letra.strip())

    print(f"\n{separador}")
    print("\n🇵🇪 TRADUCCIÓN AL ESPAÑOL:\n")
    print(traduccion.strip())
    print()

main()