class Alumno:
    def __init__(self, nombre, carnet, carrera, nota_final):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.nota_final = nota_final

    def mostrar_info(self):
        print(f"\nNombre Completo: ´{self.nombre}")
        print(f"Carnet: {self.carnet}")
        print(f"Carrera: {self.carrera}")
        print(f"Nota final:{self.nota_final} ")

class sis:
    def __init__(self):
        self.alumnos = []

    def registro_alumnos(self):
        print("\n REGISTRO")
        nombre = input("Por favor ingrese el nombre: ")
        carnet = input("Por favor ingrese el número de carnet: ")
        carrera = input ("Por favor ingrese su carrera ")
        Nota_final = input("Por favor ingrese la nota ")

    def mostrar_alumnos(self):



