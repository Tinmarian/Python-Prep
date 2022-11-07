class modulo():

    def __init__(self):
        pass

    def fprimo(self, numero):
        '''
        Esta función permite conocer si el número ingresado, la variable "numero", es un 
        número primo o no. Devuelve la variable "primo" como tipo bool.
        '''
        primo = True
        if numero < 2:
            primo = False
        else:
            for i in range(2, int(numero/2) + 1):
                if numero % i == 0:
                    primo = False
                    break
        return primo

    def moda(self, lista):

        '''
        De una lista de números enteros, devuelve el valor más repetido y cuántas veces se 
        repitio
        '''

        x = []
        z = 0
        for i in list(set(lista)):
            x.append(lista.count(i))
            lis2 = list(zip(list(set(lista)),x))
        for j in range(0,len(lis2)):
            if lis2[j][1] > z:
                y = lis2[j][0]    
                z = lis2[j][1]
        return f'La moda es {y} y se repite {max(x)} veces'

    def temperatura(self, valor, igrados, fgrados):

        '''
        Esta función permite obtener la temperatura en 3 escalas diferentes 
        [fahrenheit, celsius, kelvin], y solo acepta dichas escalas como input y un valor
        del tipo int o float
        '''
        
        y = 'NaN'
        
        if (igrados == 'celsius' and fgrados == 'farenheit'):
            y = (valor*9/5) + 32
        elif igrados == 'celsius' and fgrados == 'kelvin':
            y = valor + 273.15
        elif igrados == 'celsius' and fgrados == 'celsius':
            y = valor
        elif igrados == 'farenheit' and fgrados == 'celsius':
            y = (valor - 32)*5/9
        elif igrados == 'farenheit' and fgrados == 'kelvin':
            y = (valor - 32)*5/9 + 273.15
        elif igrados == 'farenheit' and fgrados == 'farenheit':
            y = valor
        elif igrados == 'kelvin' and fgrados == 'farenheit':
            y = (valor - 273.15)*9/5 +32
        elif igrados == 'kelvin' and fgrados == 'celsius':
            y = valor - 273.15
        elif igrados == 'kelvin' and fgrados == 'kelvin':
            y = valor

        if type(y) == int or type(y) == float:    
            return f'{valor} grados {igrados} equivalen a {y} grados {fgrados}'
        else:
            return print('Recuerda que solo puedes convertir grados [celsius, farenheit,'
                        'kelvin], y solo puedes obtener,''como resultado, grados [celsius, farenheit, kelvin]')

    def factorial(self,numero):

        '''
        Función factorial sin recurrencia. Necesita un input de tipo int.  
        '''

        x = 1

        if numero < 0:
            print('Debes ingresar un entero que sea positivo')
        #elif type(numero) == str or type(numero) == float or type(numero) == bool or type(numero) == list or type(numero) == tuple:
        elif type(numero) != int:
            print('El tipo de dato debe ser [int]')
        else:
            for i in range(1,numero+1):
                x = x * i
        return x

def factorial(numero):

    '''
    Función factorial sin recurrencia. Necesita un input de tipo int.  
    '''

    x = 1

    if numero < 0:
        print('Debes ingresar un entero que sea positivo')
    #elif type(numero) == str or type(numero) == float or type(numero) == bool or type(numero) == list or type(numero) == tuple:
    elif type(numero) != int:
        print('El tipo de dato debe ser [int]')
    else:
        for i in range(1,numero+1):
            x = x * i
    return x

def fprimo(numero):
    '''
    Esta función permite conocer si el número ingresado, la variable "numero", es un 
    número primo o no. Devuelve la variable "primo" como tipo bool.
    '''
    primo = True
    if numero < 2:
        primo = False
    else:
        for i in range(2, int(numero/2) + 1):
            if numero % i == 0:
                primo = False
                break
    return primo