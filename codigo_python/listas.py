objetos = ["Hola", 2, 4.5, True]

objetos[0]
#'Hola'

objetos[3]
# True

objetos.append(False)
# ["Hola", 2, 4.5, True, False]

objetos.pop(1) #Pasa como parámetro el índice de la lista
# 2
# Elimina el valor de la pos 2
# ["Hola", 4.5, True, False]

for elemento in objetos:
    print(elemento)
#Hola
#4.5
#True
#False

objetos[::-1]
#[False, True, 4.5, "Hola" ]

objetos[1:3]
# [4.5, True]
