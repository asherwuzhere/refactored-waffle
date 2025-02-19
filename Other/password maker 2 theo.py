import random
import time
yes = ["Yes", "yes", "YES", "yeah", "Yeah", "YEAH", "y", "Y"]
no = ["NO", "No", "no", "nah", "NAH", "Nah", "n", "N"]
sym = ["!", "?", "$"]
ransym = random.choice(sym)
yn = input("Hello, would you like to create a password?: ")
if yn in no:
    print ("Thanks, goodbye.")
elif yn in yes:
    kw = input("Please enter a keyword you would like for your password. ex) dogs name, favorite food, etc: ")
    kw = kw.capitalize()
    print(f"Thank you for selcting the keyword {kw}")
    kw2 = input ("Please enter another keyword you would like for your password: ")
    kw2 = kw2.capitalize()
    print(f"Thank you for selcting the keyword {kw2}")
    num = input("Please enter your favorite number for your password. If you don't have a number in mind, enetr 'No number selected' for a random number: ")
    if num.isnumeric():
        print (f"Thank you for selecting the number {num}")
    else:
        num = f"{random.randint(0, 99):02}"
        print (f"Okay, the random number selected for you is {num}")
    yn2 = input("Would you like symbols in your password?: ")
    if yn2 in no:
        yn3 = input("Would you a symbol at the end of your password?: ")
        if yn3 in no:
            print("Generating Password", end="", flush=True)
            time.sleep(0.5)
            print(".", end="", flush=True)
            time.sleep(0.5)
            print(".", end="", flush=True)
            time.sleep(0.5)
            print(".")
            print(kw + kw2 + num)
        elif yn3 in yes:
            print("Generating Password", end="", flush=True)
            time.sleep(0.5)
            print(".", end="", flush=True)
            time.sleep(0.5)
            print(".", end="", flush=True)
            time.sleep(0.5)
            print(".")
            print(kw + kw2 + num + ransym)
    elif yn2 in yes:
        yn4 = input("Would you a symbol at the end of your password?: ")
        if yn4 in yes:
            print("Generating Password", end="", flush=True)
            time.sleep(0.5)
            print(".", end="", flush=True)
            time.sleep(0.5)
            print(".", end="", flush=True)
            time.sleep(0.5)
            print(".")
            kw = kw.replace("s", "$")
            kw = kw.replace("S", "$")
            kw = kw.replace("o", "@")
            kw = kw.replace("a", "@")
            kw2 = kw2.replace("s", "$")
            kw2 = kw2.replace("S", "$")
            kw2 = kw2.replace("o", "@")
            kw2 = kw2.replace("a", "@")
            print(kw + kw2 + num + ransym)
        elif yn4 in no:
            print("Generating Password", end="", flush=True)
            time.sleep(0.5)
            print(".", end="", flush=True)
            time.sleep(0.5)
            print(".", end="", flush=True)
            time.sleep(0.5)
            print(".")
            kw = kw.replace("s", "$")
            kw = kw.replace("S", "$")
            kw = kw.replace("o", "@")
            kw = kw.replace("a", "@")
            kw2 = kw2.replace("s", "$")
            kw2 = kw2.replace("S", "$")
            kw2 = kw2.replace("o", "@")
            kw2 = kw2.replace("a", "@")
            print(kw + kw2 + num)
