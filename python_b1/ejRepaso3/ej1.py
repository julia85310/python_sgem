tablero = [['·', '·', '·'],['·', '·', '·'],['·', '·', '·']]
turnoJugador1 = True
jugando = True

def pedirCoordenadas():
    global jugando
    mostrarTablero()
    coordenada = [0, 0]
    try: 
        coordenada[0] = int(input('Introduce la fila: ')) - 1
        if(coordenada[0] < 0 or coordenada[0] > 2):
            raise Exception("")
        coordenada[1] = int(input('Introduce la columna: ')) - 1
        if(coordenada[1] < 0 or coordenada[1] > 2):
            raise Exception("")
        if coordenadaVacia(coordenada):
            return coordenada
        else:
            raise Exception("")
    except:
        jugando = False
        print(f"Trampa. Jugador {getJugador(True)} pierde. Jugador {getJugador(False)} gana")

def mostrarTablero():
    print('  1 2 3')
    for i in range(1,4):
        print(f'{i} {tablero[i-1][0]} {tablero[i-1][1]} {tablero[i-1][2]}')

def getJugador(esSuTurno):
    if esSuTurno and turnoJugador1 or (not esSuTurno and not turnoJugador1):
        return 1
    else:
        return 2
    
def coordenadaVacia(coordenada):
    if (tablero[coordenada[0]][coordenada[1]] == '·'):
        return True
    else:
        return False

def getFicha():
    if turnoJugador1:
        return 'O'
    else:
        return 'X'
    
def comprobarGanador(coordenada):
    hayFicha = True
    #comprobar esa fila
    for i in range (0,3):
        if (tablero[coordenada[0]][i] != getFicha()):
            hayFicha = False
            break
    if hayFicha:
        print(f'Fila completa. Gana Jugador {getJugador(True)}')
        return True
    
    #comprobar esa columna
    hayFicha = True
    for i in range (0,3):
        if (tablero[i][coordenada[1]] != getFicha()):
            hayFicha = False
            break
    if hayFicha:
        print(f'Columna completa. Gana Jugador {getJugador(True)}')
        return True
    
    #Comprobar diagonal 
    ficha = getFicha()
    if tablero[1][1] == ficha:
        if (tablero[0][0] == ficha and tablero[2][2] == ficha) or (tablero[2][0] == ficha and tablero[0][2] == ficha):
            print(f'Diagonal completa. Gana {getJugador(True)}')
            return True

    return False


def main():
    fichas = 0
    global tablero, jugando, turnoJugador1
    while(jugando):
        print(f'\tTurno del jugador {getJugador(True)}')
        coordenada = pedirCoordenadas()
        if jugando:
            tablero[coordenada[0]][coordenada[1]] = getFicha()
            fichas = fichas + 1
            if(fichas > 4):
                if comprobarGanador(coordenada):
                    jugando = False
                else:
                    if (fichas == 9):
                        jugando = False
                        print('Empate')
            turnoJugador1 =  not turnoJugador1


main()