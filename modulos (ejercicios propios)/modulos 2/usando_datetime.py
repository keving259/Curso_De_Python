import datetime, calendar

x = datetime.datetime.now()

print(f"Fecha actual: {x.date()}")
print(f"Hora actual: {x.time()}")
print(f"Año actual: {x.year}\n")

year = x.year


# Se obtiene el número de días dependiendo se si es año bisiesto
if calendar.isleap(year):
    days = 366
else:
    days = 365

today = datetime.date.today() # Se obtiene la fecha
year_day = today.timetuple().tm_yday # Se obtiene qué número de día del año es

# Número de días en el año menos día del año
print(f"Faltan {days - year_day} días para que termine el año")
