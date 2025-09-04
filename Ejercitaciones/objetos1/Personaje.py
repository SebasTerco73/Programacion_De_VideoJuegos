class Personaje:
    def __init__(self, nombre, vida, fuerza, arma):
        self.__nombre = nombre
        self.__vida = vida
        self.__fuerza = fuerza
        self.__arma = arma
    
    def atacar(self):
        print(f"El personaje ataca con {self.__fuerza}")
    def almacenarArma(self, newArma):
        self.__arma = newArma
    def atacarConArma(self):
        dañoTotal = self.__fuerza + self.__arma.getDaño()
        print(f"Daño total de: {dañoTotal}")
    def getArma(self):
        return self.__arma
    def getFuerza(self):
        return self.__fuerza
    def __str__(self):
        return f'Pj nombre: {self.__nombre}\nVida: {self.__vida}\nFuerza: {self.__fuerza}\nArma: {self.__arma}'