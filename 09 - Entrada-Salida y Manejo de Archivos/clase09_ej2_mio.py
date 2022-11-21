from csv import writer
import pandas as pd
import datetime as dt

a = int(input('Ingresa la temperatura: '))
b = int(input('Ingresa el porcentaje de humedad: '))
c = input('Y si llovio o no, con [True] o [False]: ')
d = dt.datetime.now()

assert c == 'True' or c == 'False', 'Tu tercer argumento debe ser del tipo [bool].'
assert 10<=b<=60, 'El rango de humedad no está dentro de los límites.'
assert -10<=a<=50, 'El rango de temperatura no está dentro de los límites.'

lista = [d,a,b,c]
with open('Clase09_ej2_mio.csv', 'a') as objeto:
    escritura = writer(objeto)
    escritura.writerow(lista)
    objeto.close()
df = pd.read_csv('Clase09_ej2_mio.csv')





# Una forma más sencilla de realizar el ejercicio es como lo proponen en Henry:

# lista = str(d) + ',' + str(a) + ',' + str(b) + ',' + c
# csv = open('Clase09_ej2_mio.csv','a')
# csv.write(lista + '\n')
# csv.close()

# # Esta parte solo es de visualización:

# df = pd.read_csv('Clase09_ej2_mio.csv')
# df.columns = ['Fecha','Temperatura','Humedad','Lluvia']
# df1 = pd.read_csv('Clase09_ej2_mio.csv')





# Otra forma de hacerlo sería como sigue, y de esta forma sí podemos controlar
# el nombre de las columnas del .csv, aun cuando se elimine el archivo se 
# vuelva a crear. Utilicemos try y except.

# try:
#     objeto = open('Clase09_ej2_mio.csv','x')

#     lista = [d,a,b,c]
#     columnas = ['Fecha','Temperatura','Humedad','Lluvia']
#     df = pd.DataFrame([lista],columns=columnas)#,columns=columnas)
#     df.to_csv('Clase09_ej2_mio.csv',mode='w',header=True)

#     df1 = pd.read_csv('Clase09_ej2_mio.csv')

#     objeto.close()

# except FileExistsError:
#     objeto = open('Clase09_ej2_mio.csv','a')

#     lista = [d,a,b,c]
#     columnas = ['Fecha','Temperatura','Humedad','Lluvia']
#     df = pd.DataFrame([lista],columns=columnas)#,columns=columnas)
#     df.to_csv('Clase09_ej2_mio.csv',mode='a',header=False)

#     df1 = pd.read_csv('Clase09_ej2_mio.csv')

#     objeto.close()


print(f'Los datos se  han insertado correctamente y son...\nDatos añadidos: {lista}\nData Frame:\n{df}')#\nArchivo csv:\n{df1}')

