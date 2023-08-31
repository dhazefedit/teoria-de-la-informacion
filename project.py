from PyPDF2 import PdfReader

archivo = 'D:/Teoria de la informacion 2023-B/GIT PROYECTO/teoria-de-la-informacion/entrega.pdf'

def fuente_de_informacion(ruta):
    reader = PdfReader(ruta)
    num_pages = len(reader.pages)
    listpag = []
    
    for x in range(num_pages):
        pag = reader.pages[x]
        listpag.append(pag.extract_text())
        #Nos quedamos con una sola pagina para hacer las pruebas
        if x == 1:
            #Dividimos el texto por palabras y cada palabra lo guardamos en un espacio de lista
            texto = listpag[x].split()
            return texto


def transmisor(paquetes):
    #Inicializamos una variable de tipo lista para ir guardando las palabras convertidas en binario
    paq = []
    for text in paquetes:
        #Cada palabra pasa por el proceso de binario y se deposita en un espacio de lista
        binary_text = ' '.join(format(ord(char), '08b') for char in text)
        paq.append(binary_text)

    return paq
    


def receptor(mensajes):
    #Llega el paquete y hay que codificar
    paq = []
    for text in mensajes:
        binary_list = text.split()
        #Porceso de decodificado
        cifrado = ''.join(chr(int(binary, 2)) for binary in binary_list)
        paq.append(cifrado)
    return paq

def destino_de_informacion(mensajes): 
    for x in mensajes:
        print(f'{x}\n ') 
    

def Inicializador(archivo):
    resultado = fuente_de_informacion(archivo)
    resultado2 = transmisor(resultado)
    resultado3 = receptor(resultado2)
    destino_de_informacion(resultado3)

Inicializador(archivo)