''' Aspect Ratio de una imagen '''
# Crea un programa que se encargue de programar el aspect ratio de una imagen a partir de una url.
# - Nota: Esta prueba no se puede resolver con el playground online de Kotlin. Se necesita Android Studio.
# - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png.
# - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.


from urllib import request                                      # proporciona una interfaz de programación para usar recursos de Internet identificados por URLs
from PIL import Image                                           # permite la edición de imágenes directamente desde Python

def descImagen(url):
    ''' Dercarga una imagen apartie de una url dada '''
    request.urlretrieve(url, 'local_file.png')                  # recupera la imagen de la url

def paramImagen():
    ''' Obtiene el ancho y el alto de una imagen dada '''
    img = Image.open('local_file.png')
    width, height = img.size                                # entrega los valores de tamaño de la imagen y los guardamos
    return width, height

def aspectRatio(width,height):
    ''' Calcula el aspect ratio de la imagen. '''
    i = 101                                                     # i es el numero que dividira al ancho y alto de la imagen
    n = True                                                    # n es el estado de iteracion, True: iterando; False: deja de iterar
    while n:
        if i == 1:                                              # si i llega a 1 dejamos de iterar
            n = False
        elif width%i != 0 or height%i != 0:                 # si i no es divisor de albos, ancho y alto, no se hace al división y restamos 1 a i
            i -= 1
        elif width%i==0 and height%i==0:                    # si i es divisor de ambos, ancho y alto, se hace la división y volvemos a guardar los valores
            width, height = width/i, height/i
    return int(width), int(height)
            

# Cuatro ejemplos
url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
url2 = "https://i.pinimg.com/564x/40/1a/22/401a22e837068a068afa64181b1ca202.jpg"
url3 = "https://i.pinimg.com/564x/12/87/1b/12871b6e8385373148359ec16391f60f.jpg"
url4 = "https://calculateaspectratio.com/img/16-9-aspect-ratio.png"


descImagen(url)                                                 # recuperamos la imagen apartir de una url
wid_i, hei_i = paramImagen()                                    # obtenemos las el tamaño de la imagen y guardamos los valores
wid, hei = aspectRatio(wid_i,hei_i)                             # calculamos el aspect ratio
print(wid,':',hei)


descImagen(url2)                
wid_i, hei_i = paramImagen()
wid, hei = aspectRatio(wid_i,hei_i)
print(wid,':',hei)


descImagen(url3)
wid_i, hei_i = paramImagen()
wid, hei = aspectRatio(wid_i,hei_i)
print(wid,':',hei)


descImagen(url4)
wid_i, hei_i = paramImagen()
wid, hei = aspectRatio(wid_i,hei_i)
print(wid,':',hei)
