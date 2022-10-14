import pickle
class Vehiculo:
    marca=""
    color=""
    modelo=0

    def __init__(self,marca,color, modelo):
        self.marca=marca
        self.color=color
        self.modelo=modelo
    
    def getMarca(self):
        return self.marca

v=Vehiculo("Mazda","blanco",1980)
f=open("datos.bin","wb")
pickle.dump(v, f)
f.close()

f=open("datos.bin","rb")
Mazda=pickle.load(f)
f.close()

print("El vehiculo es un",Mazda.getMarca(),"color",Mazda.color,",modelo",Mazda.modelo)

    


