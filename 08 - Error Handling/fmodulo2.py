class modulo():

    def __init__(self, lista):
        if type(lista) != list:
            raise ValueError(f'Se esperaba un objeto del tipo lista, pero se ha recibido uno de tipo {type(lista)}')
        else:
            self.x1 = lista

    def fprimo(self):
        '''
        Esta función permite conocer si el número ingresado, la variable "numero", es un 
        número primo o no. Devuelve la variable "primo" como tipo bool.
        '''

        primos = []
        for j in self.x1:
            primo = True
            if j < 2:
                primo = False
                print(j,primo)
            else:
                for i in range(2, int(j/2) + 1):
                    if j % i == 0:
                        primo = False
                #print(j,primo)
            primos.append(primo)
        return primos


    def temperatura(self, igrados, fgrados):

        '''
        Esta función permite obtener la temperatura en 3 escalas diferentes 
        [fahrenheit, celsius, kelvin], y solo acepta dichas escalas como input y un valor
        del tipo int o float
        '''
        l = ['celsius','kelvin','farenheit']
        y = 0

        q = []
        for j in self.x1:

            assert type(j) == int or type(j) == float, 'El primer argumento de la función debe ser un entero o un flotante'

            assert igrados in l, f'El segundo argumento de la función debe ser cualquier elemento de la siguiente lista {l}'
            
            assert fgrados in l, f'El tercer argumento de la función debe ser cualquier elemento de la siguiente lista {l}'
            
            if j < 0 and igrados == l[1]:
                print(f'El menor valor en la escala {l[1]} es el cero y tú trataste de convertir {j} grados')

            elif j < -273.15 and igrados == l[0]:
                print(f'El menor valor en la escala {l[0]} es el -273.15 y tú trataste de convertir {j} grados')

            elif j < -459.67 and igrados == l[2]:
                print(f'El menor valor en la escala {l[2]} es el -459.67 y tú trataste de convertir {j} grados')

            else:
                
                # for i in self.x1:
                #     if type(i) == int or type(i) == float:
                #         pass
                #     elif type(i) != int and type(i) != float:
                #         print('La lista solo puede contener elementos del tipo: [int,float]')
                #         break
            
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
                
                q.append(y)
        
                print(f'{j} grados {igrados} equivalen a {y} grados {fgrados}')    
        return q

    def factorial(self):

        '''
        Función factorial sin recurrencia. Necesita un input de tipo int.  
        '''
        q = []
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
            q.append(x)
        return q
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
        return [y,max(x)] #f'La moda es {y} y se repite {max(x)} veces'