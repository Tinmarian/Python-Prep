def verifica_primo(numero):
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    return es_primo


# Iniciamos un bucle para estar dando las opciones de salir del programa o de ingresar un número para verificar si es primo, 
# y en caso de que dicho número sea primo, dar las opciones de encontrar el siguiente número primo o de ingresar 
# otro número para su verificación.
while True:

    a = input('Ingresa un número para verificar si es primo, recuerda ingresar solo números enteros, '
            'si ingresas un número real se omitiran las decimales después del punto. Puedes salir del programa con la tecla "ESC".')
    type(a)
    # Es importante no olvidarnos de que el comando input() regresa una cadena, no un entero. Y nosotros necesitamos un entero.
    a = float(a)
    a = int(a)

    # Sabemos que números menores o iguales a 1 no son primos.
    if a <= 1:
        print(a, 'no es primo \n')
        b = input('Escribe 1 para dar otro número a verificar o escribe 2 para salir')

    # Para todos los números positivos mayores a uno vamos a verificar si es primo.
    else:
        if verifica_primo(a):
            print(a, 'es primo \n')
            b = input('Escribe 1 para encontrar el siguiente número primo o 2 para dar otro número. '
                'Puedes salir del programa con la tecla "ESC" o con cualquier otro número.')
            b = float(b)
            b = int(b)

            if b == 1:
                while b == 1:
                    while True:
                        a += 1
                        if verifica_primo(a):
                            print(a, 'es el siguiente número primo')
                            break
                    b = input('Escribe 1 para encontrar el siguiente número primo o 2 para dar otro número. '
                        'Puedes salir del programa con la tecla "ESC" o con cualquier otro número.')
                    b = float(b)
                    b = int(b)

            if b == 2:
                continue
            else:
                break

        else:
            print(a, 'no es primo')           
            b = input('Escribe 1 para verificar otro número. '
                'Puedes salir del programa con la tecla "ESC" o con cualquier otro número.')
            b = float(b)
            b = int(b)

            if b == 1:
                continue
            else:
                break