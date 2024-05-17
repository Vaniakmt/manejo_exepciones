from error import DimensionError
from PIL import Image

class Foto:
    MAX = 2500  # Dimensión máxima permitida para la foto

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = None
        self.__alto = None
        self.ruta = ruta
        self.image = Image.open(ruta)  # Abre la imagen usando PIL
        self.ancho = ancho  # Utiliza el setter para validar y asignar el ancho
        self.alto = alto  # Utiliza el setter para validar y asignar el alto

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho: int) -> None:
        # Verifica si el nuevo ancho supera el máximo permitido
        if ancho > Foto.MAX:
            raise DimensionError("Ancho no permitido.", ancho, Foto.MAX)
        # Verifica si el nuevo ancho es menor que 1
        elif ancho < 1:
            raise DimensionError("Ancho debe ser mayor a 0.", ancho)
        else:
            self.__ancho = ancho  # Asigna el nuevo valor al atributo privado
            self._resize_image()  # Redimensiona la imagen a los nuevos valores

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto: int) -> None:
        # Verifica si el nuevo alto supera el máximo permitido
        if alto > Foto.MAX:
            raise DimensionError("Alto no permitido.", alto, Foto.MAX)
        # Verifica si el nuevo alto es menor que 1
        elif alto < 1:
            raise DimensionError("Alto debe ser mayor a 0.", alto)
        else:
            self.__alto = alto  # Asigna el nuevo valor al atributo privado
            self._resize_image()  # Redimensiona la imagen a los nuevos valores

    def _resize_image(self):
        # Redimensiona la imagen a los nuevos valores de ancho y alto
        if self.__ancho and self.__alto:
            # Cambia el tamaño de la imagen utilizando los nuevos valores
            self.image = self.image.resize((self.__ancho, self.__alto))
            # Guarda la imagen redimensionada en la misma ruta
            self.image.save(self.ruta)
