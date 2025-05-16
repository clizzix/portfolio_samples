class Character:
    def __init__(self, name, health=100, strength=10, defense=5, mana=100):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.mana = mana

    def get_mana(self):
        return self.mana

    def set_mana(self, mana):
        self.mana = mana
    def cast_spell(self):
        self.mana -= 10
        print("You cast a Flash from your hands.")

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def get_strength(self):
        return self.strength

    def set_strength(self, strength):
        self.strength = strength

    def get_defense(self):
        return self.defense

    def set_defense(self, defense):
        self.defense = defense


name = str(input("Enter your name: "))
player = Character(name)
print("Welcome to your personal Adventure, " + player.get_name() + "!")
print("You wake up and slowly open your eyes. You are in a dark room with no light.")
print("Theres a Window to your left hand side and you can see the streets lights shimmering from outside. The door next to it seems to lead on the road,")
print("To the right hand side you see another door.")

answer = input("Which door would you like to go through? Type front for front door and back for back door: ")

if answer == "front":
    print("You step outside and see that its still night, there's nothing much around here.")
    print("To your left theres a car parked on the road. You decide to go to the car.")
    print("The car is empty and its window is rolled down. The car keys are on the drivers seat.")
    print("Your head aches and you remember that in fact this is your car.")
    answer = input("Would you like to take a ride? Type yes or no: ")
    if answer == "yes":
        print("You take the wheel and start driving. You're still a bit dizzy and lacking orientation.")
        print("You turn on your old school vintage radio, but there's only white noise and squeaking")
        print("Seems like you're going to have a hard time getting to your destination, without any entertainment.")
        answer = input("Would you like to go back to your house? Type yes or no: ")
        if answer == "yes":
            print("The wheels are squeaking as you turn around. As you're coming closer to your house, you realize that someone had turned the lights on.")
            answer = input("Your suspicious and remember the gun and the knife under your backseat. Would you like to take the gun or the knife? ")
            if answer == "knife":
                player.set_strength(player.get_strength() + 2)
                print("You're feeling secure as you enter the house.")
            elif answer == "gun":
                player.set_strength(player.get_strength() + 10)
                print("You're feeling secure as you enter the house. You've gain", str(player.get_strength()), "strength.")
            else:
                print("Not a valid option.")
        elif answer == "no":
            pass
        else:
            pass
    elif answer == "no":
        pass
    else:
        print("Not a valid option.")
        print("You decide to go back to your house.")
elif answer == "back":
    print("You're freezing and you decide to go back inside.")
    print("As the door shut behind you, you realize that the door to the back of the house suddenly opened.")
    print("A dark shadow of a man is blocking your path.")
    answer = input("Would you like to attack or talk? Type attack for attack or talk for talk: ")
    if answer == "attack":
        print("The shadow pulls a gun so fast you only see the flash before your lights go out. You're dead!")
    elif answer == "talk":
        print("You talk to the shadow, whose face was still in the dark. 'What are you doing here?'")
        print("The shadow pulls a gun and shoots your fucking face! You're dead, sucker!")
    else:
        print("Not a valid option. You loose!")
else:
    print("Not a valid option.")
