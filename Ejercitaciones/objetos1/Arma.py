class Arma:
    def __init__(self, nombre, daño):
        self.__nombre = nombre
        self.__daño = daño
    
    def atacarConArma(self, daño):
        ataque = self.__daño + daño
        print(f"Ataque con arma: {ataque}")
    
    def setDaño(self, newDaño):
        self.__daño = newDaño

    def getDaño(self):
        return self.__daño
        
    def __str__(self):
        return f'Nombre: {self.__nombre}\nDaño:{self.__daño}'