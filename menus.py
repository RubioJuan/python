import os 
import notas as nota
menu = "1. Registrar Alumno\n2. Registrar Notas\n3. Buscar estudiante\n4. Salir)"
subMenuNotas = "1.Parciales\n2.Quices\n3. Trabajos\n4.Regresar al menu principal"
hasError = True 
def menuPrincipal()-> int:
    global hasError
    hasError = True  
    print(menu)
    while (hasError ==True):
        try:
          menu.hasError = False 
          return int(input(":)"))
        except ValueError:
           menu.hasError = True 
def menuNotas(alumnos : dict):
    os.system('cls')
        
    isActiveMenu = True 
    while (isActiveMenu):
        os.system("cls")
        try:
            print(subMenuNotas)
            opMenu = int(input(":)")) 
        except ValueError:
            print("Opcion invalida...Recuerda que son enteros")
        else:
            if (opMenu == 1):
                nota.addGrade(alumnos,"parciales")  
            elif (opMenu == 2):
                nota.addGrade(alumnos,"quices")
            elif (opMenu == 3):
                nota.addGrade(alumnos,"trabajos")
            elif (opMenu == 4):
                isActiveMenu = False
            else:
                print("La opcion ingresada es invalida....")
                os.system('pause')         


             
              