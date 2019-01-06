import random
import json


SecretSanta = {}


def generate(dictionary):
    Members = [
        "Josh",
        "Tori",
        "Nick",
        "Emily",
        "Nichole",
        "Austin",
        "Kayla",
        "Annabelle",
        "Jaden",
        "Dakota",
    ]
    count = {}.fromkeys(Members, 0)
    for member in Members:
        a = random.choice(Members)
        b = random.choice(Members)
        while a == b or count[a] == 2 or count[b] == 2 or a == member or b == member:
            b = random.choice(Members)
            a = random.choice(Members)
        count[a] += 1
        count[b] += 1
        SecretSanta[member] = a + ' , ' + b
    if all(i == 2 for i in count.values()):
        print("We've assigned everyone a Secret Santa!")
    print(count)


def readSS(SSlist):
    for key in SSlist:
        print("{} : {}\n".format(key, SSlist[key]))


def deploySS(SSList):
    for key in SSList:
        with open(key, 'w') as f:
            json.dump(SecretSanta[key], f)


def _main_(SecretSanta):
    choice = input('Would you like to generate the Secret Santa list again?: ')
    if choice == 'n' or choice == 'N':
        output = input('Thank you for the brief time I was alive\n(Please press <ENTER> to exit the program)')
        exit()
    elif choice == 'y' or choice == 'Y':
        generate(SecretSanta)
        deploySS(SecretSanta)
        exit()
    else:
        output = input('Please run the program again.\n(Press <ENTER> to continue)')
        exit()


_main_(SecretSanta)

