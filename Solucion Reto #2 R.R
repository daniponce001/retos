## #############################################
##             SUCESIÓN DE FIBONACCI           #
## #############################################

# Enunciado: Escribe un programa que imprima los 50 primeros números se la sucesión de Fibonacci empezando en 0.
# La serie de Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13

fibonacci <- function(){
	n0 <- 0
	n1 <- 1
	i <- 1
	while(i <= 50){
		print(n0)
		ni <- n0 + n1
		n0 <- n1
		n1 <- ni
		i = i + 1
	}
}

fibonacci()