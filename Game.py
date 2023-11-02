import random
import time
import sys
import os

name = (input("Name: "))

while True:

      try:
            num2 = int(input("Lives: "))
            break
      except ValueError:
            print("Thats not a number!")
            time.sleep(3)
            os.system("cls")
            continue



print(f"\nWelcome {name}!")
time.sleep(2)
print("\nI hope you like my game! I'm new to python so its not too gud, every new live you have 10 health the rest is mistery gud luke.")
time.sleep(3)
print("\nIf you want the instructions for the game check in the readme.")
print("\nLoading game...")

for i in range(10,110,10):
      time.sleep(1)
      print(i, "%")

time.sleep(2)
print("Enjoy!")
time.sleep(3)
os.system("cls")
print(" ")

life = 10
Monster_health = 10
Potion = 1
Damage = random.randint(1,4)
items = ["Sword", f"{Potion} Health Potions", "Shield"]
dodge = random.randint(1,2)
Monster_damage = random.randint(1,3)
shield_durability = 3

def dialogue():

      print("You wake up in your bed, just like every morning.")
      time.sleep(2)
      print("But you notice something diferent, like if you are in another world.")
      time.sleep(2)
      print("You open your eyes and are baffled, somehow you got teleported into a virtual world.")
      time.sleep(2)
      print("Theres a note next to you, you read it.")
      time.sleep(3)
      print("<<Hello adventurer, you have been teleported to this world to deal with a great threat, the great king Malachar.>>")
      time.sleep(3)
      print("<<You are our only hope heroe, we entrust you this job, good luck!>>")
      time.sleep(2)
      print("**You get ou of bed and start exploring the village.**")
      time.sleep(2)
      print("**You start exploring outside of the village and discovering land.**")

def shield_defend():

      global shield_durability

      if shield_durability > 0:
            print("Successefully defended!")
            shield_durability -=1
            print(f"Your shield now has {shield_durability} durability!")
      elif shield_durability <= 0:
            print("Your shield is broken")

def check_death():

      global num2

      if num2 <= 0:
            print("Game Over")
            time.sleep(3)
            sys.exit()
      elif life <= 0:
            print("You died!")
            print("Try again!")
            os.system("cls")
            dialogue()

def monster_dodge():

      global life

      if dodge == 1:
            print("Successefully Dodged!")
            os.system("cls")
      elif dodge == 2:
            print("You failed to Dodge!")
            life -= Monster_damage
            print(f"The monster did {10 - life} damage!")
            print(f"You now have {life} health!")

def check_potions():

      global Potion
      global life

      if Potion <= 0:
            print("You dont have any more potions!")
      else:
            life += 5
            print("You used your health potion!")
            print(f"You now have {life} health!")
            Potion -= 1


check_death()
dialogue()

def monster_defeat():
      if Monster_health <= 0:
            print("Monster Defeated!")
            print("Game Over")
            time.sleep(4)
            sys.exit()
            

def choice():
      print(" ")
      print("You encountered a Monster!")
      time.sleep(1)
      print(" ")
      print("Choose: ")
      time.sleep(1)
      print("[1] - Fight")
      time.sleep(1)
      print("[2] - Flee")
      e_choice = int(input(""))
      if e_choice == 1:
            return True
      elif e_choice == 2:
            return False

def monster_atack():

      global life
      
      print("Its monsters turn, he atacked you.")
      print("What do you do?")
      time.sleep(1)
      print("[1] - Dodge")
      time.sleep(1)
      print("[2] - Use shield")
      Y = input("")

      if Y == input("1"):
            monster_dodge()
            time.sleep(4)
            os.system("cls")
      elif Y == input("2"):
            shield_defend()
            time.sleep(4)
            os.system("cls")

def player_atack():     
      
      global Monster_health
      global life
      global Potion
      global shield_durability

      os.system("cls")

      while num2 > 0:
      
            print(" ")
            print("[1] - Atack")
            print("[2] - Use Heatlh Potion")
            print("[3] - Check items")
            print("[4] - Run")
            X = input("")

            if X == "1":
                  Monster_health -= Damage
                  print("You used your sword against the monster!")
                  print(f"You did {Damage} damage!")
                  time.sleep(3)
                  check_death()
                  monster_defeat()
                  os.system("cls")
                  print(f"The monster has {Monster_health} health!")
            elif X == "2":
                  check_potions()
                  time.sleep(4)
                  os.system("cls")
            elif X == "3":
                  print(items)
                  time.sleep(3)
                  os.system("cls")
            elif X == "4":
                  print("You try to run but the monster crushes you!")
                  time.sleep(3)
                  os.system("cls")
                  print("You died! Try again!")
                  life -= life
                  time.sleep(3)
                  check_death()
                  

            print("Its monsters turn, he atacked you.")
            print("What do you do?")
            time.sleep(1)
            print("[1] - Dodge")
            time.sleep(1)
            print("[2] - Use shield")
            
            Y = input("")

            if Y == "1":  # Compare with strings, not integers
                  if dodge == 1:
                        print("Successfully Dodged!")
                        os.system("cls")
                  elif dodge == 2:
                        print("You failed to Dodge!")
                        life -= Monster_damage
                        print(f"The monster did {10 - life} damage!")
                        print(f"You now have {life} health!")
                        check_death()
                        time.sleep(4)
                        os.system("cls")
                        continue
            elif Y == "2":
                  
                  if shield_durability > 0:
                        print("Successfully defended!")
                        shield_durability -= 1
                        print(f"Your shield now has {shield_durability} durability!")
                  elif shield_durability <= 0:
                        print("Your shield is broken")
                        time.sleep(4)
                        os.system("cls")
                        continue
                  
            

if choice() == True:
      player_atack()
elif choice() == False:
      os.system("cls")
      print(" ")
      print("You coward!")
      time.sleep(2)
      sys.exit()


