class Vehiculo:
    color="negro"
    ruedas=5
    puertas=4

class Coche(Vehiculo):
    velocidad=200
    cilindrada=6

c=Coche()
print("El coche es color",c.color,"tiene",c.ruedas,"ruedas y",c.puertas,"puertas.La velocidad maxima alcanzada es de",c.velocidad,"km/hora", "teniendo",c.cilindrada,"cilindros.")
