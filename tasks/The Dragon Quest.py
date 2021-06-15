import time

#print('#################################')
#print('### Welcome to "Dragon Quest" ###')
#print('#################################')

class Skills:

    def __init__(self):
        self._skills = 1

    def gain_skills(self):
        self._skills += 1

class Money:

    def __init__(self):
        self._money = 100

    def gain_money(self, amount):
        self._money += amount

    def spend_money(self, amount):
        self._money -= amount

    def lose_money(self):
        self._money = 0

options = [1,2]
skill = Skills()
money = Money()

def choice:
    #TODO
    pass

def start():
    print("After years of hard training, you can now proudly call yourself a knight.")
    print("Your first mission is awaiting you: Find and get rid of the white dragon up in the North!")
    time.sleep(1)
    print("However, be aware that you might need more training, young knight. You now have two options: ")
    print("1 - Stay and train more. 2 - Start your journey.")
    choice = int(input("Choose 1 or 2: >> "))
    if choice not in options:
        print("This isn't a good start, as this is an invalid answer. Please enter 1 or 2.")
        choice = int(input("Choose 1 or 2: >> "))
    if choice == 1:
        skill.gain_skills()
        print("Well done! You have gained +1 skills and +100 coins, and now feel more confident to start your journey.")
        time.sleep(1)
    if choice == 2:
        print("Exciting, isn't it? Your old master also hands you +100 coins for the journey.")
        time.sleep(1)

def market():
    print('')
    print("You are first passing by the marketplace. There is an old lady who calls you towards her.")
    time.sleep(1)
    print("She is a fortune teller and wants to read your future for just 50 coins. Do you do it?")
    choice = int(input("Choose 1 (yes) or 2 (no): >> "))
    if choice not in options:
        print("Invalid answer. Please enter 1 or 2.")
        choice = int(input("Choose 1 or 2: >> "))
    if choice == 1:
        money.spend_money(50)
        time.sleep(1)
        print('What a weird lady! What could she possible mean by "Do not fight the robbers."? Such a waste of time.')
    if choice == 2:
        print("You rather create your own fortune, and continue on your way.")

def forest():
    #TODO
    pass

def sea():
    #TODO
    pass

def journey():
    print("To get to the dragon, you have two possible paths: Through the Forbidden Forest or across the Serpent Sea. Choose wisely!")
    c = input("1: Forbidden Forest or 2: Serpent Sea ? >> ")
    if c not in options:
        print("Invalid answer. Please enter 1 or 2.")
        c = int(input("Choose 1 or 2: >> "))
    if c == 1:
        forest()
    if c == 2:
        sea()

def rest():
    #TODO
    pass

def dragon():
    #TODO
    pass



start()
market()
journey()
rest()
dragon()

