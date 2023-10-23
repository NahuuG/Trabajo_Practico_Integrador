from usuario import Usuario
from curso import Curso

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
                
    def __str__(self) -> str:
        return f"""
    \nNombre: {self.nombre}
    \nTítulo: {self.titulo}
    \nAño de egreso: {self.anio_egreso}"""
    
    def dictar_curso(self, curso: Curso) -> None:
        print(f"El profesor {self.nombre} está dictando el curso: {curso.nombre}")
   
    

profe1 = Profesor("Mercedes", "Viloni", "me@123", "me123", "Programadora", 2018)
profe2 = Profesor("Juan", "Pepe", "pe@123", "pe123", "Ingeniero en sistema", 2019)

lista_profesores = [profe1, profe2]

