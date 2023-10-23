from usuario import Usuario

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, mail: str, password: str, titulo: str, anio_egreso: int) -> None:
        super().__init__(nombre, apellido, mail, password)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        Usuario.usuarios_registrados.append({"mail": self.mail, "password": self.password, "tipo": "profesor"})
        self.__mi_cursos = []