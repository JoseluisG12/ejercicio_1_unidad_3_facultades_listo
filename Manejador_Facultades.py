import csv
from Clase_Facultad import Facultad
class Lista_Facultades:
    __Facultades : list

    def __init__(self):
        self.__Facultades = []

    def getfacultades(self):
        return self.__Facultades
    def cargadatos(self):
        archivo = open('facultades.csv')
        reader = csv.reader(archivo, delimiter=(','))
        cod = '0'
        for fila in reader:
            if cod != fila[0]:
                codigo = fila[0]
                nombre = fila[1]
                direccion = fila[2]
                localidad = fila[3]
                telefono = fila[4]
                facu = Facultad(codigo,nombre,direccion,localidad,telefono)
                self.__Facultades.append(facu)
                cod = fila[0]
            else:
                codigo = fila[1]
                nombre = fila[2]
                especialidad = fila[3]
                duracion = fila[4]
                titulo = fila[5]
                self.__Facultades[int(cod)-1].setcarrera(codigo,nombre,especialidad,duracion,titulo)
                cod = fila[0]

    def mostrardatos(self):
        for facu in self.__Facultades:
            print("""
                    Facultad {}
                    codigo: {}
                    direccion: {}
                    locaclidad: {}""".format(facu.getnombre(),facu.getcodigo(), facu.getdireccion(), facu.getlocalidad()))
            for carrera in facu.getcarrera():
                print("""
            Carrera {}
            codigo: {}
            titulo: {}
            duracion:{}""".format(carrera.getnom(), carrera.getcodigo(), carrera.gettitulo(), carrera.getduracion()))

    def mostrarfacultad(self,cod):
        band = True
        i = 0
        while band and i < len(self.__Facultades):
            if self.__Facultades[i].getcodigo() == cod:
                band = False
            else:
                i = i + 1
        if band:
            print(" Error no se encontro la facultad")
        else:
            print("""
                    Facultad {}
                    """.format(self.__Facultades[i].getnombre()))
            for carrera in self.__Facultades[i].getcarrera():
                print("""
            Carrera {}
            duracion:{}""".format(carrera.getnom(), carrera.getduracion()))

    def mostrarcarrera(self,nombre):
        band = True
        i = 0
        b = 0
        while band  and i < len(self.__Facultades):
            carreras = self.__Facultades[i].getcarrera()

            while band  and b < len(carreras):
                if carreras[b].getnom() == nombre:
                    band = False
                else:
                    b = b + 1
            if band:
                i = i + 1
                b = 0
        if band == True:
            print("Error no se encontro la carrera")
        else:
            print(self.__Facultades[i].getcodigo())
            print("""
Codigo: {}-{}
Nombre:{}
Localidad:{}""".format(self.__Facultades[i].getcodigo(),carreras[b].getcodigo(),carreras[b].getnom(),self.__Facultades[i].getlocalidad()))














