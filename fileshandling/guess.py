import random
sec_num = random.randint(1,11)
def guess():
    attemped = 0
    attemps = 0
    guess_num = None
    while sec_num!=guess_num:
        try:
            guess_num = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        attemps+=1
        if guess_num>sec_num:
            print("just high.")
        elif guess_num<sec_num:
            print("just low")
        else:
            print(f"right in {attemps} attemps.")
            break
        f = open("attemps.txt","w")
        if attemps>attemped:
            print(f.write(f"attemps = {attemps}"))
        else:
            print(f"attemps is {attemps}")


guess()
