def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 21047125,
        'Colombia': 50372424
    }

    for pais, poblacion in poblacion_paises.items():
        print(pais + 'tiene ' + str(poblacion) + 'habitantes')

if __name__ == '__main__':
    run()