---
title: "Bored Jar"
date: 2022-12-28T18:40:55-08:00
draft: false
tags:
- kids
- software dev
categories: 
- kids
- software dev
---

# Bored Jar

The bored jar is something my daughter and I made and is intended to address the complaining of children in a constructive way. My daughter is 6, but I think this idea works for kids 5-10. Very young kids love to play with the cards if they're laminated too.

The best part about about jar is that it is the first bored activity. Next time your kid is bored on a rainy day sit them down in front of this site and have them make the game. All it takes is a jar, some paper, and a pen/pencil.

## Rules

The bored jar comes into play anytime someone says they're "bored" (a faux pas in life). If you get busted saying "I'm bored" you have to draw a card out of the jar. The cards are three categories; bored attack, activity, or bored reward. The bored rewards are rare, but sometimes someone will be so "bored" they're willing to play the odds and see if they get one. A bored attack is a less desirable card, they make up about a quarter of the cards. Most of the time you will get an activity to solve your boredom.

The first bored activity can be to make the bored jar! Get a mason jar, or a bowl in a pinch, and write out the cards listed below. Make up some of your own! Try to keep the bored rewards to a minimum <10%, the bored attacks should be a chore and about 25% of the cards, and the rest should be activities. Activities should be fun and take at least 15 minutes depending on the age of children in the house.

Each tasks should be expected to take about 15 minutes. The list may need to be modified depending on the setting.

## Cards

### Bored Attack!
- Dig a hole
- Clean the kitchen
- Clean your room
- Vacuum
- Rub your parent's feet...with lotion!
- Clean the fridge

### Activity
- Write a letter to a grandparent
- Do a puzzle
- Sidewalk chalk
- Write a menu to a restaurant and take someone in the house's order
- Spend 15 minutes trying to identify birds
- Find a reptile
- Find 10 different kinds of leaves
- Count the trees
- Take a nap
- Make up a new dance routine and perform it for someone
- Do a small watercolor and mail it to someone
- Make 10 new cards: 1 bored reward, 2 bored attacks, and 7 activities
- Give someone a fifteen minute massage
- Organize all of your pens, pencils, and crayons.

### Bored Reward
- Watch your favorite show
- Have a treat (candy, ice cream)

## Bonus: Bored jar code!

Make a script named `bored.py` with this content (update the cards as you see fit):

```
import random

cards = [
    # Bored attack!
    "Dig a hole",
    "Clean the kitchen",
    "Clean your room",
    "Vacuum",
    "Rub a parent's feet...with lotion!",
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
    "Give someone a fifteen minute massage",
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
```

Then run with `python bored.py`.