# DICCIONARIOS

#Estructuras de datos, otros más son: (Colas, Pilas, Arboles, etc)
#Los indices son las llaves

def run():
    mi_diccionario = {
        'llave1':1,
        'llave2':2,
        'llave3':3,
    }

    # print(mi_diccionario)
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44938485,
        'Peru':30456987,
        'Colombia':7895346232,
    }

    # print(poblacion_paises['Peru'])

    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for pais in poblacion_paises.values():
    #     print(pais)

    for pais , poblacion in poblacion_paises.items():
        print(pais + " tiene una pablación de : "+ str(poblacion) + " habitantes")



if __name__ == '__main__':
    run()