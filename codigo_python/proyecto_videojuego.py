import random

def run():
    numero = int(input("Qué número penso la computadora? (Elije entre 1 - 100): "))
    pc_numero = random.randint(1,100)
    print(pc_numero)

    while numero != pc_numero:
        if numero > pc_numero:
            numero = int(input("Busca un numero más pequeño: "))
        else:
            numero = int(input("Busca un numero más grande: "))
    print("Ganaste!") 

if __name__ == '__main__':
    run()