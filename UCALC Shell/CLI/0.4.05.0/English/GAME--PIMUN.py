						if gameselectID == 15:
							print ("P I - M U N")
							print ("Introductory Edition")
							pimunstart = input("\n\n\n\n\nPress [ENTER] key to start")
							print ("\n\n\n")
							introTXT1 = input("Welcome to the world of PIMUN")
							introTXT2 = input("This is a world full of creatures called 'appits'")
							introTXT3 = input("An appit is found out in the wild world of PIMUN. Each appit has it's own abilities")
							introTXT4 = input("However, appits have a common enemy known as malware!")
							introTXT5 = input("You MUST protect and collect appits and kill out the malware that plagues the land")
							introTXT6 = input("Work your way up and take out the evil teams that work in the malware labs")
							introTXT7 = input("[Stuxe] my name is Stuxe and I am going to help you start your journey")
							# LOOONG list of game definitions. Should load within milliseconds 
							appitcount = int(0)
							score = int(0)
							highScore = int(0)
							appit1 = str("<Empty>")
							appit2 = str("<Empty>")
							appit3 = str("<Empty>")
							appit4 = str("<Empty>")
							appit5 = str("<Empty>")
							appit1pos = str("Basic script")
							appit2pos = str("Basic script")
							appit3pos = str("Basic script")
							appit4pos = str("Basic script")
							appit5pos = str("Basic script")
							appit1LVL = int(0)
							appit2LVL = int(0)
							appit3LVL = int(0)
							appit4LVL = int(0)
							appit5LVL = int(0)
							appit1XP = int(0)
							appit2XP = int(0)
							appit3XP = int(0)
							appit4XP = int(0)
							appit5XP = int(0)
							print ("==================================================================")
							print ("| [-_-]                                                          |")
							print ("| [=====================] ( [] ) ( [] ) ( [] )                   |")
							print ("|                                                                |")
							print ("|                                                                |")
							print ("|   (-.-)                                                        |")
							print ("|    |[|                                                         |")
							print ("|    /  \\                                                        |")
							print ("|                                                                |")
							print ("|__________   ___________________________________________________|")
							introTXT8 = input("[STUXE] Now you get to choose your starter appit")
							starteroptions = input("| HTMO lvl 1 | Pithon lvl 1 | scratcher lvl 1")
							starterchoice = input("Choose a starter appit (0-2) ")
							if starterchoice == ("0"):
								introTXT9 = input("You chose HTMO lvl 1")
								appit1 = str("HTMO")
								appit1LVL = int(1)
							if starterchoice == 1:
								introTXT9 = input("You chose Pithon lvl 1")
								appit1 = str("Pithon")
								appit1LVL = int(1)
							if starterchoice == 2:
								introTXT9 = input("You chose Scratcher lvl 1")
								appit1 = str("Scratcher")
								appit1LVL = int(1)
							introTXT10 = input("[STUXE] Now how about you go outside")
							introTXT11 = input("[STUXE] I have a trainer ready for you")
							print ("==================================================================                    ")
							print ("| (-.-)                                                           ")
							print ("|  |[|                                                            ")
							print ("|                                                                 ")
							print ("|           | \ _ / |                                             ")
							print ("|                                                                 ")
							introTXT12 = input("[WHITMAN] Hey there")
							introTXT13 = input("[WHITMAN] The names whitman")
							introTXT14 = input("[WHITMAN] I heard you were into this 'appit' stuff")
							introTXT15 = input("[WHITMAN] show me what you got!")
							if starterchoice == ("0"):
								introTXT16 = input("[WHITMAN] ...\n[WHITMAN] Woah there, that seems like some unfair competition")
								introTXT17 = input("[WHITMAN] an HTMO is no match for ANY appit")
								introTXT18 = input("[WHITMAN] Here, have some XP and we'll try again")
								appit1LVL += 1
								appit1XP += 20
								introTXT19 = input("Your HTMO has leveled up!")
								introTXT20 = input("Level 2")
								appit1LVL += 1
								appit1XP += 30
								introTXT21 = input("Your HTMO has leveled up!")
								introTXT22 = input("Level 3")
								appit1LVL += 1
								appit1XP += 100
								introTXT23 = input("Your HTMO has leveled up!")
								introTXT24 = input("Level 4")
								appit1LVL += 1
								appit1XP += 300
								introTXT25 = input("Your HTMO has leveled up!")
								introTXT26 = input("Level 5")
								introTXT27 = input("What's this? Your HTMO is evolving...")
								appit1pos = str("Simple structure")
								introTXT28 = input("Your HTMO has evolved from a simple script to a simple structure")
								introTXT29 = input("[WHITMAN] OK, let's get this going! Welcome to your first battle")
							if starterchoice == ("1"):
								introTXT30 = input("[WHITMAN] A Pithon? No way!")
								introTXT31 = input("[WHITMAN] Why did that pimp give that to you?")
								introTXT32 = input("[WHITMAN] upupup, no time for answers, let's give that python some exercise!")
							if starterchoice == ("2"):
								introTXT33 = input("[WHITMAN] A scratcher?")
								introTXT34 = input("[WHITMAN] You are one SIIIIIIIIMPLE man")
								introTXT35 = input("[WHITMAN] let's get that scratcher started, fight me!")
							introTXT36 = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
							introTXT37 = input("A wild email worm appeared")
							emwormlvl = int(2)
							emwormhealth = int(50)
							emwormdamage = int(12)
							emwormname = str("I-LOVE-YOU.vbs")
							if starterchoice == ("0"):
								print ("| HTML5_webstructure.htm | " + str(appit1LVL))
								print ("|")
								print ("|")
								print ("|")
								print ("|")
								print ("|" + str(emwormname) + " " + " LVL: " + str(emwormlvl))
								print ("| Block | Delete | Flee")
								battleloop = int(1)
								while battleloop == 1:
									introTXT38 = input("What will you do? ")
									if introTXT38 == ("Block"):
										introTXT39 = input("You used block")
										introTXT40 = input("It wasn't very effective")
									if introTXT38 == ("Delete"):
										introTXT41 = input("You used DELETE")
										introTXT42 = input("It was very effective")
										emwormhealth = int(0)
										introTXT43 = input(str(emwormname) + " fainted")
										introTXT44 = input("You earned 6 xp")
										appit1XP += 6
										battleloop -= 1
									if introTXT38 == ("Flee"):
										introTXT45 = input("[WHITMAN] You cannot flee your first fight. Com'on!")
							if starterchoice == ("1"):
								print ("| Hello_World.py | " + str(appit1LVL))
								print ("|")
								print ("|")
								print ("|")
								print ("|")
								print ("|" + str(emwormname) + " " + " LVL: " + str(emwormlvl))
								print ("| Buffer | Delete | Flee")
								battleloop = int(1)
								while battleloop == 1:
									introTXT38 = input("What will you do? ")
									if introTXT38 == ("Buffer"):
										introTXT39 = input("You used buffer")
										introTXT40 = input("It wasn't very effective")
									if introTXT38 == ("Delete"):
										introTXT41 = input("You used DELETE")
										introTXT42 = input("It was very effective")
										emwormhealth = int(0)
										introTXT43 = input(str(emwormname) + " fainted")
										introTXT44 = input("You earned 6 xp")
										appit1XP += 6
										battleloop -= 1
									if introTXT38 == ("Flee"):
										introTXT45 = input("[WHITMAN] You cannot flee your first fight. Com'on!")
							if starterchoice == ("2"):
								print ("| Untitled.sb | " + str(appit1LVL))
								print ("|")
								print ("|")
								print ("|")
								print ("|")
								print ("|" + str(emwormname) + " " + " LVL: " + str(emwormlvl))
								print ("| Run project | Delete | Flee")
								battleloop = int(1)
								while battleloop == 1:
									introTXT38 = input("What will you do? ")
									if introTXT38 == ("Block"):
										introTXT39 = input("You used run project")
										introTXT40 = input("It wasn't very effective")
									if introTXT38 == ("Delete"):
										introTXT41 = input("You used DELETE")
										introTXT42 = input("It was very effective")
										emwormhealth = int(0)
										introTXT43 = input(str(emwormname) + " fainted")
										introTXT44 = input("You earned 6 xp")
										appit1XP += 6
										battleloop -= 1
									if introTXT38 == ("Flee"):
										introTXT45 = input("[WHITMAN] You cannot flee your first fight. Com'on!")
							introTXT46 = input("[WHITMAN] Good job on destroying my worm")
							introTXT47 = input("[WHITMAN] ...")
							introTXT48 = input("[STUXE] Whitman, what are you still doing here?")
							introTXT49 = input("[WHITMAN] oh, ha, just finishing up")
							introTXT50 = input("[WHITMAN] got to go kid, see ya later")
							introTXT51 = input("You are now on your own")
							introTXT52 = input("Consider looking at your appdex")
							introTXT53 = input("| Appdex | continue | ")
							if introTXT53 == ("Appdex"):
								print ("The Pimun appdex")
								print ("Appits")
								print ("HTMO - starter")
								print ("Evolutions")
								print ("Level 1 - Basic script")
								print ("Level 5 - Structured web page")
								print ("Level 10 - Strong web frame")
								print ("Level 20 - Java belly")
								print ("Level 40 - Source code megablock")
								print ("Level 60 - Client")
								print ("Level 80 - website meta HQ")
								print ("Level requirements")
								print ("Level 2 - 20 xp | Level 3 - 50 xp | level 4 - 150 xp | level 5 - 400 xp | level 6 - 700 xp | level 7 - 1000 xp")
								print ("Level 8 - 2000 xp | level 9 - 2500 xp | level 10 - 3200 xp | level 11 - 4000 xp | level 12 - 6000 xp | level 13 - 8000 xp")
								next = input("Press [ENTER] key for more")
								print ("Pithon - Starter")
								print ("Level 1 - Basic script")
								print ("Level 20 - Basic command-line")
								print ("Level 50 - Full command line")
								print ("Level 120 - Workstation")
								print ("Level 140 - Toolkit")
								print ("Level requirements")
								print ("Level 2 - 20 xp | Level 3 - 50 xp | level 4 - 150 xp | level 5 - 400 xp | level 6 - 700 xp | level 7 - 1000 xp")
								print ("Level 8 - 2000 xp | level 9 - 2500 xp | level 10 - 3200 xp | level 11 - 4000 xp | level 12 - 6000 xp | level 13 - 8000 xp")
								next = input("Press [ENTER] key for more")
								print ("Scratcher - Starter")
								print ("Level 1 - Basic script")
								print ("Level 5 - New project")
								print ("Level 10 - Advanced project")
								print ("Level 20 - SB2 project")
								print ("Level requirements")
								print ("Level 2 - 20 xp | Level 3 - 50 xp | level 4 - 150 xp | level 5 - 400 xp | level 6 - 700 xp | level 7 - 1000 xp")
								print ("Level 8 - 2000 xp | level 9 - 2500 xp | level 10 - 3200 xp | level 11 - 4000 xp | level 12 - 6000 xp | level 13 - 8000 xp")
								next = input("Press [ENTER] key for more")
								print ("JavJar Jinx - Common")
								print ("Level 1 - Mini archive")
								print ("Level 20 - Mega archive")
								next = input("Press [ENTER] key for more")
								print ("Javajuice - Common")
								print ("Level 1 - basic script")
								print ("Level 5 - Basic java application")
								print ("Level 25 - Advanced Java application")
								next = input("Press [ENTER] key for more")
								print ("Yammy - Rare")
								print ("Level 1 - Basic script")
								print ("Level 8 - YAML database")
								next = input("Press [ENTER] key for more")
								print ("Bash - Rare")
								print ("Level 1 - Basic script")
								print ("Level 12 - SUDObatch")
								next = input("Press [ENTER] key for more")
								print ("Adobo - Rare")
								print ("Level 1 - CS1")
								print ("Level 10 - CS2")
								print ("Level 20 - CS3")
								print ("Level 30 - CS4")
								print ("Level 50 - CS5")
								print ("Level 60 - CS6")
								print ("Level 90 - CC")
								next = input("Press [ENTER] key for more")
								print ("Malware")
								print ("Email worm - Common")
								print ("Level 1 - I-LOVE-YOU worm")
								next = input("Press [ENTER] key for more")
								print ("Macro - Common")
								print ("Level 1 - Office macro")
								print ("Level 5 - Copy macro")
								print ("Level 20 - Massive macro")
								print ("\tCopies all your moves and uses them against you with 2x the effect")
								next = input("Press [ENTER] key for more")
								print ("Trojan - Common")
								print ("Level 1 - Mini fleet")
								print ("Level 5 - Mini army")
								print ("Level 20 - Army cloner")
								print ("\tDoes the first attack, 80% endurance to all attacks")
								next = input("Press [ENTER] key for more")
								print ("Zip bomb - Rare")
								print ("Level 1 - Tarpit")
								print ("Level 5 - Package")
								print ("Level 20 - Magic package")
								print ("\tUses heavy blocks and sends them to you. Cannot be attacked until all files are extracted. Can only be weakened when corrupted")
								next = input("Press [ENTER] key for more")
								print ("Memz - Rare")
								print ("Level 1 - Version 1.0")
								print ("Level 5 - Version 2.0")
								print ("Level 10 - Version 3.0")
								print ("Level 20 - Version 4.0")
								print ("Level 40 - Version 5.0")
								print ("Level 75 - Vinememz")
								next = input("Press [ENTER] key for more")
								print ("Bonzi buddy - Common")
								print ("Level 1 - New 'friend'")
								print ("Level 5 - Annoyance")
								print ("Level 20 - Team Bonzi")
								print ("\tDistracts you and stalks your moves. Do not show an obvious pattern, or he will be able to defend against it")
								next = input("Press [ENTER] key for more")
								print ("That is the whole index!")
							gamefinished = input("Congratulations!\nYou beat the game")