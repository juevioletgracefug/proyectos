"""
Una rosa para ti 🌹
--------------------
Pequeño programa de escritorio hecho con Tkinter.
Si alguien te envía este programa, es porque eres importante para esa persona.
"""

import os
import tkinter as tk
from tkinter import font as tkfont


IMAGEN_ROSA = "rosa.png"

BG = "#050709"        
FG_WHITE = "#f5f5f5"   
FG_PINK = "#ff8fa3"     
LINE_COLOR = "#8b1e2b"  
HEART_COLOR = "#ff3b5c"

root = tk.Tk()
root.title("Una rosa para ti 🌹")
root.configure(bg=BG)
root.resizable(True, True)

mono_font = tkfont.Font(family="Consolas", size=13)
mono_font_bold = tkfont.Font(family="Consolas", size=15, weight="bold")
emoji_font = tkfont.Font(family="Segoe UI Emoji", size=90)
small_emoji = tkfont.Font(family="Segoe UI Emoji", size=14)

container = tk.Frame(root, bg=BG)
container.pack(expand=True, fill="both", padx=30, pady=20)

tk.Label(
    container,
    text="Si alguien te envía este programa,\nes porque eres importante para esa persona.",
    font=mono_font,
    fg=FG_WHITE,
    bg=BG,
    justify="center",
).pack(pady=(10, 8))

sep_frame1 = tk.Frame(container, bg=BG)
sep_frame1.pack(fill="x", pady=(0, 10))
tk.Frame(sep_frame1, bg=LINE_COLOR, height=1).pack(side="left", expand=True, fill="x", padx=(0, 8))
tk.Label(sep_frame1, text="♥", font=small_emoji, fg=HEART_COLOR, bg=BG).pack(side="left")
tk.Frame(sep_frame1, bg=LINE_COLOR, height=1).pack(side="left", expand=True, fill="x", padx=(8, 0))

ruta_imagen = os.path.join(os.path.dirname(os.path.abspath(__file__)), IMAGEN_ROSA)

if os.path.exists(ruta_imagen):
    foto_rosa = tk.PhotoImage(file=ruta_imagen) 

    ancho_max = 260
    if foto_rosa.width() > ancho_max:
        factor = max(1, foto_rosa.width() // ancho_max)
        foto_rosa = foto_rosa.subsample(factor, factor)

    tk.Label(container, image=foto_rosa, bg=BG).pack(pady=10)
else:
    tk.Label(container, text="🌹", font=emoji_font, bg=BG).pack(pady=10)

tk.Label(
    container,
    text="Esta rosa nunca se marchitará.",
    font=mono_font_bold,
    fg=FG_PINK,
    bg=BG,
).pack(pady=(5, 8))

sep_frame2 = tk.Frame(container, bg=BG)
sep_frame2.pack(fill="x", pady=(0, 15))
tk.Frame(sep_frame2, bg=LINE_COLOR, height=1).pack(side="left", expand=True, fill="x", padx=(0, 8))
tk.Label(sep_frame2, text="❧♡❧", font=small_emoji, fg=HEART_COLOR, bg=BG).pack(side="left")
tk.Frame(sep_frame2, bg=LINE_COLOR, height=1).pack(side="left", expand=True, fill="x", padx=(8, 0))

para_frame = tk.Frame(container, bg=BG)
para_frame.pack(pady=(0, 20))
tk.Label(para_frame, text="Para:", font=mono_font_bold, fg=FG_PINK, bg=BG).pack(side="left", padx=(0, 10))
entry_para = tk.Entry(
    para_frame,
    font=mono_font_bold,
    fg=FG_WHITE,
    bg=BG,
    insertbackground=FG_WHITE,
    relief="flat",
    highlightthickness=0,
    bd=0,
    width=20,
    justify="center",
)
entry_para.pack(side="left")
entry_para.insert(0, "")

underline = tk.Frame(container, bg=LINE_COLOR, height=1)
underline.place(in_=para_frame, relx=0.0, rely=1.0, relwidth=1.0, y=2)

tk.Label(
    container,
    text="Gracias por existir. ❤",
    font=mono_font_bold,
    fg=FG_WHITE,
    bg=BG,
).pack(pady=(10, 0))

root.mainloop()