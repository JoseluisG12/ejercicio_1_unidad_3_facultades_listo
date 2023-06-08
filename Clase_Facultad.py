from Clase_Carrera import Carrera
class Facultad:
    __codigo : int
    __nombre : str
    __direccion : str
    __localidad : str
    __telefono : int
    __carreras : list
    def __init__(self,codigo,nombre,direccion,localidad,telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carreras = []
    def setcarrera(self,codigo,nombre,inicio,duracion,titulo):
        una_carrera = Carrera(codigo,nombre,inicio,duracion,titulo)
        self.__carreras.append(una_carrera)

    def getnombre(self):
        return self.__nombre

    def getcodigo(self):
        return self.__codigo

    def getdireccion(self):
        return self.__direccion

    def getlocalidad(self):
        return self.__localidad

    def getcarrera(self):
        return self.__carreras

    def mostrarfacu(self):
        print("""
        Facultad {}
        codigo: {}
        direccion: {}
        locaclidad: {}""".format(self.__nombre, self.__codigo, self.__direccion, self.__localidad))
        for carrera in self.__carreras:
            print("""
        Carrera {}
        codigo: {}
        titulo: {}
        duracion:{}""".format(carrera.getnom(), carrera.getcodigo(), carrera.gettitulo(), carrera.getduracion()))



