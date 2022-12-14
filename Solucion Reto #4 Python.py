''' Área de un polígono '''
# Crea una única función (importante que solo sea una) que sea capaz e calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo un polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

class Poligono:
    ''' Objeto: poligono '''

    def __init__(self, altura, base=0):
        ''' Los objetos con los que vamos a trabajar comparten estos atributos.
            Definimos uno de los atributos como cero para el caso del cuadrado. '''
        self.a = altura
        self.b = base

    def areaTriangulo(self):
        ''' Caldula el área de un triángulo de una altura y base dadas. '''
        area = (self.a * self.b) / 2
        return area

    def areaRectangulo(self):
        ''' Calcula el área de un rectángulo de una altura y base dadas. '''
        area = self.a * self.b
        return area

    def areaCuadrado(self):
        ''' Calcula el área de un cuadrado con una altura dada. '''
        area = self.a**2
        return area


# Creamos objetos con los valores de sus atributos y calculamos las áreas con los metodos correspondentes
triangulo_area = Poligono(10,5).areaTriangulo()
print('Área del triangulo',triangulo_area)


rectangulo_area = Poligono(10,5).areaRectangulo()             
print('Área del rectangulo:',rectangulo_area)


cuadrado_area = Poligono(5).areaCuadrado()
print('Área del cuadrado:',cuadrado_area)
