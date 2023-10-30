import random
import time
import sys
import os

name = (input("Name: "))
num2 = int(input("Lives: "))

print(f"\nWelcome {name}!")

print("\nLoading game...")

for i in range(10,110,10):
      time.sleep(1)
      print(i, "%")

time.sleep(2)
print("Enjoy!")
time.sleep(3)
os.system("cls")

lives = num2
life = 10
Monster_health = 10
Monster_damage = random.randint(1,3)
Defense = random.randint(1,3)
Damage = random.randint(1,4)

def defense_check(a,b):
      if a - b < 0:
            print("The monster did", b - a, "damage")
            return True
      elif a - b == 0 or a - b > 0:
            print("Successefully defended!")
            return False


def check_death():
      if life <= 0:
            sys.exit()

print("You encountered a Monster!")

items = ["Sword", "Health Potion(5)", "Shield"]

print("Choose: ")
time.sleep(1)
print("[1] - Fight")
time.sleep(1)
print("[2] - Flee")

e_choice = int(input(" "))

if e_choice == 1:
    
      os.system("cls")

      while lives > 0:

            print("[1] - Atack")
            print("[2] - Defend")
            X  =  input("\n[3] - Check items")
            
            if X == 1:
                  Monster_health -= Damage
                  print(f"You did {10 - Monster_health} damage!")
                  time.sleep(3)
                  check_death()
                  os.system("cls")
                  print(f"The monster has {Monster_health} health!")
                  print(" ")
                  continue
            elif X == 2:
                  defense_check(Defense, Monster_damage)
                  time.sleep(4)
                  os.system("cls")
                  continue
            elif X == 3:
                  print(items)
                  time.sleep(5)
                  os.system("cls")
                  continue
elif e_choice == 2:
      print("You coward, kys")
      time.sleep(2)
      sys.exit()