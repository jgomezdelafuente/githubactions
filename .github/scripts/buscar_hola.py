import os
import sys

TEXTO_PROHIBIDO = "hola"
encontrado = False

for root, dirs, files in os.walk("."):
    # Ignorar carpetas típicas que no interesan
    dirs[:] = [d for d in dirs if d not in {".git", "__pycache__", ".github"}]

    for file in files:
        ruta = os.path.join(root, file)

        try:
            with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
                contenido = f.read()
                if TEXTO_PROHIBIDO in contenido:
                    print(f"El fichero {ruta} tiene el texto hola")
                    encontrado = True
        except Exception as e:
            # Si algún archivo no se puede leer, lo ignoramos
            pass

if encontrado:
    print("❌ Se encontró el texto 'hola'. No se puede aceptar la PR.")
    sys.exit(1)
else:
    print("✅ No se encontró el texto 'hola'.")

