# --------------------------------------------------------- Libraries importing ----------------------------------------------------------------------

from playsound import playsound

import time



# ---------------------------------------------------------------- BirdGuess --------------------------------------------------------------------------

print("BirdGuess: a serious game to guess the size of humingbird and falcon species that have been sighted in Cali and Bogotá - Colombia")

# ----------------------------------------------------------- Welcome to BirdGuess ------------------------------------------------------------------

# Topics to be discussed: function print(), data types in Python, operators, function input(), declaration of variables in Python ---



# --------------------------------------------------------------------------------- Data types in Python

# -------------------------------------------------- Numerical data

# ------------------------------- Integers

print()
print("5 is an integer")
print()
print("87 is an integer")
print()

# ------------------------------ Decimal numbers

print("9.8 is a decimal number")
print()
print("23.5 is a decimal number")
print()
print("This is a string data type")


# --------------------------------------------------------------------------------- Arithmetic operators

# ----------------------------- Addition

print()
print(5 + 4)
print()
print(24 + 34)

# ----------------------------- Substraction

print()
print(23 - 10)
print()
print(58 - 23)
print()

# ---------------------------- Multiplication

print(8 * 4)
print()

# --------------------------- Division

print(25 / 5)
print()

# -------------------------- Modulus

print(9 % 2)
print()
print(84 % 8)
print()

# ------------------------- Exponent

print(3 ** 3)
print()

# ------------------------ Floor division

print(9 // 2)
print()


# --------------------------------------------------------------------------- Comparison operators

# ----------------------- Equality operator

print(5 == 4)
print()
print(78 == 78)
print()

# ---------------------- Greater than

print(89 > 32)
print()
print(45 > 75)
print()

# --------------------- Different than

print(78 != 79)
print()
print(56 != 56)


# ----------------------------------------------------------------- Declaration of variables in Python

# -------------------- Our friend Uramitra

# -------------------- Nest weight is our variable

nest_weight = (2 * 3) + 0.3

print()

print("The weight of the nest before dinner is: ", nest_weight, " grams")

nest_weight = 9.1 + (2.05 * 3) + 0.3

print()
print("The weight of the nest after dinner is: ", nest_weight, " grams")


# -------------------------------------------------------------------- Function input()


# ----------------------------- Your name

print()

name = input("Enter your name: ")

print()
print("Welcome to BirdGuess: ", name)
print()

# ----------------------------- Your favorite bird

favorite_bird = input("Enter the name of your favorite bird: ")
print()
print("Your favorite bird is:", favorite_bird)


# ---------------------------- Your age

print()
age = int(input("How old are you? "))
print()
print("You are ", age, " years old")
print()

# --------------------------- Your weight


print()
weight = float(input("What is your weight in kilograms? "))
print()
print("Your weight is: ", weight, " kilograms")
print()


# ------------------------------------------------------------------------ Audio playing in Python

print("Now we are going to play an ambiental sound using Python")

print()

ambiental_sound = "Calzadito_cobrizo.wav"

time.sleep(5)

playsound(ambiental_sound)












