""" Hola a todos repaso de python """
#comentario otra vez
from gettext import install


message= 'Hola a todos'
print(message)

#Variables
numero = 1
x= 12
y=1
z=0
print(x,y,z, sep='|')
print (f"{x}+{y} kkfkkkekfkekfefkfjfkefkefkefke  : ,ms 2732n ")
#F string sirve para escribir toda una cadena sin necesidad de estar usando espacios comas y demas
""" Sequences styles"""
""" list, tuple, range  """
""" Mapeo: diccionario """
""" Booleans: bytes (True, False) """

""" Pasar cadena a numero """
holi= "12"
holin=int(holi)
print(holin+1)
""" Ver el tipo de variable """
print(type(holin))

""" Diferencia de los booleanos de python: T mayuscula y F mayuscula al usar false and true """
""" Example """
ismonday= False
if ismonday is True:
    print("Ist monday")
else:
    print("today is not monday")
""" si uso print(bool()) con none, False o vacio me va a dar false, si lo uso con una cadena me devuelve True """
""" Listas """
list= [1,2,2,3,5]
print(list)
""" Pueden ir por datos de distintos tipos, son ordenadas es decir que tiene posiciones 
y se pueden eliminar o mover"""
""" Si no recuerdo como usar una variable o funcion
puedo hacer print(dir(list)) y me va a dar las funciones con las q puedo usarla"""
""" Las tuplas no se pueden modificar """
#loops de una lista
for i in list:
 print(i)
