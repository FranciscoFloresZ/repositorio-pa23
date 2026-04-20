class Persona:
    def __init__(self, nombre, edad, peso, altura, ciudad):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
        self.__altura = altura
        self.__ciudad = ciudad

     def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_peso(self):
        return self.__peso

    def get_altura(self):
        return self.__altura

    def get_ciudad(self):
        return self.__ciudad