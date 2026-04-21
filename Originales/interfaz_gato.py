import pygame, sys
from pygame.locals import *

fondoX = pygame.Color(50,50,100)
fondoO = pygame.Color(100,50,50)

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = 0

    def draw(self,win,caracter=""):
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            if caracter=="X":
                text = font.render(self.text, 1, (45,164,215))
            elif caracter =="O":
                text = font.render(self.text, 1, (150,50,50))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

    def cancelar(self,win,caracter):
        self.text=caracter
        self.draw(win,caracter)

    def colorearMiniGato(y,x,caracter):
	if caracter=="X":
            colorFondo=(50,50,100)
        elif caracter =="O":
	    colorFondo=(100,50,50)

	for i in range(3):
	    for j in range(3):
		tablero[(y-1)*3+i][(x-1)*3+j].color=colorFondo
		tablero[(y-1)*3+i][(x-1)*3+j].draw(screen)


def crearScreen(screen):
    colorCeldas = pygame.Color(20,20,20)

    auxiliarx=2
    auxiliary=2
    separacionx=-85
    separaciony=-85

    tablero=[]

    for y in range(9):
        auxiliary+=1
        if auxiliary%3 == 0:
            separaciony+=10
        separaciony+=105
        tablero.append([])
        for x in range(9):
            auxiliarx+=1
            if auxiliarx%3 == 0:
                separacionx+=10
            separacionx+=105
            tablero[y].append(button(colorCeldas,separacionx,separaciony,95,95))
            tablero[y][x].draw(screen)
        separacionx = -85

    return tablero



pygame.init()
screen = pygame.display.set_mode((1000, 1000))
screen.fill(35,35,35)
pygame.display.set_caption("Miau de Miaus")
tablero=crearScreen(screen)

while 1:
    for evento in pygame.event.get():
        if evento.type==MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            for j in tablero:
                for i in j:
                    if i.isOver(pos)==True:
                        i.cancelar(screen,"X")

        if evento.type==QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
