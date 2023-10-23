class Curso:
    def __init__(self, nombre:str, contrasenia_matriculacion:str) -> None:
        self.__nombre = nombre
        self.__contrasenia_matriculacion = contrasenia_matriculacion
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre:str):
        self.__nombre = nuevo_nombre

    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion

    @contrasenia_matriculacion.setter
    def contrasenia_matriculacion(self, nueva_contrasenia_matriculacion:str):
        self.__contrasenia_matriculacion = nueva_contrasenia_matriculacion
        
    def __str__(self) -> str:
        return f"Curso: {self.nombre}"
    
    
curso1 = Curso("Programacion I", "programacion.123")
curso2 = Curso("Estadistica", "estadistica.123")


lista_cursos = [curso1, curso2]