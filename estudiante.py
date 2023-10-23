from usuario import Usuario


class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, mail: str, password: str, legajo: int, anio_inscripcion_carrera: int) -> None:
        super().__init__(nombre, apellido, mail, password)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        Usuario.usuarios_registrados.append({"mail": self.mail, "password": self.password, "tipo": "estudiante"})
        self.__mi_cursos = []