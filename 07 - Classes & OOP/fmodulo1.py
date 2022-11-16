class modulo():

    def __init__(self, lista):
        self.x1 = lista

    def fprimo(self):
        '''
        Esta función permite conocer si el número ingresado, la variable "numero", es un 
        número primo o no. Devuelve la variable "primo" como tipo bool.
        '''
        for j in self.x1:
            primo = True
            if j < 2:
                primo = False
                print(j,primo)
            else:
                for i in range(2, int(j/2) + 1):
                    if j % i == 0:
                        primo = False
                print(j,primo)
                                  

    def temperatura(self, igrados, fgrados):

        '''
        Esta función permite obtener la temperatura en 3 escalas diferentes 
        [fahrenheit, celsius, kelvin], y solo acepta dichas escalas como input y un valor
        del tipo int o float
        '''
        
        for j in self.x1:
            y = 'NaN'
            
            if (igrados == 'celsius' and fgrados == 'farenheit'):
                y = (j*9/5) + 32
            elif igrados == 'celsius' and fgrados == 'kelvin':
                y = j + 273.15
            elif igrados == 'celsius' and fgrados == 'celsius':
                y = j
            elif igrados == 'farenheit' and fgrados == 'celsius':
                y = (j - 32)*5/9
            elif igrados == 'farenheit' and fgrados == 'kelvin':
                y = (j - 32)*5/9 + 273.15
            elif igrados == 'farenheit' and fgrados == 'farenheit':
                y = j
            elif igrados == 'kelvin' and fgrados == 'farenheit':
                y = (j - 273.15)*9/5 +32
            elif igrados == 'kelvin' and fgrados == 'celsius':
                y = j - 273.15
            elif igrados == 'kelvin' and fgrados == 'kelvin':
                y = j

            if type(y) == int or type(y) == float:    
                print(igrados, '=', j, fgrados, '=', y)
            else:
                return print('Recuerda que solo puedes convertir grados [celsius, farenheit,'
                            'kelvin], y solo puedes obtener,''como resultado, grados [celsius, farenheit, kelvin]')

    def factorial(self):

        '''
        Función factorial sin recurrencia. Necesita un input de tipo int.  
        '''
        for j in self.x1:
            x = 1

            if j < 0:
                print('Debes ingresar un entero que sea positivo')
            #elif type(numero) == str or type(numero) == float or type(numero) == bool or type(numero) == list or type(numero) == tuple:
            elif type(j) != int:
                print('El tipo de dato debe ser [int]')
            else:
                for i in range(1,j+1):
                    x = x * i
            print(x)

    def moda(self):

        '''
        De una lista de números enteros, devuelve el valor más repetido y cuántas veces 
        se repitio
        '''

        x = []
        z = 0
        for i in list(set(self.x1)):
            x.append(self.x1.count(i))
            lis2 = list(zip(list(set(self.x1)),x))
        for j in range(0,len(lis2)):
            if lis2[j][1] > z:
                y = lis2[j][0]    
                z = lis2[j][1]
        return f'La moda es {y} y se repite {max(x)} veces'