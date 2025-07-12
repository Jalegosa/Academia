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