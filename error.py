class Error(Exception):
    """Clase base para excepciones"""
    pass

class DimensionError(Error):
    def __init__(self, mensaje: str, dimension: int = None, maximo: int = None) -> None:
        super().__init__(mensaje)  # Inicializa la clase base con el mensaje de error
        self.mensaje = mensaje  # Mensaje descriptivo del error
        self.dimension = dimension  # Dimensión que causó el error
        self.maximo = maximo  # Valor máximo permitido para la dimensión

    def __str__(self) -> str:
        if self.dimension is None and self.maximo is None:
            return super().__str__()  # Usa la representación por defecto
        else:
            ret = self.mensaje
            if self.dimension is not None:
                ret += f" Se ingresó dimensión {self.dimension}."
            if self.maximo is not None:
                ret += f" El valor máximo permitido es {self.maximo}."
            return ret
