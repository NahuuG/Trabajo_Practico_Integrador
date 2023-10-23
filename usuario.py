from abc import ABC, abstractmethod

class Usuario(ABC):

    def __init__(self, nombre: str, apellido: str, mail: str,password: str) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__mail = mail
        self.__password = password