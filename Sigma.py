from sys import exit
import sys
import os
import random
import warnings
warnings.filterwarnings('ignore')


# global variables
weapon = 0 # weapon choice
bear = 0 # bear dead or not
bearRage = 0 # bear rage meter
dungeonKey = 0 # if you have dungeon key or not
bossKey = 0 # if you have boss key or not.
stone1 = 0
stone2 = 0
stone3 = 0
bow = 0
trapSet = 0
trapSet2 = 0
puzzle = [1, 2, 3]	
torch = 0
excali = 0
excaliW = 0
bRoom_exit = 0
ring_Chaos = 0
stalfos1 = 0
stalfos2 = 0
stalfos3 = 0
D_tablet = 0
deathCH = random.random() # chance of death, varies between weapons
esqCH = random.random() # chance to escape, varies between weapons
dungeon_room3_1_ligh = 0
paintingRoom = 0

def restart_program():
		python = sys.executable
		os.execl(python, python, * sys.argv)


def clear_scrn():
	"""Clears the interpreter screen."""
	os.system(['clear','cls'][os.name == 'nt'])

def reward_room():
	"""Function block for reward room."""
	
	print "Ah, you finally made it to the last room. Go ahead and open the chest"
	
	while True:
		next = raw_input("> ")
		
		if "open" in next:
			print "You open it and get the Ring of Chaos!"
			raw_input()
			outside()
		else:
			print "You really should open the chest. There is an important item inside."
		

def dead():
	"""Function block that runs when you die."""
	
	print "Game over."
	raw_input()
	exit(0)
					
		
def start():
	"""The beginning of the game."""
	print "Background:"
	print "The world in which this game takes place in is unlike Earth. It is governed by \nseveral different empires. The largest being Europa, an Empire of Men. The \ncurrent emperor is Galahad. The Order of the Black Dragons work for this empire."
	print "You are Sigma. One of the 24 members of the Order of the Black Dragons, lead \nby Omega. The purpose of this group is to maintain order and justice through \nany means necessary. One of the sayings of this group is \"The end justifies the \nmeans.\". You have just recently been recruited by this group."
	raw_input()
	print "\"Hello Sigma, I am Omega. Welcome to the Order of the Black Dragons. Well, \nlet's get down to business, you're a new recruit so I need to know where \nyou're at.\""
	raw_input()
	
	print "\"This is your task, mission, quest, whatever you want to call it. Beneath the \nMines of Azgoth, there is a diamond tablet. On the tablet is a prophecy, \nwritten in an ancient and forgotten tongue. I want you to get it and bring it\nback to me. Simple as that."
	print "The Mines have long been abondoned. Monsters and the undead lurk in it now. \nThe race of Nargols have been wiped out by something powerful down there. It \nmight still be there. So be careful and stay on your guard.\""
	raw_input()
	print "\"It's dangerous to go alone! Take one of these. You'll need it to slay all the \nmonsters on the way to the ring.\" Choose one of the following. \nA. Two-Handed Sword \nB. One-Handed Sword and Shield \nC. Dual wield swords \nD. Unarmed"
	
	# you choose your weapon
	while True:
		global weapon
		weapon = raw_input("> ")
	
		if weapon == 'A':
			print "You have chosen the Two-Handed Sword."
			print "You are equipped with the weapon of your choice and now ready to start your \nmission."
			raw_input()
			dungeon_start()
		elif weapon == 'B':
			print "You have chosen a Sword and Shield."
			print "You are equipped with the weapon of your choice and now ready to start your \nmission."
			raw_input()
			dungeon_start()
		elif weapon == 'C':
			print "You have chosen to dual wield swords."
			print "You are equipped with the weapon of your choice and now ready to start your \nmission."
			raw_input()
			dungeon_start()
		elif weapon == 'D':
			print "You have chosen to fight with your bare hands!"
			print "You are equipped with the weapon of your choice and now ready to start your \nmission."
			raw_input()
			dungeon_start()
		else:
			print "Please type the letter corresponding to which weapon you want."
			
			
def dungeon_start():
	"""This starts the dungeon."""
	print "You are at the entrance to the Mines."
	print "What do you want to do?"
	while True:
		next = raw_input("> ")
		
		if "enter" in next or "start" in next or "go" in next or "in" in next:
			dungeon_room1()
		else:
			print "I don't understand that."


def dungeon_room1():
	"""First room of dungeon. Filled with Spiderats."""
	print "You enter the Mines. There are a few Spiderats nested here. Do you want to kill \nthem or sneak past them?"
	
	# combat system
	while True:
		kill = raw_input("> ")
		if "kill" in kill and weapon == 'A':
			print "You charge at them like a barbarian. Your 2H-Sword is no match for the \nSpiderats. You are covered in Spiderat guts but at least you killed them all."
			raw_input()
			print "There are 3 doors. One to your left, one to your right, and one straight ahead."
			dungeon_room_main()
		elif "kill" in kill and weapon == 'B':
			print "You charge at them and start attacking. You block attacks with your shield and \nstab the Spiderats with your sword. Soon there are none left in the room."
			raw_input()
			print "There are 3 doors. One to your left, one to your right, and one straight ahead."
			dungeon_room_main()
		elif "kill" in kill and weapon == 'C':
			print "You charge and start hacking at the Spiderats. You're nothing but a whirlwind \nof blades. The Spiderats never knew what hit them. In less than a second you \nclear the room."
			raw_input()
			print "There are 3 doors. One to your left, one to your right, and one straight ahead."
			dungeon_room_main()
		elif "kill" in kill and weapon == 'D':
			print "You walk into the Spiderats' view and taunt. They charge at you. You throw a \ncouple of punches and start ripping their bodies to shreds with your bare hands.\nWhen you are done you start feasting upon their dead bodies. Fucking Alpha.\nOr should I say Sigma?"
			raw_input()
			print "There are 3 doors. One to your left, one to your right, and one straight ahead."
			dungeon_room_main()
		elif "sneak" in kill:
			print "You sneak past them succesfully."
			raw_input()
			print "There are 3 doors. One to your left, one to your right, and one straight ahead."
			dungeon_room_main()
		else:
			print "You got 2 choices. To kill them or sneak past them. Choose one."


def dungeon_room_main():
	"""Main room of the dungeon. Has 3 doors, each with different stuff."""
	# left is unlocked. right has boss key. middle is boss room.
	print "Which door do you enter?"
	while True:
		next = raw_input("> ")
		if "straight" in next or "front" in next or "ahead" in next:
			print "You enter the one in front of you."
			raw_input()
			print "There is nothing in the room but another door. You go up to the door but it is \nlocked. The markings on top says,"
			print "'[Boss Key] needed'"
			raw_input()
			if bossKey == 1: # bossKey indictator used here
				print "You use [Boss Key] to unlock the door. You go in the door."
				raw_input()
				print "You're find youself in a shaft, which is going down. As you keep on \ndescending the air becomes cooler. You see frost forming on the walls. The \nshaft has reached the bottom."
				raw_input()
				print "You open the door. You find yourself at spaceous cavern. There, sleeping right \nin front of you is the Malrog of Siddiq. To your left and right is a pedestal.\nIn opposite to you are 3 doors. The Malrog is blocking your exit."
				raw_input()
				
				boss_room()
			else:
				print "You go back."
				raw_input()
				dungeon_room_main()
		elif "right" in next:
			print "You go to the door on your right. But it's locked. The markings on top says,"
			print "'[Dungeon Key] needed'"
			raw_input()
			if dungeonKey == 1:
				print "You use [Dungeon Key] to unlock the door. You go in the door."
				raw_input()
				if torch == 0:
					print "The room smells like the dead. Probably some undead monsters lurking around. \nThere are a few pickaxes lying around and skeletons. One of the skeletons is \nunlike the others, it seems more recent and a different race than the others. \nNext to it is a piece of parchment. There are removable torches on the wall. \nOpposite to you is a trapdoor."
				else:
					print "There is a trapdoor at the other end."
				dungeon_room3()
			else:
				print "Guess you have to choose another door."
		elif "left" in next:
			print "You enter the door on your left."
			raw_input()
			if bear == 0:
				print "You see a couple of things. There is a skeleton with a sleeping bear next to it\nwhich seems to be blocking something. There is a painting on the wall opposite \nto the bear. Opposite to you is a stone tablet with some markings on it."
				dungeon_room2()
			else:
				print "You're back at the left door. There's a passageway next to a skeleton and dead \nbear, a painting, and a stone tablet."
				dungeon_room2()
		else:
			print "I don't understand that."


def dungeon_room2():
	"""Left door. Has some intersting stuff in it."""
	print "What do you do?"
	
	while True:
		next = raw_input("> ")
		
		if ("bear" in next or "skeleton" in next) and (bearRage == 0 or bearRage == 1):
			if bearRage == 0:
				print "The bear wakes up and starts clawing at you. You're too weak so you flee."
				raw_input()
				print "You're back at the crossroad."
				global bearRage
				bearRage = 1
				dungeon_room_main()
			else:
				print "The bear has awoken again. This time he didn't let you go. You die a stupid \ndeath. Should have learned the first time."
				raw_input()
				dead()
		elif ("shoot" in next or "bear" in next or "bow" in next) and bow == 1:
			if bear == 0:
				print "You shoot the bear with your bow. You land a headshot which kills the bear."
				global bear
				bear = 1
				raw_input()
				print "There seems to be a passageway where the bear was. You go in it."
				raw_input()
				print "You are at the other end of the passageway."
				print "There is a key at the opposite wall. But it looks like a trap. At your right is \nsome sort of mechanical machine."
				dungeon_room2_1()
			else:
				print "The bear is dead and will stay dead."
		elif ("passageway" in next) and not (bear == 0):
			print "You go through the passageway."
			raw_input()
			print "There is a key at the opposite wall. But it looks like a trap. At your right is \nsome sort of mechanical machine."
			dungeon_room2_1()
		elif "tablet" in next or "markings" in next:
			print "You read, 'We, the miners of Azgoth, have awoken an ancient evil of this world. \nIt is a creature of Siddiq, a creature of shadow and ice. The Malrog of Siddiq.\nOnly a warrior wielding the Excalibur can defeat it. I am with the last \nremaining miners in this place. Death is near.'"
			raw_input()
			print "What do you do now?"
		elif "painting" in next:
			if paintingRoom == 0:
				print "You go to the painting. It's a painting of a Nargol, the race that mined this \nplace. You touch it."
				raw_input()
				dungeon_room2_painting()
			else:
				print "There's nothing left in the room for you to do."
		elif "back" in next or "return" in next or "leave" in next or "exit" in next:
			print "You go back to the main room."
			dungeon_room_main()
		else:
			print "I don't understand that."


def dungeon_room2_painting():
	"""Painting room. Has a chest with [Bow]"""
	print "You are warped to another room. There isn't much in the room but a chest."
	print "What do you do?"
	
	while True:
		next = raw_input("> ")
		
		if "chest" in next:
			print "You open the chest and recieve a [Bow] and a [Quiver] with 24 [Arrows]."
			global bow
			global bearRage
			global paintingRoom
			bow = 1
			bearRage = 2
			paintingRoom = 1
			raw_input()
			print "You are magically warped back to the previous room."
			raw_input()
			dungeon_room2()
		elif "back" in next or "return" in next or "leave" in next or "exit" in next:
			print "There is no way to go back."
		else:
			print "I don't understand that."


def dungeon_room2_1():
	"""Function block for the passageway blocked by bear."""
	print "What do you do?"
	
	while True:
		next = raw_input("> ")
		
		if "key" in next and trapSet == 0:
			print "You go get the key and die. It was a trap moron."
			raw_input()
			dead()
		elif "key" in next and trapSet == 1 and dungeonKey == 0:
			print "You have recieved [Dungeon Key]!"
			print "You can now unlock locked normal doors."
			raw_input()
			global dungeonKey
			dungeonKey = 1
			dungeon_room2_1()
		elif "key" in next and dungeonKey == 1:
			print "You already got the key."
		elif "machine" in next or "right" in next:
			if trapSet == 0:
				print "You go check out the machine."
				raw_input()
				dungeon_room2_1_mach()
			else:
				print "You already activated the machine."
		elif "back" in next or "return" in next or "leave" in next or "exit" in next:
			print "You go back to Dungeon Room 1."
			raw_input()
			dungeon_room2()
		else:
			print "I don't understand that."
						
def dungeon_room2_1_mach():
	print "There are some characters with numbers printed on the machine. \nThere is also a numberpad with corresponding number blocks."
	print "It appears to be some sort of puzzle. Maybe it'll disarm the trap."
	raw_input()
	print "It can only run one time, then it'll blow up. Make sure you're sure."
	raw_input()
	print "'| A3 | B3 | C1 | D2 | E4 | F3 | G2 | H_ |'"
	print "What is the missing number?"
	print "| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |"
			
	while True:
		next = raw_input("> ")
		if next.isdigit():
			puzNum = int(next)
			if puzNum == 3:
				print "The gears start shifting and something clicks. The trap has been disarmed."
				global trapSet
				trapSet = 1
				raw_input()
				dungeon_room2_1()
			else:
				print "The machine beeps and start steaming. It blows up and you die."
				raw_input()
				dead()

		else:
			print "Numbers only."
			

def dungeon_room3():
	print "What do you do?"
	
	while True:
		next = raw_input("> ")
		
		if "parchment" in next:
			print "You go pick up the parchment paper and read it."
			raw_input()
			print "'We were betrayed. The attack came at midnight, lead by the man with the silver \nand gold eyes. We had befriended him and believed he was good. But good he was \nnot. He was seeking an ancient treasure, the Ring of Chaos. When he learned \nabout it's wherabouts in the Mines, he tried to take the ring. But was stopped \nby the demon we had awoken. The man, he wasn't Human. No, he was a Hezboth, the \nextinct brother race of Humans. The lost snow-dwellers.'"
			raw_input()
			print "You put the parchment back on floor. What do you do now?"
		elif "torch" in next and not torch == 1:
			print "You place a [Torch] in your inventory."
			global torch
			torch = 1
			raw_input()
			print "You are suddendly attacked by one of the skeletons. It has a pickaxe as a \nweapon. Do you attack it, go back, or make a dash for the trapdoor?"
			
			while True:
				next = raw_input("> ")
				if "attack" in next and weapon == 'A':
					print "You attack the skeleton."
					raw_input()
					if deathCH >= 1.0 / 10.0:
						print "You thrust your 2H-sword at the skeleton. You break through hs pickaxe and \nshatter him to pieces."
						raw_input()
						dungeon_room3()
					else:
						if esqCH >= 9.0 / 10.0:
							print "The skeleton has overpowered you. But you barely make it to the next room. \nYou are tired."
							raw_input()
							dungeon_room3_1()
						else:
							print "The skeleton has overpowered you. You are too slow to escape and die at the \nhands of a skeleton."
							raw_input()
							dead()
				elif "attack" in next and weapon == 'B':
					print "You attack the skeleton."
					raw_input()
					if deathCH >= 2.0 / 10.0:
						print "You block the pickaxe swing by the skeleton with your shield. You then thrust \nyour sword and destroy the skeleton."
						raw_input()
						dungeon_room3()
					else:
						if esqCH >= 2.0 / 10.0:
							print "The block the first swing of the pickaxe but it knocks you back. The skeleton \nswings again and hits you. You barely make it to the next room. You are wounded."
							raw_input()
							dungeon_room3_1()
						else:
							print "The skeleton overpowered you. You are knocked down to the floor and can't get \nup. The skeleton swings it's pickaxe and breaks your skull. You die."
							raw_input()
							dead()
				elif "attack" in next and weapon == 'C':
					print "You attack the skeleton."
					raw_input()
					if deathCH >= 4.0 / 10.0:
						print "In a flurry of movements the skeleton is nothing but pieces. Your dual swords \nare no match for a pickaxe!"
						raw_input()
						dungeon_room3()
					else:
						print "The skeleton overpowered you. But you barely \nmake it to the next room."
						raw_input()
						dungeon_room3_1()
				elif "attack" in next and weapon == 'D':
					print "You launch yourself at the skeleton and start throwing punches."
					raw_input()
					print "You dodge the pickaxe swings and rip it's skull out. Then you proceed to bash \nthe skeleton with it's skull. In a few seconds it's nothing but a pile of \nbroken bones."
					raw_input()
					dungeon_room3()
				elif "trapdoor" in next or "dash" in next:
					print "You dodge the skeleton and make a dash for the door. You barely make it."
					raw_input()
					dungeon_room3_1()
				elif "back" in next:
					print "You dodge the skeleton and run back to the main room."
					raw_input()
					dungeon_room_main()
				else:
					print "I don't understand that."
		elif "torch" in next and torch == 1:
			print "You already have a torch."
		elif "trapdoor" in next:
			if bossKey == 0 and dungeon_room3_1_ligh == 0:
				print "You enter the trapdoor."
				raw_input()
				dungeon_room3_1()
			elif bossKey == 0 and not dungeon_room3_1_ligh == 0:
				print "You enter the trapdoor."
				raw_input()
				dungeon_room3_1_light()
			else:
				print "You already got everything from here."
		elif "miner" in next or "miners" in next:
			print "They're just a bunch of dead miners. Nothing interesting."
		elif "back" in next or "return" in next or "leave" in next or "exit" in next:
			print "You go back to the main room."
			raw_input()
			dungeon_room_main()
		else:
			print "I don't understand that."


def dungeon_room3_1():
	print "It's really dark in here. You can't see anything! It's too dark to do anything!"
	raw_input()
	print "What do you do?"
	while True:
		next = raw_input("> ")
		
		if ("torch" in next or "light" in next) and torch == 0:
			print "You don't have a [Torch] or any other source of light."
		elif ("torch" in next or "light" in next) and torch == 1:
			print "You take out the [Torch] and now able to see."
			raw_input()
			dungeon_room3_1_light()
		elif "back" in next or "return" in next or "leave" in next or "exit" in next:
			print "You go back up to Dungeon Room 2."
			raw_input()
			dungeon_room3()
		else:
			print "I don't understand that."


def dungeon_room3_1_light():
	if dungeon_room3_1_ligh == 0:
		print "You see several things. For one, the ladder back up is gone. There's also an \nangry bear in the room that you just woke up. There's also a chest behind the \nbear."
		raw_input()
		print "You're still too weak to fight a bear. What do you do?"
	else:
		print "What do you do?"
	
	while True:
		next = raw_input("> ")
		
		if ("torch" in next or "light" in next) and dungeon_room3_1_ligh == 0:
			print "You throw the torch at the bear. It goes up in flames and lights up the room \neven more. Good job! You killed the bear."
			global dungeon_room3_1_ligh
			dungeon_room3_1_ligh = 1
			raw_input()
			print "The ladder back up has appeared again."
			raw_input()
			print "With the added light by the bear you see another trapdoor near the chest."
			print "What do you do now?"
			
			while True:
				next = raw_input("> ")
				
				if "chest" in next and excali == 0:
					print "You have recieved an [Excalibur]!"
					print "This is the legendary 3-pronged, 2H weapon of Nargols, has many uses but it's \ntoo heavy for you to actually fight with it."
					global excali
					excali = 1
					raw_input()
					print "What do you do?"
				elif "chest" in next and not excali == 0:
					print "You already checked the chest."
				elif "trapdoor" in next and not excali == 0:
					print "You go through the trapdoor."
					raw_input()
					print "You see a key on the wall opposite to you. On your right there's an even \nbigger machine. The key has a trap on it."
					raw_input()
					dungeon_room3_2()
				elif "trapdoor" in next and excali == 0:
					print "You should check the chest first."
				elif ("back" in next or "return" in next or "leave" in next or "exit" in next) and not excali == 0:
					print "You go up the ladder."
					raw_input()
					dungeon_room3()
				elif ("back" in next or "return" in next or "leave" in next or "exit" in next) and excali == 0:
					print "You should really check the chest."
				else:
					print "I don't understand that."
		elif "trapdoor" in next and not dungeon_room3_1_ligh == 0:
			print "You go through the trapdoor."
			raw_input()
			print "You see a key on the wall opposite to you. On your right there's an even \nbigger machine. The key has a trap on it."
			raw_input()
			dungeon_room3_2()					
		elif ("attack" in next) and not ("torch" in next or "light" in next) and dungeon_room3_1_ligh == 0:
			print "You're too weak to fight it!"
		elif "chest" in next and dungeon_room3_1_ligh == 0:
			print "The bear is in the way!"
		elif ("back" in next or "return" in next or "leave" in next or "exit" in next) and dungeon_room3_1_ligh == 0:
			print "The ladder is gone!"
		elif ("back" in next or "return" in next or "leave" in next or "exit" in next) and not dungeon_room3_1_ligh == 0:
			print "You go back to Dungeon Room 2."
			raw_input()
			dungeon_room3()
		else:
			print "I don't understand that."
	

def dungeon_room3_2():
	print "What do you do?"
	
	while True:
		next = raw_input("> ")
		
		if "key" in next:
			if trapSet2 == 0 and bossKey == 0:
				print "You go get the key. The trap activates. You die. It was a trap moron."
				raw_input()
				dead()
			elif bossKey == 1:
				print "You already have the key."
			else:
				print "You have recieved [Boss Key]!"
				print "You can now unlock the boss room and complete the dungeon!"
				raw_input()
				global bossKey
				bossKey = 1
				dungeon_room3_2()
				
		elif "machine" in next:
			if trapSet2 == 0:
				print "You go check out the huge machine."
				raw_input()
				dungeon_room3_2_mach()
			else:
				print "You already activated the machine."
		elif "back" in next or "return" in next or "leave" in next or "exit" in next:
			print "You go back to the room with the lit bear."
			raw_input()
			dungeon_room3_1_light()
		else:
			print "I don't understand that."


def dungeon_room3_2_mach():
	print "It is similar to the other machine you came across, complete with a numpad. \nBut it has 3 different parts. You will need to solve 3 different puzzles in \norder to disarm the trap."
	raw_input()
	print "The machine will blow up at the first mistake, so make sure you're sure."
	raw_input()
	print "First puzzle:"
	print "1, 1, 2, 3, 5, 8, 13, 21, 34, 55,..."
	print "What number is in the 20th place of the sequence?"
	print "| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |"
	
	while True:
		next = raw_input("> ")
		
		if next.isdigit():
			if int(next) == 6765:
				print "The gears on the machine shifts and something clicks. You have unlocked this \npart."
				raw_input()
				dungeon_room3_2_mach2()
			else:
				print "The machine beeps and starts steaming. It blows up and you die."
				raw_input()
				dead()
		else:
			print "Numbers only."


def dungeon_room3_2_mach2():
	print "With the first part completed you go on to the next puzzle."
	print "The next puzzle has 4 triangles with numbers at the verteces and in the middle."
	raw_input()
	print "7------5    2------3    8------6    5------9"
	print " \ 26 /      \  5 /      \ 44 /      \  ? /"
	print "  \  /        \  /        \  /        \  /"
	print "   \/          \/          \/          \/"
	print "    3          1           2            4"
			     
	print "What number goes in the 4th triangle?"
	print "| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |"
	
	while True:
		next = raw_input("> ")
		
		if next.isdigit():
			if int(next) == 29:
				print "The gears on the machine shifts and something clicks. You solved this part of \nthe machine."
				raw_input()
				dungeon_room3_2_mach3()
			else:
				print "The machine beeps and starts steaming. It blows up and you die."
				raw_input()
				dead()
		else:
			print "Numbers only."


def dungeon_room3_2_mach3():
	print "With the first 2 parts completed, you go on to the next and last puzzle."
	print "This is similar to the first puzzle you did on the other machine."
	raw_input()
	print "| A5 | B2 | C1 | D1 | E6 | F5 | G3 | H_ |"
	print "What is the missing number?"
	print "| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |"
	
	while True:
		next = raw_input("> ")
		
		if next.isdigit():
			if int(next) == 6:
				print "The gears on the machine shifts and something clicks. You solved the last part \nof the machine."
				raw_input()
				print "You have solved all 3 parts of the machine! The trap has now been disarmed."
				raw_input()
				global trapSet2
				trapSet2 = 1
				dungeon_room3_2()
			else:
				print "The machine beeps and starts steaming. It blows up and you die."
				raw_input()
				dead()
		else:
			print "Numbers only."
			
def boss_room():
	print "What do you do?"
	
	while True:
		next = raw_input("> ")
		
		if "attack" in next or "malrog" in next or "Malrog" in next:
			print "You can't do that. The Malrog will wake up and kill you."
		elif "right" in next:
			print "You go check out the pedestal on the right."
			raw_input()
			boss_room_Rped()
		elif "left" in next:
			print "You go check out the pedestal on the left."
			raw_input()
			boss_room_Lped()
		elif "pedestal" in next and not "left" in next and not "right" in next:
			print "Which pedestal?"
		elif "doors" in next or "door" in next:
			print "You silently creep toward the doors."
			raw_input()
			print "You are at the other side."
			boss_room_doors()
		elif "Excalibur" in next or "excalibur" in next:
			print "You're too weak to use the Excalibur in a fight."
		elif "torch" in next:
			print "A single torch is useless against the Malrog."
		elif "back" in next or "return" in next or "leave" in next or "exit" in next:
			print "The Malrog is blocking the exit and the shaft only goes down."
		else:
			print "I don't understand that."


def boss_room_Rped():
	print "On the pedestal is a tablet. Not a stone tablet. But a tablet made out of \ndiamonds. It's written in some language that you cannot read."
	raw_input()
	print "The tablet is locked into place and does not look like you could get it out. \nThere is a big key slot next to the pedestal. A perfect fit for the Excalibur."
	raw_input()
	if ring_Chaos == 0:
		print "Since you can't really lift the Excalibur you'll have to do something else."
		boss_room()
	else:
		print "You insert the Excalibur in the slot. You hear something click."
		print "You have recieved the [Diamond Tablet]!"
		global D_tablet
		D_tablet = 1
		raw_input()
		print "Now turn this in to Omega."
		raw_input()
		boss_room_fight()

def boss_room_Lped():
	print "On the pedestal is a locked case. There are 3 notches on the case. Inside the \ncase seems to be some sort of ring."
	raw_input()
	if stone1 == 1 and stone2 == 1 and stone3 == 1:
		print "You put the 3 stones in their corresponding notches. The case is unlocked. You \nhave recieved the [Ring of Chaos]!"
		raw_input()
		print "Do you want to equip it? (Y/n)"
		while True:
			next = raw_input("> ")
			
			if "Y" in next or "y" in next:
				print "You equip the ring. A red aura start emanating from you. The ruby red jewel on \nthe ring starts glowing."
				global ring_Chaos
				ring_Chaos = 1
				raw_input()
				print "The ring has buffed you. You are now stronger. You are now faster. You have \nthe strength to wield the Excalibur."
				raw_input()
				print "But, as a result of wearing a Ring of Power you will have to stay true to it's \nname. You will only be able to spread chaos and destruction with this."
				raw_input()
				boss_room_fight()
			elif "N" in next or "n" in next:
				print "You really should think about using it."
			else:
				print "Please type 'Y' or 'n'"
	else:
		print "You don't have all 3 stones to unlock the case."
		raw_input()
		boss_room()

	
def boss_room_doors():
	print "Which door do you enter? Left, right, in front, or none?"
	
	while True:
		next = raw_input("> ")
		
		if "left" in next:
			print "You enter the door on your left."
			raw_input()
			print "There is a stone on the opposite wall. Guarding it is a Stalfos, a skeleton \nwarrior."
			boss_room_Lrm()
		elif "right" in next:
			print "You enter the door on your right."
			raw_input()
			print "There is a stone on the opposite wall. Guarding it is a Stalfos, a \nskeleton warrior."
			boss_room_Rrm()
		elif "front" in next:
			print "You enter the door in front of you."
			raw_input()
			print "There is a stone on the opposite wall. Guarding it is a Stalfos, a \nskeleton warrior."
			boss_room_Frm()
		elif "none" in next:
			print "You don't go in any doors."
			raw_input()
			boss_room()
		else:
			print "I don't understand that."


def boss_room_Lrm():
	print "What do you do?"
	
	while True:
		next = raw_input("> ")
		
		if "stone" in next:
			if stalfos1 == 0:
				print "The Stalfos is guarding it. Try to get rid of him."
			elif stalfos1 == 1 and stone1 == 0:
				print "You got the stone."
				global stone1
				stone1 = 1
				raw_input()
				boss_room_Lrm()
			else:
				print "You already have the stone."
		elif "attack" in next or "stalfos" in next or "Stalfos" in next:
			if stalfos1 == 0:
				print "You go attack the Stalfos."
				raw_input()
				print "The Stalfos has been defeated! You can now get the stone."
				global stalfos1
				stalfos1 =  1
				raw_input()
				boss_room_Lrm()
			else:
				print "The Stalfos is gone now."
		elif "back" in next or "return" in next or "leave" in next or "exit" in next:
			print "You go back to the previous room."
			raw_input()
			boss_room_doors()
		else:
			print "I don't understand that."


def boss_room_Rrm():
	print "What do you do?"
	
	while True:
		next = raw_input("> ")
		
		if "stone" in next:
			if stalfos2 == 0:
				print "The Stalfos is guarding it. Try to get rid of him."
			elif stalfos2 == 1 and stone2 == 0:
				print "You got the stone."
				global stone2
				stone2 = 1
				raw_input()
				boss_room_Rrm()
			else:
				print "You already have the stone."
		elif "attack" in next or "stalfos" in next or "Stalfos" in next:
			if stalfos2 == 0:
				print "You go attack the Stalfos."
				raw_input()
				print "The Stalfos has been defeated! You can now get the stone."
				global stalfos2
				stalfos2 =  1
				raw_input()
				boss_room_Rrm()
			else:
				print "The Stalfos is gone now."
		elif "back" in next or "return" in next or "leave" in next or "exit" in next:
			print "You go back to the previous room."
			raw_input()
			boss_room_doors()
		else:
			print "I don't understand that."


def boss_room_Frm():
	print "What do you do?"
	
	while True:
		next = raw_input("> ")
		
		if "stone" in next:
			if stalfos3 == 0:
				print "The Stalfos is guarding it. Try to get rid of him."
			elif stalfos3 == 1 and stone3 == 0:
				print "You got the stone."
				global stone3
				stone3 = 1
				raw_input()
				boss_room_Frm()
			else:
				print "You already have the stone."
		elif "attack" in next or "stalfos" in next or "Stalfos" in next:
			if stalfos3 == 0:
				print "You go attack the Stalfos."
				raw_input()
				print "The Stalfos has been defeated! You can now get the stone."
				global stalfos3
				stalfos3 =  1
				raw_input()
				boss_room_Frm()
			else:
				print "The Stalfos is gone now."
		elif "back" in next or "return" in next or "leave" in next or "exit" in next:
			print "You go back to the previous room."
			raw_input()
			boss_room_doors()
		else:
			print "I don't understand that."


def boss_room_fight():
	print "What do you do?"
	
	while True:
		next = raw_input("> ")
		
		if "attack" in next or "Malrog" in next or "malrog" in next:
			if bRoom_exit == 0:
				if excaliW == 0:
					print "You should wield the Excalibur first."
				else:
					print "You attack the Malrog with the Excalibur."
					raw_input()
					print "The red aura around you gets stronger. Your eyes also start glowing red. The \nMalrog's icy blue eyes flick open. But it's too late as you pierce the Malrog \nwith the Excalibur. A red stream of light emits from withing the Malrog and \nit turns to dust. You have slain the Malrog of Siddiq."
					global bRoom_exit
					bRoom_exit = 1
					raw_input()
					boss_room_fight()
			else:
				print "You already slew the Malrog."
		elif "Excalibur" in next or "excalibur" in next:
			print "You equip the [Excalibur]."
			global excaliW
			excaliW = 1
			raw_input()
			boss_room_fight()
		elif ("exit" in next or "leave" in next) and bRoom_exit == 1:
			if D_tablet == 0:
				print "You need to get the Diamond Tablet. It's your mission."
			else:
				print "You go through the exit."
				raw_input()
				exit_dun()
		elif "left" in next:
			print "You already got everything from the left pedestal."
		elif "right" in next:
			print "You go check out the pedestal on the right."
			raw_input()
			boss_room_Rped()
		elif "back" in next:
			print "The shaft only goes down."
		else:
			print "I don't understand that."
			
			
def exit_dun():
	print "You are warped out of the dungeon. You have completed your mission. You now go \nback to base."
	raw_input()
	print "~~~At the base~~~"
	print "You enter HQ and Alpha greets you."
	raw_input()
	print "\"Hey Sigma. I see you're back from your quest, huh? Omega isn't here right now,\nhe's got a meeting with Emperor Galahad. I'll take the Diamond Tablet instead.\""
	raw_input()
	print "You give the [Diamond Tablet] to Alpha."
	raw_input()
	print "\"Anything else you got from the dungeon is yours. I see you found the Exaclibur.\nIf you have any questions about anything you can ask Delta.\""
	raw_input()
	print "You decide to go to Delta's room to ask him about this ring you got."
	raw_input()
	delta_func()
			
			
def delta_func():
	print "\"Hey Sigma, heard you came back with the Diamond Tablet. I'll be deciphering \nthat for the next few weeks.\""
	raw_input()
	print "\"Oh, you want to show me something?\""
	raw_input()
	print "You take the Ring of Chaos out of your pocket and show Delta."
	raw_input()
	print "\"Where did you get that? Do you know what that is? It's one of the 7 Rings of \nPower, the Ring of Chaos, once used by Mortokai during the Great Elven \nGenocide.\""
	raw_input()
	print "\"Legends say that when a mortal is in posession of all 7 rings, he \nwill have the power of a god. It is because of this legend so many wars and \nbetrayals has happened.\""
	raw_input()
	print "\"The 7 rings are: The Ring of Chaos, The Ring of Peace, The Ring of Darkness, \nThe Ring of Light, The Ring of Time, The Ring of Space, and the Arch Ring.\""
	raw_input()
	print "\"Only 4 of them have been discovered, at least only 4 of them are known \nthrough recorded history.\""
	raw_input()
	print "\"I won't take your ring. You can keep it. But just remember. That ring has \npower beyond any human can imagine. Do not be light in using that ring. Power \nwithout control is just mere violence.\""
	raw_input()
	print "You keep the ring in your pocket and head to your room. It's been a \nlong day, and you're tired. You lay down on your bed and the slight glow of \nthe Ring of Chaos is the last thing you see before you fall asleep."
	raw_input()
	end_game()
	
	
def end_game():
	print "Congratulations! You have finished the game!"
	raw_input()
	exit(0)

start()

