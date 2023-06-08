from Manejador_Facultades import Lista_Facultades
from Clase_Facultad import  Facultad
from Clase_Carrera import  Carrera
from Clase_Menu import Menu
def test():
    opc = int(input("desea probar el test 1 = datos correctos 2 = datos incorrectos 0 = salir\n"))
    while opc != 0:
        if opc == 1:
            facultades = Lista_Facultades()
            listafacu = facultades.getfacultades()
            facu = Facultad('1', 'Facultad de Ingenieria', ' Libertador General San Martin 1109 (O)', ' Capital', ' 0264-4222074 - 4222643')
            facu.setcarrera('1', ' Bioingenieria', ' Bioingeniero', ' Once Semestres', ' Grado')
            listafacu.append(facu)
            facu.mostrarfacu()
            cod = input("ingrese elcodigo de la facultad a buscar\n")
            facultades.mostrarfacultad(cod)
            nombre = input("ingres el nombre de una carrera a conocer sus datos\n")
            facultades.mostrarcarrera(nombre)
        if opc == 2:
            facultades = Lista_Facultades()
            listafacu = facultades.getfacultades()
            facu = Facultad(1234, 'Facultad de Ingenieria', ' Libertador General San Martin 1109 (O)', ' Capital',2641313121)
            facu.setcarrera('1', ' Bioingenieria', ' Bioingeniero', ' Once Semestres', ' Grado')
            listafacu.append(facu)
            facu.mostrarfacu()
            cod = input("ingrese elcodigo de la facultad a buscar\n")
            facultades.mostrarfacultad(cod)
            nombre = input("ingres el nombre de una carrera a conocer sus datos\n")
            facultades.mostrarcarrera(nombre)

        opc = int(input("desea probar el test 1 = datos correctos 2 = datos incorrectos 0 = salir\n"))

if __name__=='__main__':
    opc = input("desea probar los metodos con la funcion test y = si n = no\n")
    if opc == 'y':
        test()
    print("_______main________")
    Facu = Lista_Facultades()
    Facu.cargadatos()
    menu = Menu()
    menu.run(Facu)


