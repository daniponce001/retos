''' ¿Es un anagrama? '''
# Escribe una función que reciba dos palabras (string) y retorne verdadero o falso (Boolean) según o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS las letras de  otra palabra inicial.
# No hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagramas.

def anagrama(word1, word2):
    ''' Verifica si dos "strings" son anagramas '''
    word1, word2 = word1.lower(), word2.lower()
    if word1 == word2: return False                 # Fasle si los 'strings' son iguales
    word1, word2 = sorted(word1), sorted(word2)     # hace todos los caracteres minusculas y los ordena en listas
    if word1 == word2: return True                  # True si las lsitas con los caracteres ordenados son iguales
    else: return False                              # False de otra manera


print(anagrama('roma', 'ROMA'))
print(anagrama('aMOr', 'roma'))
print(anagrama('camo', 'amor'))


