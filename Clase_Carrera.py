
class Carrera:
    __codigo = int
    __nombre = str
    __especialidad = str
    __duracion = int
    __titulo = str
    def __init__(self,codigo,nombre,especialidad,duracion,titulo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__duracion = duracion
        self.__titulo = titulo
    def getnom(self):
        return self.__nombre

    def getcodigo(self):
        return self.__codigo

    def gettitulo(self):
        return self.__titulo

    def getduracion(self):
        return self.__duracion
