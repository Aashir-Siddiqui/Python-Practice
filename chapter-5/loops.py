i = 1

while i <= 5:
    print("Iteration:", i)
    if i == 3:
        break
    i += 1
    
while i <= 5:
    i += 1
    if i == 3:
        continue
    print("Iteration after continue:", i)
    
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)