f=open('C:/Users/User/OneDrive/Escritorio/EJERCICIOS PYTHON/mi_archivo.txt', 'r')
datos=f.read()
f.close()
print(datos)

f=open('C:/Users/User/OneDrive/Escritorio/EJERCICIOS PYTHON/mi_archivo.txt', 'w')
f.write("Hola, soy Gabriela Cristina Rodriguez\n")
f.write("y estoy haciendo el Open Bootcamp Python")
f.close()