import time

print('#################################')
print('### Welcome to "Dragon Quest" ###')
print('#################################')

class Skills:

    def __init__(self):
        self._skills = 1

    def gain_skills(self):
        self._skills += 1

    def  __repr__(self):
        return 'Current level of skills: %s' % (self._skills)

    def count_skills(self):
        return self._skills

class Money:

    def __init__(self):
        self._money = 100

    def gain_money(self, amount):
        self._money += amount

    def spend_money(self, amount):
        self._money -= amount

    def lose_money(self):
        self._money = 0

    def  __repr__(self):
        return 'Current amount of coins: %s' % (self._money)

    def count_money(self):
        return self._money


skill = Skills()
money = Money()

def choice():
    options = [1,2]
    time.sleep(2)
    c = int(input("Choose 1 or 2: >> "))
    if c not in options:
        print("Invalid answer. Please enter 1 or 2.")
        choice()
    return c

def train():
    print("\nAfter years of hard training, you can now proudly call yourself a knight.")
    print("Your first mission is awaiting you: Find and get rid of the white dragon up in the North!")
    time.sleep(1)
    print("\nHowever, be aware that you might need more training, young knight. You now have two options: ")
    print("1 - Stay and train more. 2 - Start your journey.")
    c = choice()
    if c == 1:
        skill.gain_skills()
        print("Well done! You have gained +1 skills and +100 coins, and now feel more confident to start your journey.")
        time.sleep(2)
    if c == 2:
        print("Exciting, isn't it? Your old master also hands you +100 coins for the journey.")
        time.sleep(2)

def market():
    print("\nYou are first passing by the marketplace. There is an old lady who calls you towards her.")
    time.sleep(1)
    print("She is a fortune teller and wants to read your future for just 50 coins. Do you do it?")
    print("1 - Yes. 2 - No.")
    c = choice()
    if c == 1:
        money.spend_money(50)
        time.sleep(1)
        print('\nWhat a weird lady! What could she possible mean by "Do not fight the robbers."? Such a waste of time.')
    if c == 2:
        print("\nYou rather create your own fortune, and continue on your way.")

def forest():
    print("\nForest it is! But what are those weird noises all around you?")
    time.sleep(1)
    print("Help! Five robbers jump from the bushes and start threatening you. What do you do?")
    print("1 - Try to make friends with them. 2 - Fight them off.")
    c = choice()
    if c == 1:
        time.sleep(1)
        print("\nWow, those robbers are funny and friendly guys! And they even teach you some new tricks - your skills increase by +1")
        skill.gain_skills()
    if c == 2:
        print("The fighting begins.")
        time.sleep(1)
        print("Well, that was embarrassing. Not only did the robbers beat you up badly, but they also took all your money!")
        money.lose_money()

def sea():
    print("\nThe sea is beautiful, but larger than expected. In the distance, there is a ferry going across it. But you could also try swimming.")
    print("What do you do? 1 - Ferry, 2 - Swim")
    c = choice()
    if c == 1:
        if money.count_money() < 100:
            print("Oh no, the ferry is 100 coins which you do not have. So swimming it is anyways!")
            time.sleep(1)
            print("\nNot the nicest swim, but a good practice! You gain +1 skills.")
            skill.gain_skills()
            print("You are now exhausted but made it across.")
        else:
            print("The ferry is 100 coins, but there is no turning back now.")
            money.spend_money(100)
            time.sleep(1)
            print("\nNot the most comfortable ride, but you made it to the other side of the sea.")
    if c == 2:
        time.sleep(1)
        print("Not the nicest swim, but a good practice! You gain +1 skills.")
        skill.gain_skills()
        print("\nYou are now exhausted but made it across.")

def journey():
    print("\nTo get to the dragon, you have two possible paths: Through the Forbidden Forest or across the Serpent Sea.")
    print("Choose wisely! 1: Forbidden Forest or 2: Serpent Sea ?")
    c = choice()
    if c == 1:
        forest()
    if c == 2:
        sea()

def rest():
    print("\nYou continue the journey and suddenly, you are so close!\nIn the distance, you can see the white dragon's mountain and hear it roar.")
    time.sleep(1)
    print("You are arriving at a clearing and enjoy your last hours before the fight.")
    print("What will you do before facing your destiny? 1 - Rest. 2 - Practice.")
    c = choice()
    if c == 1:
        print("\nRest is never a bad decision. Now off to the dragon!")
    if c == 2:
        print("\nGreat commitment! Your skills rise by +1.")

def dragon():
    print("\nWill you win, or be eaten by the dragon? Only one way to find out!")
    time.sleep(1)
    print("Your hands are shaking a bit but you keep going.")
    time.sleep(1)
    print("This is it! The dragon is right in front of you and turns to face you.")
    time.sleep(1)
    print("\nIt speaks! It makes you an offer: Instead of fighting you, it would take 100 gold coins to leave.")
    time.sleep(1)
    print("\nYou check your resources and skills level before deciding:")
    print(skill)
    print(money)
    print("\nSo what will it be? 1 - Fight. 2 - Pay.")
    c = choice()
    if c == 1:
        if skill.count_skills() < 3:
            print("The fight is tough, but you are slowly loosing!")
            time.sleep(1)
            print("Oh no! You should have practiced more, the dragon is too strong!")
            time.sleep(1)
            print("This is it - the dragon prepares its final attack. It strikes, and you are dead.")
            print("\nYou lost. Game over.")
        else:
            print("It's a tough fight, but you are gaining ground!")
            time.sleep(1)
            print("You are sweating like crazy, but it's paying off - the dragon is slowly retreating!")
            time.sleep(1)
            print("With one last roar, the dragon sets off. You saved the kingdom! Well done!")
    if c == 2:
        if money.count_money() < 100:
            print("\nFirst, the dragon is happily taking your coins. \nThis however changes fast when it notices you do not have enough!")
            time.sleep(1)
            print("The dragon takes a deep, angry inhale. You are starting to get worried.")
            time.sleep(1)
            print("Maybe you should have fought him instead, but now it's too late! The dragon shoots a giant flame at you, and you are dead.")
            print("\nYou lost. Game over.")
        else:
            print("\nMaybe this is not the most heroic way, but it works.")
            time.sleep(1)
            print("With one last roar, the dragon sets off. You saved the kingdom! Well done!")
            print("Let's just hope no one ever finds out that you cheated your way out of this one.")

def start():
    c = choice()
    if c == 1:
        game_on()
    if c == 2:
        print("\nMaybe another time then, Pyland is looking forward to welcoming you again!")

def game_on():
    train()
    market()
    journey()
    rest()
    dragon()

def play_again():
    print("\nDo you want to play again?")
    print("1 - Yes. 2 - No.")
    start()



###Running it: ###
print("\nWelcome to the kingdom of Pyland. We might need your help. Are you willing to help us?")
print("Please select 1 to start the game, or 2 to exit.")
start()
play_again()