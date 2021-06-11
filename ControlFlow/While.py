is_integer = False

while not is_integer:
    age = input("What is your age? ")
    if age.isdigit() and 0 < int(age) < 120:
        is_integer = True
        print("Thanks for providing your age")
    else:
        print("Please provide your answer as a number below 120")