car_parts = {"wheels", "doors", "exhaust", "exhaust"}
print(car_parts)

list_CarParts = ["wheels", "doors", "exhaust", "exhaust"]
print(set(list_CarParts))

car_parts.add("windows")
print(car_parts)

car_parts.discard("doors")
print(car_parts)

x = frozenset([1,2,3,4])
print(x)