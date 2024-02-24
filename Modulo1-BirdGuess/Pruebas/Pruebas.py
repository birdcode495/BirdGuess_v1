import random


aves = [["Pato", 23], ["Colibri", 12], ["Flamingo", 34], ["Tucan", 17], ["Canario", 14], ["Avestruz", 79]]

#print(len(aves))


# -------------------- El estudiante debe pensar como crear las pantallas en las que el jugador debe adivinar el tamaño del ave dentro del elenco de especies
# -------------------- construido. Cada vez que el jugador adivine el tamaño de una especie el juego debe continuar, eliminando dentro de la lista la especie
# -------------------- cuyo tamaño ha sido adivinada por el jugador y ofreciendo al jugador una pantalla siguiente para adivinar el tamaño de otra especie 
# -------------------- dentro de la lista restante. ------------------------------------------------------------------------------------------------------





indice = random.randint(0, len(aves)-1)

secretSize = aves[indice][1]


print("Adivina el tamaño del ave que estoy pensando!!")

guess =  int(input("Ingresa el tamaño del ave: "))

intentos = 1

vidas = 4

acierto = False

puntos = 0



while acierto == False and vidas > 0:

	if guess != secretSize and intentos == 5 and vidas > 1:

		print("Lo has intentado 5 veces y no has podido adivinar el tamaño de esta ave. Perdiste una vida.")
		vidas = vidas - 1
		print("Ahora tienes: ", vidas, " vidas")
		indice = random.randint(0, len(aves)-1)
		secretSize = aves[indice][1]
		intentos = 0
		print("Adivina el tamaño del ave que estoy pensando!!")
		guess = int(input("Ingresa el tamaño del ave: "))
		intentos = intentos + 1

	elif guess != secretSize and intentos == 5 and vidas == 1:

		print("Ya no tienes vidas. Game over")
		vidas = vidas - 1
		break

	elif guess < secretSize:

		guess = int(input("Esta ave es mas grande que el valor que has ingresado. Intentalo de nuevo: "))
		intentos = intentos + 1

	elif guess > secretSize:

		guess = int(input("Esta ave es mas pequeña que el valor que has ingresado. Intentalo de nuevo: "))
		intentos = intentos + 1


	elif guess == secretSize and len(aves) > 1:

		print("Felicitaciones!!! Has adivinado el tamaño del ave que estaba pensando. Has ganado 10 puntos!!!")
		acierto = True
		puntos = puntos + 10
		print("Ahora tienes: ", puntos, " puntos")
		del aves[indice]
		indice = random.randint(0, len(aves)-1)
		secretSize = aves[indice][1]
		acierto = False
		print("Adivina el tamaño del ave que estoy pensando!!")
		intentos = 0
		guess =  int(input("Ingresa el tamaño del ave: "))
		intentos = intentos + 1


	elif guess == secretSize and len(aves) == 1:

		print("Felicitaciones!!! Has adivinado el tamaño del ave que estaba pensando. Has ganado 10 puntos!!!")
		acierto = True
		puntos = puntos + 10
		print("Ahora tienes: ", puntos, " puntos")
		del aves[0]
		print("Felicitaciones!!! Has adivinado todos los tamaños de las aves en la lista. Fin del juego")
		break








