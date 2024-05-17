from foto import Foto
from error import DimensionError

# Inicializamos 'foto' con None para asegurarnos de que esté definida
foto = None

# Prueba 1: Intentamos crear una foto con un ancho demasiado grande
try:
    foto = Foto(3000, 2000, "vision.jpg")
except DimensionError as e:
    print(e)
    # Inicializamos 'foto' con valores válidos para continuar
    foto = Foto(1000, 1000, "vision.jpg")

# Prueba 2: Intentamos establecer un alto inválido (demasiado pequeño)
try:
    foto.alto = -1
except DimensionError as e:
    print(e)

# Prueba 3: Intentamos crear una foto con un alto demasiado grande
try:
    foto = Foto(1000, 3000, "vision.jpg")
except DimensionError as e:
    print(e)

# Prueba 4: Intentamos establecer un ancho inválido (demasiado pequeño)
try:
    foto.ancho = 0
except DimensionError as e:
    print(e)

# Prueba 5: Establecemos valores válidos para alto y ancho
try:
    foto.ancho = 1500
    foto.alto = 2000
    print(f"Ancho y alto establecidos correctamente: {foto.ancho}x{foto.alto}")
except DimensionError as e:
    print(e)
