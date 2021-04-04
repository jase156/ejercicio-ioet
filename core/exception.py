class NotFileException(Exception):
    def __init__(self, file):
        super().__init__("El archivo {} no existe".format(file))

class TypeFileException(Exception):
    def __init__(self, file):
        super().__init__("El archivo {} no existe".format(file))