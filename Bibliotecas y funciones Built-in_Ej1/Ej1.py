
#INGRESO DE USUARIO, GUARDADO EN LISTA, ELIMINA DUPLICADOS, ORDENA Y MUESTRA STRING SEPARADO POR COMAS

paises=[]
pais=input("Ingresar pais y * para finalizar:")
while pais!="*":
    paises.append(pais)
    pais=input("Ingresar y * para finalizar:")
    
salida=",".join(list(sorted(set(paises))))
print(f"Los paises sin duplicados y en orden alfabetico son:{salida}")
