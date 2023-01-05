import random

cards = [
    # Bored attack!
    "Dig a hole",
    "Clean the kitchen",
    "Clean your room",
    "Vacuum",
    # Activities
    "Write a letter to a grandparent",
    "Do a puzzle",
    "Sidewalk chalk",
    "Write a menu to a restaurant and take someone in the house's order",
    "Find a bird",
    "Find a lizard",
    "Find 10 different kind of leaves",
    "Count the trees",
    "Take a nap",
    "Learn a new dance move and perform it to someone",
    "Do a small watercolor and mail it to someone",
    "Make 10 new cards: 1 bored reward, 2 bored attacks, and 7 activities",
    # Bored reward
    "Watch your favorite show",
    "Have a treat (candy, ice cream)",
]

def get_a_card(cards):
    """Takes a list of cards and returns one.
    """
    return random.choice(cards)

if __name__ == "__main__":
    print(get_a_card(cards))