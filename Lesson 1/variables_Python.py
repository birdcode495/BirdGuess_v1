
# ------------------------------ Práctica de declaración de variables en Python -------------------------------------------------


# ---------------------- Declaración de la variable de tamaño en centímetros del ave adulta Amazilia tzacatl (Rufous-tailed hummingbird)


bird_size = 10


# ----------------------- Declaración de la variable de peso del nido antes de la cena

#print(bird_size)

nest_weight = (0.7*3) + 0.1


# ----------------- Declaración de la variable de puntaje del jugador para la primera práctica o juego de adivinar el tamaño del ave en cm


score_1 = 0

score_2 = 0

# ------------------ Declaración de la variable que almacenará las respuestas del jugador para tratar de adivinar el número secreto

guess_bird = float(input("Enter the bird size value in centimeters: "))

# ----------------- Declaración de la variable que definirá la fase o "pantalla" de adivinanza del peso del nido antes y después 
# ----------------- de la cena en el segundo juego 

phase = "before" 




print()
print("----------------------------- Welcome to BirdGuess - A game to guess the size of the Colombian birds-------------------")
print()
print(" ---------- In this case you will try to guess the size of Amazilia tzacatl (Rufous-tailed hummingbird) in centimeters--------")


print()
print()



# Evaluar las respuestas dadas por el jugador


if guess_bird == bird_size:

	print("Congratulations!!! You have guessed the birds size")
	score_1 = score_1 + 50

elif guess_bird < bird_size:

	print("This bird is larger than the value you have entered")

elif guess_bird > bird_size:

	print("This bird is smaller than the value you have entered")













