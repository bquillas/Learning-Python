menu = """
Bienvenido al conversor de Monedas 💰

1 - Pesos colombianos a Dolares
2 - Pesos argentinos a Dolares
3 - Pesos mexicanos a Dolares
4 - Nuevos Soles a Dolares
5 - Dolares a Nuevos Soles

Elige una opción: 
"""

opcion = input(menu)

if opcion == '1':
    pesos = input("¿Cuántos Pesos Colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares.")

elif opcion =='2':
    pesos = input("¿Cuántos Pesos Argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares.")

elif opcion =='3':
    pesos = input("¿Cuántos Pesos Mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares.")

elif opcion =='4':
    soles = input("¿Cuántos Nuevos Soles tienes?: ")
    soles = float(soles)
    valor_dolar = 3.5
    dolares = soles / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)

    print("Tienes $" + dolares + " dolares.")

elif opcion == '5':
    dolar = input("¿Cuántos Dólares tienes?: ")
    dolar = float(dolar)
    valor_dolar = 3.5
    sol = dolar * valor_dolar
    sol = round(sol,2)
    sol = str(sol)

    print("Tienes S./" + sol + " Nuevos Soles.")

else:
    print("Ingrese una opcion correcta, porfavor.")

