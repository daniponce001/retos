## ############################################## 
## #            EL FAMOSO "FIZZ BUZZ"           #
## ##############################################

# Escribe un programa que muestre por consola (coun un print) los números del 1 al 100 (ambos incluidos y con un salto de línea entre cada imporesión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra 'fizz'
# - Múltiplos de 5 por la palabra 'buzz'
# - Múltiplos de 3 y de 5 a la vez por la palabra 'fizzbuzz'

fizzbuzz <- function(){
	for (i in c(1:100)) {
		if (i%%3 == 0 & i%%5 == 0) {
			print('fizzbuzz')
		}
		if (i%%3 == 0) {
			print('fizz')
		}
		if (i%%5 == 0) {
			print('buzz')
		}
		else {
			print(i)
		}
	}
}

fizzbuzz()