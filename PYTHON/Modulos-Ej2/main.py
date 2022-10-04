
import datetime

fecha_hoy=datetime.datetime.now()

def calcula_FinDeJornada(fecha_hoy):
    salida=datetime.datetime.now().replace(hour=19, minute=0,second=0)
    faltan=salida-fecha_hoy
    return faltan

def traductor():
    DiaSem=datetime.datetime.today().strftime('%A')
    if DiaSem == "Monday":
        return "lunes"
    elif DiaSem == "Tuesday":
        return "martes"
    elif DiaSem == "Wednesday":
        return "miercoles"
    elif DiaSem == "Thursday":
        return "jueves"
    elif DiaSem == "Friday":
        return "viernes"
    else:
        return "domingo"
    
hora,minuto,segundo=(fecha_hoy.hour,fecha_hoy.minute,fecha_hoy.second)
horas,minutoss,segundoss=(19,0,0)

dia=traductor()

print("Hoy es:",dia,fecha_hoy)

if dia == "sabado" or dia == "domingo":
    print(f"Hoy,{dia}, no es dia laboral.")
else:
    if hora < horas and hora >=12:
       tiempores=calcula_FinDeJornada(fecha_hoy)
       print("Nos encontramos dentro del horario laboral.")
       print(f"Faltan hs:{tiempores} para terminar la jornada.")
    else:
       print(f"A las {hora}:{minuto}:{segundo} te encontras fuera de tu horario laboral.")
    





