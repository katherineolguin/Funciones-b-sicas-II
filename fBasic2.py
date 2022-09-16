def countdown (x,y):
    while x > y:
        print(x)
        x -=1
countdown(5, 0)


def countdown(num): #num = 5
    lista = [] #Creamos lista vacía, para ahí poner todos los números
    for i in range(num, -1, -1): #(num con el que comenzamos, parada, avance)
        lista.append(i)
        #lista += [i]

    return lista

def countdownWhile(num):
    lista = []
    while num > -1:
        lista.append(num)
        num -= 1
    return lista


# Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
# Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2

def imp_devolver (array):
    
    print(array[0])

imp_devolver(array = [20,10])  

# primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
# Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)

def valor_longitud():
    Lista1 = [3,6,9,12]
    Lista2 = [2,4,6,8]
    
    suma = Lista1[0]+len(Lista1)
    return suma

suma = valor_longitud()
print(suma)

# Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
# Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
# Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False

def listas (listaC):
    
    if len(listaC)<2:
        return False

    new_listaC =[]   

    for num in listaC:

        if num > listaC[1]:
            new_listaC.append(num)
    
    return(new_listaC)    
print(listas([5,2,3,2,1,4]))
print(listas([]))




# Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
# Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
# Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]

def length_and_value(a,b):
    new_lisB = []
    for x in range(a):
        new_lisB.append(b)
    return new_lisB
print(length_and_value(6,2))
