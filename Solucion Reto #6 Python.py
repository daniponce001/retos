''' Invirtiendo Cadenas '''
# Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH".

def invCadena(cadena):
    cadena_inv = ''
    for i in range(len(cadena)-1, -1, -1):
        cadena_inv += cadena[i]
    print(cadena_inv)

invCadena('Hola mundo')
invCadena('AnitaLavaLaTina')
invCadena('Amor')
