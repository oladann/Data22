shopping_list = ["Bread", "Lettuce", "Potatoes", "Bananas"]

print(shopping_list)
print(type(shopping_list))


print(shopping_list[0])
print(shopping_list[-1])

shopping_list[0] = "Sugar"

print(shopping_list)

shopping_list.append("carrots")
print(shopping_list)

shopping_list.remove("Lettuce")
print(shopping_list)

shopping_list.pop()
print(shopping_list)
shopping_list.pop()
print(shopping_list)


mixture = [1, 2, 3, "one", "two", "three"]
print(mixture)

print(mixture[1:3])
print(mixture[1::2])
print(mixture[-1::-2])

essentials = ("Oil", "Salt", "Pepper") # Tuple

# essentials[0] = "Beans"
# You cannot change a value in a tuple