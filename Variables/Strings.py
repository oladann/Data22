# String_failure = 'I Said 'Wow!''

escape_example = 'I Said \"Wow!\"'

print(escape_example)

Reverse_Quote_in_quote = "I said 'Wow!'"

print(Reverse_Quote_in_quote)

Hw = "Hello! World"

print(Hw[7:])
print(Hw[-5:])
print(Hw[:5])
print(Hw[3:8])

print(len(Hw))

White_space = "Lots of space at the end           "
print(len(White_space))
print(len(White_space.strip()))
print(White_space.strip())

Example_Text = "Here's some text with lot's of text"

print(Example_Text.count("text"))
print(Example_Text.lower())
print(Example_Text.upper())
print(Example_Text.capitalize())
print(Example_Text.replace("with", "without"))
print(Example_Text.replace("'", ""))


a = 2
b = 5.4
c = "How old are you? "

print(c+"I am "+str(a)+str(b))


int_string = "6"
print(type(int(int_string)))
print(type(float(int_string)))


name = "Lassie"
years = 7
height_cm = 60.2

print(f"{name} is {years} years old and {height_cm}cm tall")

print(f"{name.upper()} is {years*7} years old in dog years")



pi = 3.14159265359

print(f"Pi to 3 decimal places: {pi:.3f}")
print(f"Pi to 3 decimal places: {pi:.5f}")

score = 16
max_score = 26

print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:%}")
print(f"You scored {score/max_score:.2%}")
print(f"You scored {score/max_score:.0%}")