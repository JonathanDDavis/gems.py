import time
import random
import sys

locations = ["river", "mountain", "cave", "forest"]
riverLocations = ["river1", "river2"]
caveLocations = ["cave1", "cave2"]
mountainLocations = ["mountain1", "mountain2"]
forestLocations = ["forest1", "forest2"]

# define the gem location function
def gems():
	global gemsLocation
	gemsGeneralLocation = random.choice(locations).lower()
	if gemsGeneralLocation == "river":
		gemsLocation = random.choice(riverLocations).lower()
		print(gemsGeneralLocation)
		print(gemsLocation)
	elif gemsGeneralLocation == "mountain":
		gemsLocation = random.choice(mountainLocations).lower()
		print(gemsGeneralLocation)
		print(gemsLocation)
	elif gemsGeneralLocation == "cave":
		gemsLocation = random.choice(caveLocations).lower()
		print(gemsGeneralLocation)
		print(gemsLocation)
	elif gemsGeneralLocation == "forest":
		gemsLocation = random.choice(forestLocations).lower()
		print(gemsGeneralLocation)
		print(gemsLocation)
	else:
		print("check your code")

gems()
