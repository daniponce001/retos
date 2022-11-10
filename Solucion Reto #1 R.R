## ##############################################
##                ¿ES UN ANAGRAMA?              #
## ##############################################

# Escribe una función que reciba dos palabras (character en R) y retorne verdadero o falso (logical en R) según sean o no anagramas.
# Un Anagrama cocsite en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras exitan.
# Dos palabras exactamnte iguales no son anagramas.

anagrama <- function(palabra1, palabra2){
	palabra1 <- tolower(palabra1)
	palabra2 <- tolower(palabra2)

	if (palabra1 == palabra2) {
		FALSE
	}else{
	
		letras1 <- c()
		letras2 <- c()
	
		for (i in 1:nchar(palabra1)){
			letras1 <- c(letras1, substr(palabra1,i,i))
		}
		for (i in 1:nchar(palabra2)){
			letras2 <- c(letras2, substr(palabra2,i,i))
		}
	
		letras_sorted1 <- sort(letras1)
		letras_sorted2 <- sort(letras2)

		all(letras_sorted1 %in% letras_sorted2)
	}
}

anagrama('roma','amor')
anagrama('roma','ROMA')
anagrama('roma','paloma')