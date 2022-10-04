# FUNCION AÑO BISIESTO:
#----------------------
#Declaracion
#~~~~~~~~~~~

def esBisiesto(anio):
    if anio%4==0 and anio%100!=0 or anio%400==0:
        return True
    else:
        return False

#ingreso de datos
anio=int(input("Ingresar anio: "))

#Llamada a la funcion
#~~~~~~~~~~~~~~~~~~~~~

respuesta=esBisiesto(anio)

#comprobacion
if respuesta==True:
    print("El año",anio,"es bisiesto.")
else:
    print("El año",anio,"no es bisiesto.")