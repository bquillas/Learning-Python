valor_dolar = 3.5

def dolar_soles():
    soles = input("¿Cuántos Nuevos Soles tienes?: ")
    soles = float(soles)

    dolares = soles / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)

    print("Tienes $" + dolares + " dolares.")

def soles_dolar():
    dolar = input("¿Cuántos Dólares tienes?: ")
    dolar = float(dolar)

    sol = dolar * valor_dolar
    sol = round(sol,2)
    sol = str(sol)

    print("Tienes S./" + sol + " Nuevos Soles.")


opcion = input("¿Que cambio desea realizar? -Ingrese Opción 1 o 2- \
    1. Convertir Dolar a Soles  \
    2. Convertir Soles a dolares \
    Opción: ")

opcion = int(opcion)

if (opcion == 1):
    dolar_soles()
else:
    soles_dolar()

