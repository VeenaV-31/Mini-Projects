# 1- import the random module
import random

# 2- Create subjects
subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitaraman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL match",
    "at India Gate"
]

# -3 start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing} "
    print("\n" + headline)

    user_input = input("Do you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break
    #print goodbye messege
print("\nThanks for using Fake News Headline Generator. have a fun day")

