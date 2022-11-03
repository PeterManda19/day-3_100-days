import time

food = input("A type of food: ")
plant = input("A type of plant: ")
cooking = input("A method of cooking: ")
burned = input("A word to describe burned food: ")
item = input("A household item: ")
print()

print(cooking.upper(), food, "with", burned, plant, "on a bed of", item)


def endGame():
  while True:
    print()
    x= input("""Thank you for playing the game!
To read again please click Stop on top right page and click Run """)
    print()
    continue


if __name__ == "__main__":
  time.sleep(2)
  endGame()