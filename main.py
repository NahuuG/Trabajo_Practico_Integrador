Menu = """
\n Menu Principal 
1 - Ingresar como alumno
2 - Ingresar como profesor
3 - Informes
4 - Salir 
"""

# Menu principal
def menu_principal():
    while True:
        print(Menu)
        
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            email = input("Ingrese su email: ")
            print("ingresar_como_alumno(email)")
        elif opcion == "2":
            email = input("Ingrese su email: ")            
            print("ingresar_como_profesor(email)")
        elif opcion == "3":
            print("informes()")
        elif opcion == "4":
            print("Saliendo del sistema....")
            break
        else:
            print("Opción inválida.")

