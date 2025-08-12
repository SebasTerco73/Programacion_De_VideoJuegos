def agregarElemento(inventario):
    elemento = input("Ingrese el elemento a agregar al inventario:\n-> ").lower()
    inventario.append(elemento)
    print(f'{elemento} agregado con exito al inventario')
    input('Enter para continuar')

def eliminarElemento(inventario):
    elemento = input("Ingrese el elemento a eliminar del inventario:\n-> ").lower()
    if elemento in inventario:
        inventario.remove(elemento)
        print(f'{elemento} eliminado con exito al inventario')
    else: print(f'{elemento} no se encuentra en el inventario')
    input('Enter para continuar')

def mostrarInventario(inventario):
    if len(inventario) == 0:
        print('El inventario esta vacio')
    else:
        for e in inventario:
            print(f'[ {e} ] ')
    input('Enter para continuar')

def buscarElemento(inventario):
    elemento = input("Ingrese el elemento a buscar en el inventario:\n-> ").lower()
    if elemento in inventario: print(f'{elemento} se encuentra en el inventario')
    else: print(f'{elemento}  no encontrado en el inventario')
    input('Enter para continuar')

def funciones1():
    inventario = []
    while True:
        print('***** Menu del inventario *****')
        print('1. Agregar al inventario')
        print('2. Eliminar del inventario')
        print('3. Mostrar inventario')
        print('4. Buscar en el inventario')
        print('0. Salir')

        try:
            opcion = int(input("-> "))
        except ValueError:
            opcion = -1

        match opcion:
            case 1: agregarElemento(inventario)
            case 2: eliminarElemento(inventario)
            case 3: mostrarInventario(inventario)
            case 4: buscarElemento(inventario) 
            case 0: 
                print('Finalizando....') 
                break
            case _:
                print('Opcion incorrecta')
                input('Enter para continuar ')


# *********************************** EJERCICIO 2 **********************************************

def mostrarEnemigos(enemigos):
    if len(enemigos) == 0:
        print('Felicidades mataste a todos los enemigos')
    else:
        for clave, valor in enemigos.items():
            print(f'{clave}: [ Vida {valor["vida"]} ] - [ daño {valor["daño"]} ]')

def atacarEnemigo(enemigos):
    enemigo = input('Que enemigo deseas atacar?\n-> ').lower()
    if enemigo in enemigos:
        try:
            danio = int(input("Cuanto daño le queres causar?\n-> "))
        except ValueError:
            enemigos[enemigo]['vida'] = enemigos[enemigo]['vida'] + 50
            print(f'Falló el ataque, {enemigo} recupera 50 puntos de salud')
            return

        enemigos[enemigo]['vida'] = enemigos[enemigo]['vida'] - danio
        if enemigos[enemigo]['vida'] <= 0:
            enemigos.pop(enemigo)
            print(f'{enemigo} fue eliminado')
        else: print(f'Has herido a {enemigo}. Vida restante: {enemigos[enemigo]["vida"]}')
    else:
        print(f'{enemigo} no existe')

def funciones2():
    enemigos = {
        'orco':{'vida':100,'daño':50},
        'pirata':{'vida':60,'daño':30},
        'zombie':{'vida':30,'daño':80},
        'gargola':{'vida':100,'daño':50},
        'libertario':{'vida':10,'daño':5},
        'vampiro':{'vida':100,'daño':20}
    }
    
    while True:
        print('***** Acciones *****')
        print('1. Mostrar enemigos')
        print('2. Atacar enemigo')
        print('0. Salir')

        try:
            opcion = int(input("-> "))
        except ValueError:
            opcion = -1

        match opcion:
            case 1: mostrarEnemigos(enemigos)
            case 2: atacarEnemigo(enemigos)
            case 0: 
                print('Finalizando....') 
                break
            case _:
                print('Opcion incorrecta')
        input('Enter para continuar ')    


if __name__ == "__main__":
    # funciones1()
    funciones2()