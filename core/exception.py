class NotFileException(Exception):
    def __init__(self, file:str):
        super().__init__("El archivo {} no existe".format(file))

class TypeFileException(Exception):
    def __init__(self, file:str):
        super().__init__("El tipo de archivo {} es el incorrecto".format(file))
        
class FormatTimeException(Exception):
    def __init__(self):
        super().__init__("Error en formato de horas ingresadas, corriga el formato e intente nuevamente")
        
class FormatFileException(Exception):
    def __init__(self):
        super().__init__("Error en estructura de archivo, intente con otro archivo")