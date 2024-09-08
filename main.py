#imports go at the top
from world import Shop
from stats import Stats
enter_pressed = False
from scroll import Scroll
from tutorial import Tutorial

def main():
    tutorial_instance = Tutorial()  # Create an instance of the Tutorial class
    tutorial_instance.tutorialf()  # Call the tutorialf method to start the tutorial

if __name__ == "__main__":
    main() 
