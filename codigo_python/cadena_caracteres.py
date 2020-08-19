nombre = input("¿Cu{al es tu nombre?: ")

nombre = nombre.capitalize() #Bill
nombre = nombre.strip() #'bill ' -> 'bill' Elimina Espacios en blanco
nombre = nombre.upper() # BILL
nombre = nombre.lower() # bill
nombre = nombre.replace('i','a') #remplaza los 'i' por 'a'
nombre[0] # Mediante índices puedes recorrer
len(nombre) # Cuenta la cantidad de caracteres que tiene el dato alamacenado en la variable 
len("bill") # Cuenta los caracteres del string -> 4


#TRABAJANDO CON TEXTO: SLICES (Rebanadas)

nombre = 'Francisco'

nombre[0]       # 'F' 
nombre[1]       # 'r' 
nombre[0:3]     # 'Fra' 
nombre[:3]      # 'Fra' 
nombre[3:]      # 'ncisco' 
nombre[1:7]     # 'rancis' 
nombre[1:7:2]   # 'rni' 
nombre[::]      # 'Francisco' 
nombre[1::3]    # 'rcc' 
nombre[::-1]    # 'ocsicnarF' 