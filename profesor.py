from usuario import Usuario

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, mail: str, password: str, titulo: str, anio_egreso: int) -> None:
        super().__init__(nombre, apellido, mail, password)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        Usuario.usuarios_registrados.append({"mail": self.mail, "password": self.password, "tipo": "profesor"})
        self.__mi_cursos = []
        
    @property
    def mi_cursos(self):
        return self.__mi_cursos

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, nuevo_titulo: str):
        self.__titulo = nuevo_titulo

    @property
    def anio_egreso(self) -> int:
        return self.__anio_egreso

    @anio_egreso.setter
    def anio_egreso(self, nuevo_anio_egreso: int):
        self.__anio_egreso = nuevo_anio_egreso