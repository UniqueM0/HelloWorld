import random 

elements = [
    "earth",
    "air",
    "fire",
    "water"
]

#different ways to use random, sample, shuffle
# print("choice===>", random.choice(elements))

# print("sample ===>", random.sample(elements, 2))

# random.shuffle(elements)
# print("shuffle ===>", (elements))


# is returning a random integer from choices  1-5
# print("randint ===>", random.randint(1, 5))

def main():
    for i in range(3):
        outcome = spin()
        print(outcome, end=" ")


def spin():
    n = random.randint(1, 20)
    if n > 15:
        return "cherries"
    elif n > 10:
        return "orange"
    elif n > 5:
        return "plum"
    elif n > 2:
        return "melon"
    elif n > 1:
        return "bell"
    else:
        return "bar"

    


main()