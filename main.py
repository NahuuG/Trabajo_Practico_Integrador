from usuario import Usuario
from estudiante import Estudiante
from profesor import Profesor

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


# Menu para ALUMNOS
def menu_alumno(estudiante):
    while True:
        print(f"\n Bienvenido {estudiante.nombre}")
        print("Menú Alumno")
        print("1 - Matricularse a un curso")
        print("2 - Ver cursos matriculados")
        print("3 - Volver al menú principal")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            "matricularse_a_curso(estudiante)"
        elif opcion == "2":
            "ver_cursos_matriculados(estudiante)"
        elif opcion == "3":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


# Menu para PROFESORES
def menu_profesor(profesor):
    while True:
        print(f"\n Bienvenido {profesor.nombre}")
        print(" Menú Profesor")
        print("1 - Dictar curso")
        print("2 - Ver cursos dictados")
        print("3 - Volver al menú principal")
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            "dictar_curso(profesor)"
        elif opcion == "2":
            "ver_cursos_dictados(profesor)"
        elif opcion == "3":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


# Menu para INFORMES
def informes():
    while True:
        print("\n Informes ")
        print("1 - Listado de cursos")
        print("2 - Listado de alumnos")
        print("3 - Listado de profesores")
        print("4 - Volver")
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            "ver_cursos(lista_cursos)" # Imprime la lista de los cursos disponibles
        elif opcion == "2":
            "ver_alumnos()" # Imprime la lista de los alumnos dados de alta
        elif opcion == "3":
            "ver_profesores()" # Imprime a los profesores dados de alta
        elif opcion == "4":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")