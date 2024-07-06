from actividad2.solicitardatos import datos

nombre = input("Ingrese un nombre: ")
edad = int(input("Ingrese su edad: "))
rut = int(input("Ingrese su rut: "))

print(datos(nombre, edad, rut))
