# Code development practice in Python using the BirdCode and STEM methodologies

# Now, let's run this program



# ------------------------------------------------------------ Creation of graphical interface ------------------------------------------------------

# -----------------------------------------Temas tratados: Creación inicial de interfaz gráfica y reproducción de audio con Python ----------------------

from tkinter import *

import time

from playsound import playsound

playsound("welcome.mp3")

time.sleep(2)

playsound("hummingbird.mp3")

raiz=Tk()

raiz.title("Coppery-bellied Puffleg")

raiz.iconbitmap("BirdCode-logo.ico")

miFrame=Frame(raiz)

miFrame.pack()

miImagen=PhotoImage(file="EriocnemisCupreoventris.png")

Label(miFrame, image=miImagen).pack()

raiz.mainloop()


# ---------------------------------------------------------------- Welcome to BirdCode ---------------------------------------------------------------

# ----------------------------- Temas tratados: Función print(), función time.sleep(), función input() y reproducción de audio -----------------------



print()
print("BIRDCODE - A PROGRAM TO GUESS THE NAME OF AN ENDEMIC BIRD OF COLOMBIA")

print()
playsound("enter_name.mp3")
username = input("Please enter your name: ")

print()

print("Welcome to BirdCode ", username, ". Now we are going to learn how to create variables using new knowledge of colombian hummingbirds biodiversity")

print()

time.sleep(5)

playsound("endemic.mp3")

time.sleep(10)



# ------------------------------------------------------------- Declaration of variables ------------------------------------------------------------------

# -------------------------- Temas tratados: Declaración de variables en Python, tipos de datos y operadores aritméticos y de asignación ------------------



scientific_name = "Eriocnemis cupreoventris"

family = "Trochilidae"

bird_name = "Coppery-bellied Puffleg"

spanish_name = "Calzadito cobrizo"

french_name = "Érione à ventre cuivré"

german_name = "Kupferbauch-Schneehöschen"

chinese_bird_name = "铜腹毛腿蜂鸟"

pinyin = "Tóng fù máo tuǐ fēngniǎo"

feeding = "nectar"

habitat = "high Andean forest and paramo"

distribution = "almost endemic"

min_altitude_msnm = 1950

max_altitude_msnm = 3200

mean_altitude_msnm = (max_altitude_msnm + min_altitude_msnm) / 2

length_beak_mm = 18

conservacion = "Near Threatened" 

migration = False

size = 9.7


# -------------------------------------------------------- Bird Species Information Printing --------------------------------------------------------------

# ---------------------- Temas tratados: Potencialidad de la función print(), función time.sleep(), concatenación de cadenas de caracteres-----------------



print("The scientific name of this bird is: ", scientific_name)
print()
time.sleep(5)
print("The english name is this bird is: ", bird_name)
print()
time.sleep(5)
print("The spanish name of this bird is: ", spanish_name)
print()
time.sleep(5)
print("The french name of this bird is: ", french_name)
print()
time.sleep(5)
print("The german name of this bird is: ", german_name)
print()
time.sleep(5)
print("The chinese name of this bird is: ", chinese_bird_name, " and the pinyin (phonetic translation) is: ", pinyin)
print()
time.sleep(10)
print("The coppery-bellied puffleg feeds on: ", feeding)
print()
time.sleep(5)
print("This birds habitat is: ", habitat)
print()
time.sleep(5)
print("The distribution of this hummingbird is: ", distribution)
print()
time.sleep(5)
print("The minimun altitude where we can find this bird is: ", min_altitude_msnm, " msnm")
print()
time.sleep(5)
print("The maximun altitude where we can find this bird is: ", max_altitude_msnm, " msnm")
print()
time.sleep(5)
print("The mean altitude where this bird dwells is: ", mean_altitude_msnm, " msnm")
print()
time.sleep(5)
print("The birds beak length is: ", length_beak_mm, " mm")
print()
time.sleep(5)
print("The conservation state of this bird according to the IUCN is: ", conservacion)
print()
time.sleep(5)
print("The ", bird_name, " is an emblematic species of Colombia. Migration: ", migration)
print()
time.sleep(5)
print("The type of the object 'bird_name' is: ", type(bird_name))
print()
time.sleep(5)
print("The type of the object 'max_altitude_msnm' is: ", type(max_altitude_msnm))
print()
time.sleep(5)
print("The type of the object 'mean_altitude_msnm' is: ", type(mean_altitude_msnm))
print()
time.sleep(5)
print("The type of the object 'migration' is: ", type(migration))
time.sleep(5)
print()
print()


# -------------------------------------------- Game development "Guess the size of the bird in centimeters" ----------------------------------------------

# -------------------------------------- Temas tratados: Función input() o entrada de datos por consola, Condicionales y bucles --------------------------


playsound("try_guess.mp3")

match = False

while match == False:

	answer = float(input("Enter the size in cm you think the bird has: "))

	if answer < size:

		print("This bird is larger than the value you have entered. Try again.")
		playsound("larger.mp3")
		print()

	elif answer > size:

		print("This bird is smaller than the value you have entered. Try again.")
		playsound("smaller.mp3")
		print()

	else:

		print("Congratulations. You have guessed the birds size.")
		playsound("Congratulations.mp3")
		time.sleep(3)
		playsound("lets_listen_to_it.mp3")
		time.sleep(3)
		playsound("Calzadito_cobrizo.wav")
		time.sleep(2)
		playsound("End.mp3")
		print()
		match = True



# ------------------------------------------------------------------ End of the game ----------------------------------------------------------------------







