

# --------------------------------------------------------CLASSES CREATION IN BIRDCODE WITH PYTHON ---------------------------------------------------------



# -----------------------------------------------------------------DEFINITION OF CLASS BIRD -------------------------------------------------------------------


# ------------------------------------------------------------Definition of Bird Class properties and states --------------------------------------------------
# -----------------------------Each group of students must research about the birds properties and states and enrich this definition set ----------------------

class Bird():

	BodyTemperature = "warm-blooded"
	Phylum = "Chordata"
	Subphylum = "Vertebrata"
	Class = "Aves"
	EpidermalGrowth = "feathers"
	Tooth = "Thoothless"
	Reproduction = "oviparous"
	Eggshell = "hard"
	Metabolism = "high rate"
	Heart = "four-chambered"
	SkeletalSystem = "strong and lightweight"
	TemporalRange = "Late Cretacious - present"
	TemporalRange_Ma = 72
	Distribution = "worldwide"
	MinimunSize_cm = 5.5
	MaximunSize_cm = 280
	Forelimbs = "wings"
	Homology = True
	InEnglish = "birds"
	InSpanish = "aves"
	InFrench = "oiseaux"
	InGerman = "Vögel"
	InChinese = "鸟类"
	fly = False
	sing = False
	eat = False


# ---------------------------------------------- Definition of methods of the class Bird --------------------------------------------------------------------


	def TakeOff(self):
		self.fly = True


# --------------------------------------------- Creation of the first object which belongs to the class Bird ------------------------------------------------


AndeanEmerald = Bird()


# ---------------------------------------------------------- First printing of Bird class data --------------------------------------------------------------


print("The english name of the Class to which this bird belongs to is: ", AndeanEmerald.InEnglish)
print()
print("The chinese name of the Class to which this bird belongs to is: ", AndeanEmerald.InChinese)









