class Persona:
    es_humano = True

    def __init__(self,nombre,nivel=1,vida=100,experiencia=0):
        self.nombre = nombre
        self.nivel = nivel
        self.__vida = vida
        self.__experiencia = experiencia

    def get_vida(self):
        return self.__vida
    
    def set_vida(self, nueva_vida):
        if nueva_vida >= 0:
            self.__vida = max(0,self.__vida - nueva_vida)  # No permite negativos

    @property
    def experiencia(self):
        return self.__experiencia
    
    @experiencia.setter
    def experiencia(self, nueva_xp):
        self.__experiencia = nueva_xp

    def __str__(self):
        return f'{self.nombre} (Nivel {self.nivel}) - Vida: {self.__vida} - XP: {self.__experiencia}'
    
    def subir_nivel(self):
        self.nivel += 1
        self.experiencia += 10

    def estado(self):
        if self.__vida > 0:
            return 'vivo'
        else:
            return 'derrotado'
    
    def recibir_danio(self,valor):
        self.__vida = max(0,self.__vida - valor)
        return self.estado()
    
p = Persona('Sebas')
print(p)
p.subir_nivel()
print(p)
print(p.estado())
print(p.recibir_danio(50))
print(p)
print(p.recibir_danio(70))
print(f'{p.es_humano} - {p.experiencia} - {p.get_vida()}')
