''' Decimal a Binario '''
# Crea un programa que se encargue de tranformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente

def decimalToBinario(decimal):

    binario = ''
    n = True
    
    while n:
        if decimal == 0: return '0'
        
        elif decimal == 1: n = False
            
        else:
            residuo = decimal % 2
            decimal = decimal // 2
            binario = str(residuo) + binario

    binario = str(decimal) + binario
    
    return binario

def main():
    print(decimalToBinario(387))
    print(decimalToBinario(0))
    print(decimalToBinario(651518))

if __name__ == '__main__':
    main()

    
