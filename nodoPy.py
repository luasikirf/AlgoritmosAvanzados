import pygame
import sys
#tamaño pantalla
ancho= 800
alto = 800
pantalla = pygame.display.set_mode((ancho,alto))

#tamaño nodo
radio_nodo = 10

#lista nodos
nodos= []
centros = []
aristas = []
nodos_unir=[]


def iniciar():
    pygame.init()
    pantalla.fill((125,125,125))
    pygame.display.update()


def crear_nodo(posicion,color=(0,150,150)):
    global pantalla
    pygame.draw.circle(pantalla,#donde lo va a dibujar
                       color, #color del punto
                       posicion, #posicion
                       radio_nodo) #tamaño circulo
    #pygame.display.update()
    
def actualizar_pantalla():
    global centros, aristas
    pantalla.fill((125,125,125))
    for centro in centros:
        crear_nodo(centro)
    for a in aristas:
        arista([centros[a[0]],centros[a[1]]])
    pygame.display.update()
    
def arista(nodos):
    global pantalla, aristas
    pygame.draw.line(pantalla,#donde dibujar
                     (0,150,150),#color linea
                     nodos[0],#iniciar la linea
                     nodos[1],#terminar la linea
                     2)#grosor linea
    aristas.append((centros.index(nodos[0]),centros.index(nodos[1])))
    aristas = list(set(aristas))
    #print('como funciona el index',nodos[0])
    #pygame.display.update()
    
'''def resaltar_nodo(nodo,color):
    colores={'red':(255,0,0),'blue':(0,0,255),'default':(0,150,150)}
    for nodo in nodos:
        crear_nodo(nodo_seleccionado,colores[color])

def des_resaltar(nodos):
    for nodo in nodos:
        crear_nodo(nodo,(0,150,150))'''
    
def mover(nodo):
    index = centros.index(nodo)
    while pygame.mouse.get_pressed() == (0,0,1):
        try:
            centros[index] = pygame.mouse.get_pos()
            #nodo = centros.index(index)
            actualizar_pantalla()
            return True
        except:
            centros[index] = pygame.mouse.get_pos()
            nodo = pygame.mouse.get_pos()
            actualizar_pantalla()
            return True
    return True
    
def verificar_nodo(x,y):
    global nodos
    for posicion in nodos:
        if x >= posicion[0][0] and x <= posicion[0][1] and y >= posicion[1][0] and y <= posicion[1][1]:
            return (posicion[0][0]+10,posicion[1][0]+10)

iniciar()
condicion= True
while condicion == True:
    for evento in pygame.event.get():
        if pygame.event.event_name(evento.type) == 'Quit':#obtiene el texto del id que da "evento.type",y lo compara con quit
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed() == (1,0,0):
            x,y= pygame.mouse.get_pos()
            print(centros)
            if verificar_nodo(x,y):
                nodo_seleccionado=verificar_nodo(x,y)
                nodos_unir.append(nodo_seleccionado)
                #resaltar_nodo(nodo_seleccionado,"blue")
                #print(nodos_unir)
                #print(len(nodos_unir))
                if len(nodos_unir) == 2:
                    arista(nodos_unir)
                    pygame.display.update()
                    print(aristas)
                    #des_resaltar(nodos_unir)
                    nodos_unir = []
            else: #si el primer click es sobre un nodo, pero el segundo no, entra aqui
                crear_nodo([x,y])
                #print('posicion original nodo',x,y)
                nodos.append([[x-10,x+10],[y-10,y+10]])#del "centro" del nodo, tomamos radio = 10, para comprobar si se da click en esa zona
                centros.append((x,y))
                print(centros)
                pygame.display.update()
                try:
                    nodos_unir.pop() #como el segundo click no es sobre un nodo, borra el elemento de "nodos unir" si es que hay
                except:
                    None
        if pygame.mouse.get_pressed() == (0,0,1):
            x,y= pygame.mouse.get_pos()
            if verificar_nodo(x,y):
                centro_nodo_seleccionado=verificar_nodo(x,y)
                indice = centros.index(centro_nodo_seleccionado)
                centros[indice] = pygame.mouse.get_pos()
                nueva_x=centros[indice][0]
                nueva_y=centros[indice][1]
                nodos[indice] = [[x-10,x+10],[y-10,y+10]]
                actualizar_pantalla()
                #break
#print(evento.type)
    
    
    
    
