def conversor(tipo_pesos,valor_dolar):
    pesos = input("¿Cuántos " + tipo_pesos +" tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares.")

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
    conversor('Pesos colombianos',3875)

elif opcion =='2':
    conversor('Pesos argentinos',65)

elif opcion =='3':
    conversor('Pesos mexicanos',24)

elif opcion =='4':
    conversor('Nuevos soles',3.5)

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

