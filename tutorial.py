from scroll import Scroll
from stats import Stats  # Correctly import the Stats class
from world import Shop  # Import the Shop class

class Tutorial:
    def __init__(self):
        self.scroll = Scroll()
        self.stats = Stats()

    def tutorialf(self):
        stats = self.stats  # Use the stats object from the class

        # Start of name program
        stats.Name = input("Enter your name: ")
        self.scroll.slow_print("Hi " + stats.Name)
        self.scroll.slow_print("Welcome to the Overrun Animal Earth")
        self.scroll.slow_print("You must rescue Animal Earth from humans")
        self.scroll.slow_print("Choose a Weapon: Mace, Bow, or Sword.")

        resetwp = True
        while resetwp:
            stats.Weapon = input("What weapon do you choose? ").lower()
            if stats.Weapon == "mace":
                self.scroll.slow_print("You have chosen the Mace")
                self.scroll.slow_print("It has swing, throw, and slam as moves.")
                resetwp = False
            elif stats.Weapon == "bow":
                self.scroll.slow_print("You have chosen the Bow")
                self.scroll.slow_print("It has Shoot, Charged Shot, and Charge as moves")
                resetwp = False
            elif stats.Weapon == "sword":
                self.scroll.slow_print("You have chosen the Sword")
                self.scroll.slow_print("It has stab, swing, and slam.")
                resetwp = False
            else:
                self.scroll.slow_print("You didn't choose correctly, try again.")
                resetwp = True

        stats.gold = 400
        self.scroll.slow_print("You receive 400 gold as a starter gift")
        self.scroll.slow_print("Gold can be used to buy items and barter around")
        self.scroll.slow_print("You can get gold from defeating an enemy")
        self.scroll.slow_print("Now it is time for you to begin your journey")
        self.scroll.slow_print("I wish you the best of luck, freeing the animals from this world")

        # Tutorial Town Code
        self.scroll.slow_print("You are in a town")
        self.scroll.slow_print("In a town, you can do a bunch of things!")
        self.scroll.slow_print("For now, let's visit the shop")
        self.scroll.slow_print("You can visit the shop by typing 'Shop' when you are at most towns")
        self.scroll.slow_print("To do that, just type in 'Shop'!")

        # Initial prompt
        stats.place = input("Where do you want to go?: ")

        # Loop until 'Shop' is selected
        while stats.place.lower() != "shop":
            self.scroll.slow_print("You didn't type in 'Shop', so you are still in the town")
            self.scroll.slow_print("You can visit the shop by typing 'shop' when you are at most towns")
            self.scroll.slow_print("To do that, just type in 'Shop'!")
            stats.place = input("Where do you want to go?: ")

        # Create an instance of Shop and call the merchant method
        shop_instance = Shop(stats)
        shop_instance.merchant()

        # Battle initiation or something similar
        self.scroll.slow_print("You still need to learn how to fight. ")
        self.scroll.slow_print("To first fight, go into the outskirts.")
        self.scroll.slow_print("To go to the outskirts, you need to go out of the town first.")
        self.scroll.slow_print("To do that, type leave.")

        # You can add the logic for leaving the town and entering the outskirts here

