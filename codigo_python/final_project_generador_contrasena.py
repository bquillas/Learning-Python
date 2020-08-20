import random

def generar_contrasena():
    mayuscula = ['A','B','C','D','E','F','G','H','I','J','K','L','LL','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    minuscula = ['a','b','c','d','e','f','g']
    caracter = ['!','@','#','$','%','&','/','(',')','*','+','.']
    numero = ['1','2','3','4','5','6','7','8','9','0']

    cadena_caracteres = mayuscula + minuscula + caracter + numero

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(cadena_caracteres)
        contrasena.append(caracter_random)
    
    contrasena = ''.join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print('tu nueva contraseña es: ' + contrasena)



if __name__ == '__main__':
    run()