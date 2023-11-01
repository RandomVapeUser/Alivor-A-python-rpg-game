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
print(" ")
print("I hope you like my game! I'm new to python so its not too gud, every new live you have 10 health the rest is mistery gud luke.")
time.sleep(3)
print(" ")
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
Damage = random.randint(1,4)
items = ["Sword", "Health Potion(5)", "Shield"]

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

dialogue()

def defense():
      
      global life

      X = random.randint(1,3)
      Y = random.randint(1,5)
      Z = X - Y
      
      if Z >= 0:
            print("Successfully defended!")
            print(f"You have {life} health!")
      elif Z < 0:
            life += Z
            print(f"The monster did {-Z} damage!")
            print(f"You have {life} health!")

def check_death():

      global num2

      if num2 <= 0:
            print("Game Over")
            time.sleep(3)
            sys.exit()

      if life <= 0:
            num2 -= 1
            print("You died! Try again!")
            os.system("cls")
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


def fight():     
      
      global Monster_health

      os.system("cls")

      while num2 > 0:
      
            print("You encountered a Monster!")
            print(" ")
            print("[1] - Atack")
            print("[2] - Defend")
            print("[3] - Check items")
            X = input("")

            if X == "1":
                  Monster_health -= Damage
                  print(f"You did {10 - Monster_health} damage!")
                  time.sleep(3)
                  check_death()
                  monster_defeat()
                  os.system("cls")
                  print(f"The monster has {Monster_health} health!")
                  continue
            elif X == "2":
                  defense()
                  check_death()
                  time.sleep(4)
                  os.system("cls")
                  continue
            elif X == "3":
                  print(items)
                  time.sleep(3)
                  os.system("cls")
                  continue


if choice() == True:
      fight()
elif choice() == False:
      os.system("cls")
      print(" ")
      print("You coward!")
      time.sleep(2)
      sys.exit()


