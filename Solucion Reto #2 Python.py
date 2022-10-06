''' La Sucesión de Fibonacci '''
# Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
# La serie de Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...

def fibo():
    ''' Calcula los primeros 50 números de la sucesión de Fibonacci '''
    n0, n1 = 0, 1                       # estos dos inician la sucesión
    i = 1                               # un contador que inicia en 1
    while i <= 50:                      # hace el loop hasta 50 veces
        print(n0)
        ni = n0 + n1                    # un número es el resultado se sumar los dos números anteriores
        n0, n1 = n1, ni
        i += 1

fibo()
