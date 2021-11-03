from imgurpython import ImgurClient
import os
import urllib.request
import timeit
from concurrent.futures import ThreadPoolExecutor  
from multiprocessing import Pool
secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_cliente = "bfa0e227a1c5643"
 
cliente = ImgurClient(id_cliente, secreto_cliente)
 
# Metodo para la descarga url imagen
# Datos necesarios del metodo
# Nombre de la imagen => yntdWAr
# Formato de la imagen => png
listaURL = []
 
def descarga_url_img(link):
   print(link)
   # Con esto ya podemos obtener el corte de la url imagen
   nombre_img = link.split("/")[3]
   formato_img = nombre_img.split(".")[1]
   nombre_img = nombre_img.split(".")[0]
   print(nombre_img, formato_img)
   url_local = "D:/UP CHIAPAS/SEPTIMO CUATRIMESTRE/Programacion Concurrente/Corte 2/Tareas/imagenes/{}.{}"
  
   #Guardar nne local las imagenes
   urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))
   
def multiprocessing_imagenes():
   print('multiprocessing')
   with Pool(len(listaURL)) as p:
        p.map(descarga_url_img,listaURL)

def url():
   id_album = "bUaCfoz"
   imagenes = cliente.get_album_images(id_album)
   for imagen in imagenes:
       listaURL.append(imagen.link)
   
if __name__ == "__main__":
   url()
   print("Tiempo de descarga {}".format(timeit.Timer(multiprocessing_imagenes).timeit(number=1)))
