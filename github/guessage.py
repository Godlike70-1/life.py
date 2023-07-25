def age(DOB):
    current_year = 2023
    a = current_year-DOB
    print(f"your age is exactly {a}.")
    if a<18:
        print("Sorry,your not authorized to vote.")
    else:
        print("you are authorized to vote.")

age(2005)