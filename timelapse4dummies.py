#!/usr/bin/env python
# Este archivo usa el encoding: utf-8

##########################################
##         Script realizado por         ##
##    Mario Fernández Gómez (mafergo)   ##
##     para automatizar tareas en la    ##
##     realización, por ejemplo, de     ##
##              timelapses.             ##
##  Para ello llamará a Imagemagick y   ##
##   creará la secuencia de vídeo con   ##
##              mencoder                ##
##   Este script se ha liberado bajo    ##
##    Licencia General Pública (GPL)    ##
##########################################

import os, sys, shutil, glob

# Averiguamos la versión de Python:
print ("Versión de Python: " + str(sys.version_info))

# Dependiendo de la versión de Python 
# importamos tkinter de una forma u otra.
if sys.version_info[:2] < (3,0):
	from Tkinter import *
	from tkFileDialog import *
elif sys.version_info[:2] >= (3,0):
	from tkinter import *
	from tkinter.filedialog import *

#from PIL import Image
#import Image

## Declaración de variables ##
returned_values = {}
returned_values['original'] = ""
returned_values['temporal'] = ""
directorio_origen = os.getcwd()
#directorio_temporal = os.environ["HOME"]
directorio_temporal = os.path.expanduser("~")

horizontal = 1920
vertical = 1080
nfps = 25
video = "video"
plataforma = sys.platform

## Declaración de funciones ##
	
## Redimensionamos las fotos
#def fredimensionar(origen, temporal, horizontal, vertical):
def fredimensionar(origen, temporal, horizontal, vertical, nfps, nombreVideo):
	#print origen
	#print destino
	#print horizontal
	#print vertical
	
	os.chdir(origen)
	#os.mkdir("original")
	#shutil.rmtree("original")
	

	# nos cambiamos al directorio de destino
	#os.chdir(temporal)
	
	
	#print 'listamos ficheros...'

	listaFicheros=os.listdir(origen)
	#print listaFicheros
	numeroFotos = len(glob.glob1(origen,"*.jpg"))
	if numeroFotos == 0:
		numeroFotos = len(glob.glob1(origen,"*.JPG"))
		extension = "JPG"
	else:
		extension = "jpg"
	if numeroFotos > 0:
		print ("Se han encontrado " + str(numeroFotos) + " de fotos.")
	else:
		print ("No hay fotos, no hay timelapse :-(")
		print ("Saliendo del programa.")
		#root.quit
		#salir()
	#'''
	
	#print 'Creamos un directorio temporal dentro del temporal'
	temporalTemporal = (temporal + "/temporal")
	if os.path.isdir(temporalTemporal) == False:
		os.mkdir(temporal + "/temporal")
	for foto in glob.glob1(origen,"*." + extension): # + glob.glob1(origen,"*.JPG"):
		print ("Redimensionando " + foto)
		numeroFotos = numeroFotos - 1
		print ("Faltan " + str(numeroFotos) + " fotos por redimensionar.")
		#comando = "convert -scale " + str(horizontal) + "x " + origen + "/" + foto + " " + temporal + "/temporal/" + foto
		copiaYredimensiona = "convert -scale " + str(horizontal) + "x" + str(vertical) + " " + origen + "/" + foto + " " + temporal + "/temporal/" + foto
		print (copiaYredimensiona)
		os.system(copiaYredimensiona)
		print ("")
	
	tmp = str(temporal)
	ext = str(extension)
	fps = str(nfps)
	nVideo = str(nombreVideo)
	crearVideo = "mencoder mf://"+tmp+"/temporal/*."+ext+" -mf fps="+fps+":type=jpg -ovc lavc  -lavcopts vcodec=ffvhuff  -o "+tmp+"/" + nVideo
	#mencoder mf://*.jpg -mf fps=8 w=800:h=600:fps=25:type=jpg -ovc lavc -o ./video.avi
	print (crearVideo)
	os.system(crearVideo)
	#mencoder mf://$directorio_destino/*.jpg -mf fps=$nfps:type=jpeg -ovc lavc -lavcopts vcodec=mjpeg -o $nombre_video.avi;
	print ("Video finalizado.")
	print ("Puede salir del programa.")
		
	#'''
	
	#if 
	#print "Borramos el directorio"
	#shutil.rmtree( temporal + "/temporal")
	
'''	
	# open an image file (.bmp,.jpg,.png,.gif) you have in the working folder
imageFile = "zFlowers.jpg"
im1 = Image.open(imageFile)
# adjust width and height to your needs
width = 500
height = 420
# use one of these filter options to resize the image
im2 = im1.resize((width, height), Image.NEAREST) # use nearest neighbour
im3 = im1.resize((width, height), Image.BILINEAR) # linear interpolation in a 2x2 environment
im4 = im1.resize((width, height), Image.BICUBIC) # cubic spline interpolation in a 4x4 environment
im5 = im1.resize((width, height), Image.ANTIALIAS) # best down-sizing filter

ext = ".jpg"
im2.save("NEAREST" + ext)
im3.save("BILINEAR" + ext)
im4.save("BICUBIC" + ext)
im5.save("ANTIALIAS" + ext)
region = im.crop(box)
'''

## Seleccionamos el directorio del que copiaremos las fotografías.
def fDirectorioOrigen():

	print ("Seleccione el directorio donde se encuentran las fotografías")
	# Preguntamos por el directorio.
	directorioOrigen=askdirectory()
	# Convertimos a string el resultado.
	origen = str(directorioOrigen)
	# Guardamos la variable de forma que podamos acceder a ella.
	returned_values['original'] = origen
	#print origen
	return origen

## Seleccionamos el directorio temporal donde copiaremos las fotografías
## y el archivo de video resultante.
def fDirectorioTemporal():

	print ("Seleccione un directorio temporal")
	# Preguntamos por el directorio
	directorioTemporal=askdirectory()
	# Convertimos a string el resultado
	temporal = str(directorioTemporal)
	# Guardamos la variable de forma que podamos acceder a ella.
	returned_values['temporal'] = temporal
	return directorioTemporal

## Averiguamos qué resolución ha escogido.  ##
## En caso de no escoger ninguna seleccionamos la resolución HD ##
def fResolucion():

	if resolucion.get() == 1:
		vertical = 1920
		horizontal = 1080
		nfps = 25
		#print "procediendo HD"
		
	elif resolucion.get() == 2:
		vertical = 768
		horizontal = 576
		nfps = 25
		#print "procediendo PAL"
		
	elif resolucion.get() == 3:
		vertical = 648
		horizontal = 486
		nfps = 30
		#print "procediendo NTSC"
		
	elif resolucion.get() == 4:
		vertical = 1920
		horizontal = 1080
		nfps = 25
		#provaProva = "ProvaProva" + varNombreVideo.get()
		#print "procediendo Resolución personalizada: " + provaProva
		
	else:
		vertical = 1920
		horizontal = 1080
		nfps = 25
		#print "procediendo 0"
	
	return (vertical,horizontal,nfps)

## Función que define el nombre del video resultante
def fNombreVideo():
	if varNombreVideo.get() == "":
		video = "video.avi"
	else:
		video = varNombreVideo.get() + ".avi"
	return video

#def f

## Función para cerrar la ventana y salir de la aplicación		
def salir():
	root.quit

def main():
	print ("")
	print ("procediendo...")
	fResolucion()
	H,V,F = fResolucion()
	# Si no se ha seleccionado ningún directorio de origen
	# el valor de returned_values['original'] = ""
	# así que le asignamos el valor del directorio personal del usuario.
	if returned_values['original']== "":
		#original = str(os.environ['HOME'])
		original = os.path.expanduser("~")
	else:
		original = str(returned_values['original'])
	print ("Directorio origen: " + original)
	
	
	# Si no se ha seleccionado ningún directorio temporal
	# el valor de returned_values['temporal'] = ""
	# así que le asignamos el valor del directorio personal del usuario.
	if returned_values['temporal']== "":
		#temporal = str(os.environ['HOME'])
		temporal = os.path.expanduser("~")
	else:
		temporal = str(returned_values['temporal'])
	print ("Directorio temporal: " + temporal)
	
	print ("Resolución horizontal: " + str(H))
	print ("Resolución vertical: " + str(V))
	print ("Número de fotogramas por segundo: " + str(F))
	video = fNombreVideo()
	print ("Nombre del video: " + video)
	#ejecutar = fredimensionar(original, temporal, H, V)
	ejecutar = fredimensionar(original, temporal, H, V, F, video)


		



root = Tk()
root.geometry("500x400") #tamaño de ventana
root.title("Timelapses4dummies") #titulo



## Creación del formulario:

# Directorio de origen de las fotografías
origen = Label(root, text="Directorio con las fotografías:")
origen.grid(sticky=E)

#Directorio temporal donde se copiarán para finalmente ser borradas.
destino = Label(root, text="Directorio donde se copiarán las imágenes,\n (que después se borrarán)\n y el video resultante.")
destino.grid(sticky=E)

#Cuadro de dialogo donde se escribirá el nombre del video resultante.
nombreVideo = Label(root, text="Nombre del video resultante:")
nombreVideo.grid(sticky=E)
varNombreVideo = StringVar()
textoNombreVideo = Entry(root, textvariable=varNombreVideo)

#textoNombreVideo = Entry(None, text="video")
textoNombreVideo.grid(row=2, column=1, padx=10, pady=10)

varOrigen = StringVar() 
origen = Button(root, text="Seleccionar carpeta origen", bg="cyan", activebackground="red",activeforeground="white", height=2, command=fDirectorioOrigen)
origen.grid(row=0, column=1, padx=10, pady=10)
 
temporal = Button(root, text="Seleccionar carpeta destino", bg="red", fg="white", height=2, command=fDirectorioTemporal)
temporal.grid(row=1, column=1, padx=10, pady=10)

resolucion = IntVar()
check1 = Radiobutton(root, text="HD 1920x1080x25fps", variable=resolucion, value=1, justify="left")
check2 = Radiobutton(root, text="PAL 768x576x25fps", variable=resolucion, value=2, justify="left")
check3 = Radiobutton(root, text="NTSC 648x486x30fps", variable=resolucion, value=3, justify="left")
check4 = Radiobutton(root, text="Personalizado", variable=resolucion, value=4, justify="left")
#cm = Button(root, text="Verificar", command=verificar, width=20)
check1.grid(row=3, column=1, padx=10, pady=1)
check2.grid(row=4, column=1, padx=10, pady=1)
check3.grid(row=5, column=1, padx=10, pady=1)
check4.grid(row=6, column=1, padx=10, pady=1)
#cm.grid()

salir = Button(root, text="Salir", bg="red", fg="white", height=2, command=root.quit)
#salir.grid(row=4, column=1)
salir.grid(sticky=E)

procesar = Button(root, text="Crear video", bg="green", fg="white", height=2, justify="left", command=main)
procesar.grid(row=7, column=1)
 
mainloop()
