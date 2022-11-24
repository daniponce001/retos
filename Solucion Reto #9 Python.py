''' CÓDIGO MORSE '''
# Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# - En morse se soporta raya "-", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.

class Morse:
    ''' Hace la conversión de una string de texto alfanumérico a un string de código morse y
        de un string de código morse a un string de texo alfanumérico. '''

    def __init__(self, frase):
        self.frase = frase
        self.letras = [' ','A','B','C','CH','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                       '0','1','2','3','4','5','6','7','8','9',
                       '.',',','?','"','/']
        self.morse = ['','·-','-···','-·-·','----','-··','·','··-·','--·','····','··','·---','-·-','·-··','--','-·','--·--','---','·--·','--·-','·-·','···','-','··-','···-','·--','-··-','-·--','--··',
                       '-----','·----','··---','···--','····-','·····','-····','--···','---··','----·',
                       '·-·-·-','--··--','··--··','·-··-·','-··-·']
        self.indices = []


    def conversor(self):
        ''' Identifica si el string de entrada esta escrito en texto alfanumérico o
            o en código morse.
            Basta con reconocer el primer carácter. '''
        if self.frase[0] in self.letras:
            return Morse(self.frase).letras_to_morse()
        elif self.frase[0] in self.morse:
            return Morse(self.frase).morse_to_letras()


    def letras_to_morse(self):
        ''' Hace la conversión de texto alfanumérico a código morse. '''
        morse = ''
        for i in range(len(self.frase)):
            if self.frase[i] == 'C' and self.frase[i + 1] == 'H':
                self.indices.append(self.letras.index('CH'))
            elif self.frase[i] == 'H' and self.frase[i - 1] == 'C':
                pass    
            else:
                self.indices.append(self.letras.index(self.frase[i]))
        for j in self.indices:
            morse = morse + self.morse[j] + ' '
        return morse
    

    def morse_to_letras(self):
        ''' HAce la conversión de código morse a texto alfanumérico. '''
        letras = ''
        for i in self.frase.split(' '):
            self.indices.append(self.morse.index(i))
        for j in self.indices:
            letras = letras + self.letras[j]
        return letras
        


frase_letras = 'CHOCAPIC. ES UNA MARCA DE CEREALES?'

morse = Morse(frase_letras).conversor()
print(morse)
letras = Morse(morse).conversor()
print(letras)
