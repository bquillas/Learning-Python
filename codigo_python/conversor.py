soles = input("¿cuantos Nuevos soles tienes?: ")
soles = float(soles)

valor_dolar = 3.5

dolares = soles / valor_dolar
dolares =round(dolares,2)
dolares = str(dolares)

print("Tienes $" + dolares + " dolares.")