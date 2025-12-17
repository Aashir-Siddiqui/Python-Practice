fruits = ("apple", "cherry", "banana")

print(fruits)
print(type(fruits))

print(fruits[0])
print(fruits[0:2])
print(fruits[-1])

temp = list(fruits)
temp[1] = "mango"
fruits = tuple(temp)
print(fruits)

for fruite in reversed(fruits):
    print(fruite)

i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

a, b, c = fruits
print(a, b, c)

numbers = (1, 2, 3, 4, 5)
x, *y, z = numbers
print(x, y, z)

join = fruits + numbers

print(join)

print(join.count(2))
print(join.index("banana"))