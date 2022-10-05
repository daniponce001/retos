''' El famoso FizzBuzz '''
# Escribe un programa que muestre en consola (con un print) los números del 1 al 100 (ambos incluidos y con un salto de linea entra cada impresión), sustituyendolo.
# - Múltiplos de 3 por la palabra 'fizz'.
# - Múltiplos de 5 por la palabra 'buzz'.
# - Múltiplos de 3  y de 5 a la vez por la palabra 'fizzbuzz'.

def fizzbuzz():
    ''' Para cada numero del 1 al 100
        - si es multiplo de 3 muestra la palabra "fuzz"
        - si es multiplo de 5 muestra la palabra "buzz"
        - si es multiplode 3 y 5 muestra la palabra "fizzbuzz" '''
    
    for i in range(1, 101):
        if i%3==0 and i%5==0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fuzz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)

fizzbuzz()
