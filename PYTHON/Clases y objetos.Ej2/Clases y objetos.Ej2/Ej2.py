class Alumno:
    nombre=None
    nota=None
    def __init__(self):
        self.nombre=input("Ingrese el nombre del alumno:")
        self.nota=float(input("Ingrese la nota:"))
    def resultado_nota(self):
        if self.nota >= 7:
            print("La nota es:",self.nota,"y se encuentra aprobado")
        else:
            print("La nota es:",self.nota,"y no aprobó")

a=Alumno()
a.resultado_nota()