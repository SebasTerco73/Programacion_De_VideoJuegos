from collections import Counter
import array 

# Ejercicios de Listas
def consigna1 ():
    enemigos = ['zombie','orco','dragón']
    enemigos.append('fantasma')
    enemigos.insert(1, 'golem')
    print(enemigos)

def consigna2():
    enemigos = ['zombie','orco','dragón','orco','zombie']
    enemigos_unicos = []
    print(Counter(enemigos))
    # enemigos_unicos_set = list(set(enemigos))
    for enemigo in enemigos:
        if enemigo not in enemigos_unicos:
            enemigos_unicos.append(enemigo)

    print(f"Enemigos sin repetir {enemigos_unicos}")
    print(f"Enemigos totales: {len(enemigos_unicos)}")


# Ejercicios de arrays
def consigna3():
    puntos = array.array('i',[10,20,30])
    puntos.insert(2,25)

    for p in puntos:
        print(f"[{p}]", end=" ")
    
def consigna4():
    vida = 50 
    danios = array.array('i',[10,5,15,0,20])
    print(f'Vida total: [{vida}]')
    for atk in danios:
        vida -= atk
        print(f'Ataque causo {atk} de daño', end=" - ")
        print(f'Vida restante: {vida}')

# Ejercicio de Diccionarios

def consigna5():
    jugador = {"nombre":"Mario", "vidas":3}
    jugador["nivel"] = 1
    jugador.update({'puntos':100,'arma':"espada"})

    #  diccionario trae la clave
    # .values() trae el valor
    # .items() trae clave valor
    for clave,valor in jugador.items():
        print(f'{clave}: {valor}')

def consigna6():
    jugadores = {
                    'Mario':{'vidas':3,'puntos':120},
                    'Luigi':{'vidas':2,'puntos':150},
                    'Peach':{'vidas':4,'puntos':90}
                }
    
    for clave,valor in jugadores.items():
        valor['puntos'] += 50
        if valor['vidas'] < 3:
            valor['vidas'] += 1
        print(f'Jugador {clave}\nVidas: {valor["vidas"]}\nPuntos: {valor["puntos"]}\n')


# Ejercicios combinados
#  
def hogwarts1():
    hechizos_basicos = ['lumos', 'alohomora', 'wingardium leviosa']
    eleccion = input('Que hechizo desea lanzar?\n-> ')
    print('Hechizo lanzado con éxito') if eleccion.lower() in hechizos_basicos else print('Ese hechizo no está aprendido aún')

def hogwarts2():
    alumnos = {'Harry':80,'Hermione':95,'Ron':60}
    for clave, valor in alumnos.items():
        if valor > 90:
            print(f'{clave}: Excelente')
        elif valor >= 70:
            print(f'{clave}: Muy bien')
        else:
            print(f'{clave}: Debe practicar más') 

def hogwarts3():
    alumno_puntaje = array.array('i',[70,85,60,90,75])
    contador =  sum(1 for puntaje in alumno_puntaje if puntaje > 80)
    print(f'Puntaje total: {sum(alumno_puntaje)}\nPromedio: {sum(alumno_puntaje)/len(alumno_puntaje)}\nNotas mayores a 80: {contador}')

def hogwarts4():
    estudiantes = {
                    'Sebas':{'hechizos_aprendidos':['wingardium leviosa','expecto patronum'],'puntos':250,'examenes':array.array('f',[5.5,4,5,6])},
                    'Harry':{'hechizos_aprendidos':['lumus','alohomora'],'puntos':273,'examenes':array.array('f',[9.5,8,8,7])},
                    'Hermione':{'hechizos_aprendidos':['wingardium leviosa','expecto patronum','lumus','alohomora'],'puntos':500,'examenes':array.array('f',[10,10,10,10])},
                    'Ron':{'hechizos_aprendidos':['lumos'],'puntos':2,'examenes':array.array('f',[2,4.5,3,1])},
                    'Draco':{'hechizos_aprendidos':['wingardium leviosa','expecto patronum','lumus','alohomora'],'puntos':300,'examenes':array.array('f',[9,9.5,8.5,9])},
                  }

    for nombre, datos in estudiantes.items():
        promedio = sum(datos['examenes'])/len(datos['examenes'])
        suficientes_hechizos = f'Aprendio mas de 3 ({len(datos["hechizos_aprendidos"])})' if len(datos['hechizos_aprendidos']) > 3 else f'Solo aprendio {len(datos["hechizos_aprendidos"])}'
        es_graduado = 'ES GRADUADO' if datos['puntos'] > 250 else 'NO ES GRADUADO'
        print(f'Alumno {nombre}\nPromedio: {promedio}\nHechizos: {suficientes_hechizos}\nPuntos: {datos["puntos"]}\n{es_graduado}\n')

hogwarts4()