''' ¿Es un número primo? '''
# Escribe un programa  que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.

def esPrimo(n):
    ''' Determina si un numero dado es un número primo o no '''
    if n < 2:                           # por definición los números primos son números naturales mayores que 1
        return False
    for i in range(2,n):                # si existe un número en el rango del 2 al número dado que sea divisor del número dado,
        if n % i == 0:                  # entonces el número dado no es un número primo
            return False
    return True                         # el número dado es un número primo si no se cumple la condición anterior

def primos():
    ''' Muestra los numeros primos del 1 al 100 '''
    for i in range(1,101):
        if esPrimo(i):                  # usamos la función anterior para ver si los números dados son números primos
            print(i)                    # motramos en número que si sea primo

primos()
