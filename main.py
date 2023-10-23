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
            matricularse_a_curso(estudiante)
        elif opcion == "2":
            ver_cursos_matriculados(estudiante)
        elif opcion == "3":
            print("Volviendo al menú principal....")
            break
        else:
            print("Opción inválida.")


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
            

# Funcion para que el alumno ingrese al sistema
def ingresar_como_alumno(email): 
    # Recorre en la lista estudiantes a cada estudiante 
    for estudiante in lista_estudiantes:
        if estudiante.mail == email:
            password = input("Ingrese su contraseña: ")
            if Usuario.validar_credenciales(email, password):
                menu_alumno(estudiante)
                return
            else:
                print("Contraseña incorrecta. Por favor, inténtelo de nuevo.")
                return
    # Si no se encontro ningun alumno con ese mail se le pregunta si quiere darse de alta
    confirmacion = input("No se encontró un estudiante con ese email. ¿Desea darlo de alta? (si/no): ").lower()
    if confirmacion == "si":
        alta_alumno(email)
    else:
        print("Operacion cancelada.")


# Esta funcion nos muestra a los Cursos que esta o no inscripto el estudiante
def ver_cursos_matriculados(estudiante):
    if not estudiante.mi_cursos:
        print("No estás matriculado en ningún curso aún.")
    else:
        print("\n Cursos Matriculados ")
        for i, curso in enumerate(estudiante.mi_cursos, start=1):
            print(f"{i}. {curso.nombre}")


# Da la posibilidad a inscribirse a un curso
def matricularse_a_curso(estudiante):
    lista_cursos_ordenados = sorted(lista_cursos, key=lambda cursos: cursos.nombre)
    ver_cursos(lista_cursos)
    opcion = input("Seleccione el número del curso al que desea matricularse: ")
    if opcion.isdigit():
        curso_index = int(opcion) - 1
        if 0 <= curso_index < len(lista_cursos_ordenados):
            curso = lista_cursos_ordenados[curso_index]
            contrasenia = input(f"Ingrese la contraseña de matriculación para el curso {curso.nombre}: ")
            mensaje = estudiante.matricularse_al_curso(curso, contrasenia)
            print(mensaje)           
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")

        
# Se encarga de dar de alta a un alumno en el sistema
def alta_alumno(mail:str):
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    legajo = input("Ingrese el numero de legajo: ")
    password = input("Ingrese la contraseña: ")
    fecha_actual = datetime.datetime.now()
    fecha_inscripcion = fecha_actual.year
    nuevo_estudiante = Estudiante(nombre, apellido, mail, password, legajo, fecha_inscripcion)
    lista_estudiantes.append(nuevo_estudiante)