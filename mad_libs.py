# Programmer: Jacob Mark-Synard
# Description: The bot uses questions and makes a sentence.

# The bot asks the following questions to the user.
name = input ("What is your first name? ")
book = input ("Give me your favorite book ")
animal = input ("Give me an animal ")
vehicle = input ("Give me a type of vehicle ")
planet = input ("Tell me a planet. ")

print()

# Bot turns questons into a sentence.
print(f"{name} was reading {book}, the book that featured a {animal} ")
print(f"flying a {vehicle} to the planet; {planet} for an adventure. ")