from clases import Alumno
from clases import Final


suma2=0
promedioFinal=0
contadorAlumno=0
opcion=1
lista2=[]
while opcion==1:
    lista=[]
    contador=0
    nombre=input("Ingrese el nombre del Alumno : ")
    semestre=int(input("Ingrese el numero de semestre del Alumno : "))
    materias=int(input("Dime cuantas materia llevas : "))
    contadorv=0
    for numero in range (1,materias+1):
        contador=contador+1
        contadorv=contadorv+1
        print("*"*30)
        print(f"Materia {contadorv}:")
        calf1=float(input("Ingrese su calificacion : "))
        a=Alumno(calf1,nombre)
        a.Promedio()
        if contador==materias:
            contadorAlumno=contadorAlumno+1
            print("1=SI\n2=NO")
            opcion=int(input("Deseas seguir ejecutando el programa : "))
            print("*"*50)




b=Final(None,None)

Final=b.final()/contadorAlumno
print(f"Este es el Promedio Final del Salon : {Final}")
print("$"*50)
