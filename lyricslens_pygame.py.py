import pygame
import requests
import threading
import sys
import time

# ── Configuración ──────────────────────────────────────────────
ANCHO, ALTO = 700, 600
FPS = 60
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (150, 150, 150)
DORADO = (200, 170, 100)
GRIS_OSCURO = (40, 40, 40)

GEMINI_API_KEY = ""  # Se pide al inicio

# ── API ────────────────────────────────────────────────────────
def buscar_letra(artista, cancion):
    try:
        url = f"https://api.lyrics.ovh/v1/{artista}/{cancion}"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return r.json().get("lyrics", "").strip()
    except:
        pass
    return None

def traducir_letra(letra, artista, cancion, api_key):
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
        prompt = f"""Traduce al español la letra de "{cancion}" de {artista}.
Mantén el formato original con saltos de línea entre versos.
Solo devuelve la traducción, sin explicaciones ni títulos extra.

Letra:
{letra[:2500]}"""
        body = {"contents": [{"parts": [{"text": prompt}]}]}
        r = requests.post(url, json=body, timeout=30)
        if r.status_code == 200:
            return r.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    except:
        pass
    return None

# ── Input de texto ─────────────────────────────────────────────
class InputBox:
    def __init__(self, x, y, w, placeholder="", password=False):
        self.rect = pygame.Rect(x, y, w, 36)
        self.text = ""
        self.placeholder = placeholder
        self.activo = False
        self.password = password

    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            self.activo = self.rect.collidepoint(evento.pos)
        if evento.type == pygame.KEYDOWN and self.activo:
            if evento.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif evento.key not in (pygame.K_RETURN, pygame.K_TAB):
                self.text += evento.unicode

    def dibujar(self, surface, fuente):
        color_borde = DORADO if self.activo else GRIS_OSCURO
        pygame.draw.rect(surface, GRIS_OSCURO, self.rect, border_radius=4)
        pygame.draw.rect(surface, color_borde, self.rect, 1, border_radius=4)
        mostrar = "*" * len(self.text) if self.password else self.text
        if mostrar:
            txt = fuente.render(mostrar, True, BLANCO)
        else:
            txt = fuente.render(self.placeholder, True, (70, 70, 70))
        surface.blit(txt, (self.rect.x + 10, self.rect.y + 8))

# ── Pantalla de búsqueda ───────────────────────────────────────
def pantalla_busqueda(screen, clock, fuente, fuente_small, fuente_titulo):
    input_key   = InputBox(200, 160, 300, "AIza...", password=True)
    input_art   = InputBox(200, 240, 300, "ej. Shakira")
    input_can   = InputBox(200, 310, 300, "ej. Waka Waka")
    inputs = [input_key, input_art, input_can]
    labels = ["API Key", "Artista", "Canción"]
    mensaje = ""
    buscando = False
    resultado = [None]

    def hacer_busqueda():
        nonlocal mensaje, buscando
        letra = buscar_letra(input_art.text.strip(), input_can.text.strip())
        if not letra:
            mensaje = "❌ No se encontró la canción"
            buscando = False
            return
        mensaje = "Traduciendo..."
        trad = traducir_letra(letra, input_art.text.strip(), input_can.text.strip(), input_key.text.strip())
        if not trad:
            mensaje = "❌ Error al traducir"
            buscando = False
            return
        resultado[0] = (letra, trad, input_art.text.strip(), input_can.text.strip())
        buscando = False

    while True:
        clock.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            for inp in inputs:
                inp.manejar_evento(evento)
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                if not buscando and input_key.text and input_art.text and input_can.text:
                    buscando = True
                    mensaje = "Buscando letra..."
                    threading.Thread(target=hacer_busqueda, daemon=True).start()

        if resultado[0]:
            return resultado[0]

        screen.fill(NEGRO)

        # Título
        t = fuente_titulo.render("🎵 LyricLens", True, DORADO)
        screen.blit(t, (ANCHO // 2 - t.get_width() // 2, 60))
        sub = fuente_small.render("letra + traducción al español", True, GRIS)
        screen.blit(sub, (ANCHO // 2 - sub.get_width() // 2, 105))

        # Labels e inputs
        for i, (label, inp) in enumerate(zip(labels, inputs)):
            lbl = fuente_small.render(label, True, GRIS)
            screen.blit(lbl, (110, inp.rect.y + 9))
            inp.dibujar(screen, fuente_small)

        # Botón / estado
        if buscando:
            dots = "." * (int(time.time() * 2) % 4)
            msg = fuente_small.render(mensaje + dots, True, DORADO)
            screen.blit(msg, (ANCHO // 2 - msg.get_width() // 2, 380))
        else:
            hint = fuente_small.render("↵ Enter para buscar", True, GRIS_OSCURO)
            screen.blit(hint, (ANCHO // 2 - hint.get_width() // 2, 380))
            if mensaje:
                err = fuente_small.render(mensaje, True, (200, 80, 80))
                screen.blit(err, (ANCHO // 2 - err.get_width() // 2, 410))

        pygame.display.flip()

# ── Pantalla de letra animada ──────────────────────────────────
def pantalla_letra(screen, clock, fuente, fuente_small, fuente_titulo, letra, traduccion, artista, cancion):
    modos = [("ORIGINAL", letra), ("TRADUCCIÓN", traduccion)]
    modo_idx = 0

    def preparar_lineas(texto, fuente, max_ancho):
        lineas = []
        for parrafo in texto.split("\n"):
            if not parrafo.strip():
                lineas.append("")
                continue
            palabras = parrafo.split()
            linea_actual = ""
            for palabra in palabras:
                prueba = linea_actual + (" " if linea_actual else "") + palabra
                if fuente.size(prueba)[0] <= max_ancho:
                    linea_actual = prueba
                else:
                    if linea_actual:
                        lineas.append(linea_actual)
                    linea_actual = palabra
            if linea_actual:
                lineas.append(linea_actual)
        return lineas

    def iniciar_modo(idx):
        titulo_modo, texto = modos[idx]
        lineas = preparar_lineas(texto, fuente_small, ANCHO - 100)
        return {
            "lineas": lineas,
            "titulo": titulo_modo,
            "char_idx": 0,       # índice global de caracteres
            "total_chars": sum(len(l) + 1 for l in lineas),
            "scroll": 0,
            "ultimo_char": 0,
            "velocidad": 18,     # chars por segundo
        }

    estado = iniciar_modo(modo_idx)
    ALTO_LINEA = 26
    MARGEN = 50
    AREA_Y = 130
    AREA_ALTO = ALTO - AREA_Y - 60

    while True:
        dt = clock.tick(FPS) / 1000
        lineas = estado["lineas"]

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return  # volver a búsqueda
                if evento.key == pygame.K_TAB:
                    modo_idx = (modo_idx + 1) % 2
                    estado = iniciar_modo(modo_idx)
                if evento.key == pygame.K_DOWN:
                    estado["scroll"] = min(estado["scroll"] + 30,
                        max(0, len(lineas) * ALTO_LINEA - AREA_ALTO))
                if evento.key == pygame.K_UP:
                    estado["scroll"] = max(0, estado["scroll"] - 30)
            if evento.type == pygame.MOUSEWHEEL:
                estado["scroll"] = max(0, min(
                    estado["scroll"] - evento.y * 20,
                    max(0, len(lineas) * ALTO_LINEA - AREA_ALTO)))

        # Avanzar animación
        estado["ultimo_char"] += estado["velocidad"] * dt
        estado["char_idx"] = min(int(estado["ultimo_char"]), estado["total_chars"])

        # Auto-scroll siguiendo el texto
        chars_vistos = 0
        linea_actual_idx = 0
        for i, l in enumerate(lineas):
            chars_vistos += len(l) + 1
            if chars_vistos >= estado["char_idx"]:
                linea_actual_idx = i
                break
        y_actual = linea_actual_idx * ALTO_LINEA
        if y_actual - estado["scroll"] > AREA_ALTO - ALTO_LINEA * 3:
            estado["scroll"] = y_actual - AREA_ALTO + ALTO_LINEA * 3

        # ── Dibujo ──
        screen.fill(NEGRO)

        # Cabecera
        t_cancion = fuente_titulo.render(cancion, True, BLANCO)
        screen.blit(t_cancion, (ANCHO // 2 - t_cancion.get_width() // 2, 18))
        t_artista = fuente_small.render(artista, True, DORADO)
        screen.blit(t_artista, (ANCHO // 2 - t_artista.get_width() // 2, 58))

        # Tab activo
        for i, (nombre, _) in enumerate(modos):
            color = DORADO if i == modo_idx else GRIS_OSCURO
            txt = fuente_small.render(nombre, True, color)
            x = 160 + i * 200
            screen.blit(txt, (x, 88))
            if i == modo_idx:
                pygame.draw.line(screen, DORADO, (x, 108), (x + txt.get_width(), 108), 1)

        hint = fuente_small.render("TAB cambia vista  ·  ↑↓ scroll  ·  ESC volver", True, (45, 45, 45))
        screen.blit(hint, (ANCHO // 2 - hint.get_width() // 2, 88))

        # Área de letra con clip
        area_rect = pygame.Rect(MARGEN, AREA_Y, ANCHO - MARGEN * 2, AREA_ALTO)
        screen.set_clip(area_rect)

        chars_mostrados = 0
        for i, linea in enumerate(lineas):
            y = AREA_Y + i * ALTO_LINEA - estado["scroll"]
            if y + ALTO_LINEA < AREA_Y or y > AREA_Y + AREA_ALTO:
                chars_mostrados += len(linea) + 1
                continue
            chars_en_linea = max(0, min(len(linea), estado["char_idx"] - chars_mostrados))
            if chars_en_linea > 0:
                fragmento = linea[:chars_en_linea]
                surf = fuente_small.render(fragmento, True, BLANCO)
                screen.blit(surf, (MARGEN, y))
                # cursor parpadeante
                if chars_mostrados + chars_en_linea == estado["char_idx"] and int(time.time() * 2) % 2:
                    cx = MARGEN + fuente_small.size(fragmento)[0]
                    pygame.draw.rect(screen, DORADO, (cx, y + 2, 2, 20))
            chars_mostrados += len(linea) + 1

        screen.set_clip(None)

        # Línea separadora cabecera
        pygame.draw.line(screen, GRIS_OSCURO, (MARGEN, AREA_Y - 8), (ANCHO - MARGEN, AREA_Y - 8), 1)

        pygame.display.flip()

# ── Main ───────────────────────────────────────────────────────
def main():
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("LyricLens")
    clock = pygame.time.Clock()

    fuente_titulo = pygame.font.SysFont("Georgia", 28, bold=True)
    fuente        = pygame.font.SysFont("Georgia", 18)
    fuente_small  = pygame.font.SysFont("Consolas", 16)

    while True:
        resultado = pantalla_busqueda(screen, clock, fuente, fuente_small, fuente_titulo)
        if resultado:
            letra, trad, artista, cancion = resultado
            pantalla_letra(screen, clock, fuente, fuente_small, fuente_titulo, letra, trad, artista, cancion)

main()