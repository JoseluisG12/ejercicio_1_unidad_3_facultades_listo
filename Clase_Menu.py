from Manejador_Facultades import Lista_Facultades
class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {1:self.opc1,
                           2:self.opc2,

                        }
    def run(self,Manejador_F):
        band = True
        while band == True:
            b = int(input("""
    Menu Principal:
1-Ingresar codigo de facultad para conocer sus carreras y duracion de cada una
2-Ingresar nombre de una carrera y conocer su codigo(conformado por codigo de facultad y carrera),nombre y localidad donde se dicta

        0-salir\n"""))
            func = self.__switcher.get(b)
            if func:
                func(Manejador_F)
            else:
                band = False

    def opc1(self,Manejador_F):
        cod = input("ingrese elcodigo de la facultad a buscar\n")
        Manejador_F.mostrarfacultad(cod)

    def opc2(self,Manejador_F):
        nombre = input("ingres el nombre de una carrera a conocer sus datos\n")
        Manejador_F.mostrarcarrera(nombre)

