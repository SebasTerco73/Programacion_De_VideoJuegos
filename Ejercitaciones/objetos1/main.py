from Arma import Arma
from Personaje import Personaje
espada = Arma("Espada", 50)
daga = Arma("daga", 10)
pirata = Personaje("Pepe", 500, 40, espada)
#print(pirata)
pirata.almacenarArma(daga)
#print(pirata)
#pirata.atacar()
#pirata.getArma().atacarConArma(pirata.getFuerza())
pirata.atacarConArma()