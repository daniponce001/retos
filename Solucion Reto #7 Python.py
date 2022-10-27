''' Contando Palabras '''
# Crea un programa que cuante cuantas veces se repite cada palabra y que muestre el recuento final de todas ella.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilzar funciones propias del lenguaje que lo resuelvan automáticamente

def wordsCount(frase):
    ''' Preparamos la frase para contar las palabras. '''

    frase = frase.lower()                       # todo en minúsculas.

    signos = [',', '.', ';', ':', '?', '¿', '!', '¡', '...', '(', ')', '[', ']', '"', "'", '-']

    for i in frase:                             # sacamos los signos de puntuación reemplazandolos por espacios en blanco
        if i in signos:
             frase = frase.replace(i, ' ')

    frase = frase.split()                       # dividimos la frase en palabras, queda en una lista.

    cuenta_palabras = {}
    for i in frase:                             # recorremos la lista de palabras contando las veces que se repite cada palabra.
        n = 0
        for j in frase:
            if i == j:
                n += 1
        cuenta_palabras.update({i:n})           # guardamos el conteo en un diccionario, no se repiten las claves en un diccionario

    for k, v in cuenta_palabras.items():        # presenta el conteo de las palabras.
        if v == 1:
            print('"{}" aparece {} vez'.format(k,v))
        else:
            print('"{}" aparece {} veces'.format(k,v))



a = '¡Hola, mi nombre es "Daniel"!. ¿Mi nombre completo es Daniel Ponce?. completo - completo'
print('En la frase "{}":'.format(a))

wordsCount(a)
