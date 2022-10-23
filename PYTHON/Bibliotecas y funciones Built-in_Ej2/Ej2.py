from functools import reduce
#INGRESO DE DATOS POR USUARIO
numeros=[]
numero=int(input("Ingresar numeros mayores a 0 y 0 para finalizar:"))
while numero!=0:
    numeros.append(numero)
    numero=int(input("Ingresar numeros mayores a 0 y 0 para finalizar:"))
    
#FUNCIONES LAMBDA DE IMPARES Y DE SUMA DE IMPARES
imp=filter(lambda x: x%2!=0,numeros)
suma = reduce(lambda x, y: x + y, imp)
print(suma)
    
            
