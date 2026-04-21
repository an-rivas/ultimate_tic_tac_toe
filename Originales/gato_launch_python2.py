#"O" representa a la IA; "X" al jugador; 0 casilla vacia
#El jugador siempre empieza primero y es representado por -1 con turno
import copy

turno=1
hojas=[]
class Node:
    def __init__(self, padre, caracter, i, j, estado):
        if padre==None and caracter==None and i==None and j==None:
            self.estado=copy.deepcopy(estado)
        elif padre!=None:
            self.padre=padre
            self.estado=copy.deepcopy(padre.estado)
            self.caracter = caracter
            self.i = i
            self.j = j
            self.estado[i][j] = caracter
        elif estado!=None:
            self.estado=copy.deepcopy(estado)
            self.caracter = caracter
            self.i = i
            self.j = j
            self.estado[i][j] = caracter
        self.hijos=[]
        self.valor=False
def espaciosVacios(estado):
    espacios=[]
    for i in range(3):
        for j in range(3):
            if(estado[i][j]==0):
                espacios.append([i,j])
    return espacios

def verElFuturo(node, turno):
    tuplaEspacios=espaciosVacios(node.estado)
    if turno==1:
        caracter="O"
    else:
        caracter="X"
    turno=-turno
    for i in range(len(tuplaEspacios)):
        hijo=Node(node, caracter, tuplaEspacios[i][0], tuplaEspacios[i][1], None)
        gana=ganador(hijo.estado)
        if gana=="X":
            hijo.valor=-10
            hojas.append(hijo)
            node.hijos.append(hijo)
            return
        elif gana=="O":
            hijo.valor=10
            hojas.append(hijo)
            node.hijos.append(hijo)
            return
        elif len(tuplaEspacios)==0:
            hijo.valor=0
            hojas.append(hijo)
            node.hijos.append(hijo)
            return
        node.hijos.append(hijo)
        verElFuturo(hijo, turno)

def ganador(estado):
    gano=""
    for i in range(3):
        if estado[0][i]=="X" and estado[1][i]=="X" and estado[2][i]=="X":
            gano="X"
        elif estado[i][0]=="X" and estado[i][1]=="X" and estado[i][2]=="X":
            gano="X"
        elif estado[0][i]=="O" and estado[1][i]=="O" and estado[2][i]=="O":
            gano="O"
        elif estado[i][0]=="O" and estado[i][1]=="O" and estado[i][2]=="O":
            gano="O"
    if estado[0][0]=="X" and estado[1][1]=="X" and estado[2][2]=="X":
        gano="X"
    elif estado[0][0]=="O" and estado[1][1]=="O" and estado[2][2]=="O":
        gano="O"
    elif estado[0][2]=="X" and estado[1][1]=="X" and estado[2][0]=="X":
        gano="X"
    elif estado[0][2]=="O" and estado[1][1]=="O" and estado[2][0]=="O":
        gano="O"
    return gano

def evaluarNodos(padre, turno):
    if len(padre.hijos)==0:
        return
    if turno==-1:
        min=15
        for i in range(len(padre.hijos)):
            if padre.hijos[i].valor==False:
                evaluarNodos(padre.hijos[i],-turno)
            if padre.hijos[i].valor==-10:
                min=-10
                nodo_electo=padre.hijos[i]
                break
            if padre.hijos[i].valor<min:
                min=padre.hijos[i].valor
                nodo_electo=padre.hijos[i]
        padre.valor=min
    else:
        max=-15
        for i in range(len(padre.hijos)):
            if padre.hijos[i].valor==False:
                evaluarNodos(padre.hijos[i],-turno)
            if padre.hijos[i].valor==10:
                max=10
                nodo_electo=padre.hijos[i]
                break
            if padre.hijos[i].valor>max:
                max=padre.hijos[i].valor
                nodo_electo=padre.hijos[i]
        padre.valor=max
    return nodo_electo

def cuadrante(i, j):
    fila=int(i/3)
    columna=int(j/3)
    return fila, columna

def verificacion(meow, grid_i, grid_j, meowsote):
    mini_ganador=ganador(meow[grid_i][grid_j])
    verificar=False
    termino=False
    if len(espaciosVacios(meow[grid_i][grid_j]))==0:
        meowsote[grid_i][grid_j]="/"
        verificar=True
    else:
        if mini_ganador=="X":
            meowsote[grid_i][grid_j]="X"
            verificar = True
        elif mini_ganador=="O":
            meowsote[grid_i][grid_j]="O"
            verificar = True
    if verificar==True:
        ganador_total=ganador(meowsote)
        if ganador_total=="X":
            print "Gano el jugador"
            termino = True
        elif ganador_total=="O":
            print "Gano la Ai por que eres punetas"
            termino = True
        elif len(espaciosVacios(meowsote))==0:
            print "Tablas"
            termino=True
    return termino

meow=[[[[0 for i in range(3)] for j in range(3)] for k in range(3)] for m in range(3)]
meowsote=[[0,0,0],[0,0,0],[0,0,0]]
while True:
    jugada = raw_input("Introduzca las coordenadas para X separadas por espacio: ").split()
    jugada[0]=int(jugada[0])
    jugada[1]=int(jugada[1])
    grid_i, grid_j = cuadrante(jugada[0] - 1, jugada[1] - 1)
    meow[grid_i][grid_j][(jugada[0]-1)%3][(jugada[1]-1)%3]='X'
    termino=verificacion(meow, grid_i, grid_j, meowsote)
    if termino==True:
        break
    if meowsote[grid_i][grid_j]=='/':
        for i in range(3):
            for j in range(3):
                if meowsote[i][j]==0:
                    grid_i=i
                    grid_j=j
                    break
        Padre=Node(None,None,None,None,meow[grid_i][grid_j])
    elif meowsote[grid_i][grid_j]==0:
        Padre=Node(None,'X',(jugada[0]-1)%3, (jugada[1]-1)%3,meow[grid_i][grid_j])
    else:
        print "No puedes introducir una ficha ahi"
    verElFuturo(Padre,1)
    Nodo_electo=evaluarNodos(Padre,1)
    meow[grid_i][grid_j][Nodo_electo.i][Nodo_electo.j]='O'
    termino = verificacion(meow, grid_i, grid_j, meowsote)
    if termino == True:
        break
