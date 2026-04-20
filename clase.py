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
            def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_peso(self, peso):
        self.__peso = peso

    def set_altura(self, altura):
        self.__altura = altura

    def set_ciudad(self, ciudad):
        self.__ciudad = ciudad

    def cumplir_anios(self):
        self.__edad += 1

    def cambiar_ciudad(self, nueva_ciudad):
        self.__ciudad = nueva_ciudad
    
    def info(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Ciudad: {self.__ciudad}"

        p = Persona("Juan", 18, 70, 1.75, "Monterrey")

        print(p.info())
        p.cumplir_anios()
        p.cambiar_ciudad("CDMX")
        print(p.info())