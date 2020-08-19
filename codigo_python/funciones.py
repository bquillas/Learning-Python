""" def imprimir_mensaje():
    print("Hola, estoy aprendiendo funciones!")

imprimir_mensaje()
imprimir_mensaje() """

def conversacion(mensaje):
    print("Hola")
    print("Cómo estás")
    print(mensaje)
    print("Adios")

opcion = int(input("Elige una opciòn (1, 2, 3): "))

if opcion == 1:
    conversacion("Elegiste la opción 1")

elif opcion == 2:
    conversacion("Elegiste la opción 2")

elif opcion == 3:
    conversacion("Elegiste la opción 3")

else:
    print("Elige una opcion correcta")

    