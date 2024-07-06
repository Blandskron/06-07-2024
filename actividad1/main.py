from modulos.tiposdesaludos.saludar import saludo
from modulos.tiposdedespedida.despedida import despedida
import datetime as dt

hoy = dt.date.today()

nombre = input("Ingrese su nombre: ")
estadia = int(input("Cuantos dias estara en nuestro hotel: "))

retiro = hoy + dt.timedelta(days=estadia)

print(saludo(nombre, hoy))
print(despedida(nombre, retiro))
