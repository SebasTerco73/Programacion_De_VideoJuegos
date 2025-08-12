def mostrar_mapa(mapa):
    for fila in mapa:
        for columna in fila:
            if columna == "":
                columna = " "
            print(f'[{columna}]', end=" ")
        print()

def pos_actual(mapa):
    for indFila, eleFila in enumerate(mapa):
        for indCol, eleCol in enumerate(eleFila):
            if eleCol == "P":
                return indFila, indCol
    return None, None

def control_mapa(x,y,mapa):
    if not (0 <= x < len(mapa) and 0 <= y < len(mapa[x])):
        print("No puedes salir del mapa.")
        return False
    return True

def mover_jugador(mapa):
    filaJugador, colJugador = pos_actual(mapa)
    if filaJugador is None:
        print("Error, no se cargo al jugador")
        return False
    
    direccion = input('Mover (w/a/s/d)\n-> ').lower()

    if direccion == "w":
        nueva_fila, nueva_col = filaJugador - 1, colJugador
    elif direccion == "s":
        nueva_fila, nueva_col = filaJugador + 1, colJugador
    elif direccion == "a":
        nueva_fila, nueva_col = filaJugador, colJugador - 1
    elif direccion == "d":
        nueva_fila, nueva_col = filaJugador, colJugador + 1
    else:
        nueva_fila, nueva_col = filaJugador, colJugador
        print("Direccion incorrecta")
        return True

    permitir_movimiento = control_mapa(nueva_fila,nueva_col,mapa)    

    if permitir_movimiento:
        if mapa[nueva_fila][nueva_col] == "M":
            print('**************************************')
            print("* Saliste del laberinto, bien jugado *")
            print('**************************************')
            return False
        elif mapa[nueva_fila][nueva_col] == "E":
            print('************************************************')
            print("* Te encontraste con el enemigo, fin del juego *")
            print('************************************************')
            return False
        elif mapa[nueva_fila][nueva_col] == "":
            print("El jugador se movio con éxito")
            mapa[filaJugador][colJugador] = ""
            mapa[nueva_fila][nueva_col] = "P"
            return True
    else:
        return True

def main():
    mapa = [
    ['','','P','E'],
    ['','E','E',''],
    ['','','E',''],
    ['E','','','M']
    ]

    en_juego = True
    while en_juego:
        try:
            opc = int(input('***** MENU *****\n1. Ver Mapa\n2. Mover Jugador\n0. Salir\n-> '))
        except ValueError:
            opc = -1
        match opc:
            case 1: 
                mostrar_mapa(mapa)
                input('Enter para continuar ')
            case 2: 
                en_juego = mover_jugador(mapa)
                input('Enter para continuar ')
            case 0: 
                print('Finalizando....') 
                break
            case _:
                print('Opcion incorrecta')
                input('Enter para continuar ')
    
if __name__ == "__main__":
    main()