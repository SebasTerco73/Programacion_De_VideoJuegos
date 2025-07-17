import random
def ejercicio1():
    for i in range(1,11):
        print(f"Paso {i}")

def ejercicio2():
    for i in range(5,0,-1):
        print(i)

def ejercicio3():
    pos = 0
    while(pos<=5):
        print(f"Posicion actual: {pos}")
        pos +=1

def ejercicio4():
    vidas = 3
    while(vidas > 0):
        print(f"Vida: {vidas}")
        vidas -=1
    
    print("Game Over")

def ejercicio5():
    password = "123456"
    login = False
    intentos = 3
    while(not login and intentos>0):
        entrada = input("Ingrese su contraseña\n=> ")
        if password == entrada:
            login = True
        else:
            intentos -=1
            print("Contraseña incorrecta")
    if login:
        print("Bienvenido")
    else:
        print("Se te acabaron los intentos")

def ejercicio6():
    aleatorio = random.randint(1,20)
    intentos = 5
    acierto = False
    while (intentos > 0):
        numero = int(input(f"Adivine el numero, intentos restantes {intentos}\n=> "))
        if numero == aleatorio:
            acierto = True
            break
        intentos -=1
        if intentos>1:
            if numero > aleatorio:
                print(f"Intente con un numero menor")
            elif numero < aleatorio:
                print(f"Intente con un numero mayor")
        
    print("Ganaste") if acierto else print(f"Incorrecto. Se te agotaron los intentos, el numero era {aleatorio}")


ejercicio6()