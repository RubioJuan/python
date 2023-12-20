import os 
import menus as menu 
import alumnos as st 
alumnos={}
isActive =True 
opMenu = 0
while (isActive) : 
    os.system("cls")
    try: 
        opMenu =int(input(menu))
    except ValueError:
        print("Error en el dato de ingreso")
        os.system("pause")
    else:
        if(opMenu==1):
            rta== "s"
            while (rta in ["S", "s"]):
                os.system("cls")
                alumnos.update(st.regAlumno())
                print(alumnos) 
                rta = input("desea registar otro alumno S(si) N(no)").upper()
        elif(opMenu == 2):
            codAlumno = input("ingrese el codigo a buscar: ")
            st.buscarAlumnos(codAlumno,alumnos) 
        elif(opMenu== 4): 
            isActive = False