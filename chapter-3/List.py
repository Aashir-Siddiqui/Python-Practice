my_list = [1, "two", 3.0, True, [5, 6, 7]]

print(my_list)
print(len(my_list))
print(my_list[0])        # Access first element
print(my_list[4])        # Access nested list
print(my_list[4][1])     # Access element in nested list
my_list.append("new item")
print(my_list)
print(my_list.remove(3.0))
my_list.insert(2, "inserted item")
print(my_list)
print(my_list.pop())
print(my_list)
print(my_list.index("two"))

num1 = [1, 2, 3]
num2 = [4, 5, 6]

print(num1 + num2)

num1.extend(num2)
print(num1)

del num1[0]
print(num1)

fruits = ["apple", "cherry", "date", "banana"]
fruits.sort()
print(fruits)

for fruit in reversed(fruits):
    print(fruit)
    
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
    
    
numbers = [4, 3, 1, 2, 5]
squares = [x**2 for x in numbers if x % 2 == 0]
print(squares)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

copy1 = numbers.copy()
copy2 = copy1[:]
print(copy1, copy2)

listCopy = list(fruits)
print(listCopy)

print(fruits.count("apple"))

print(fruits.clear())
print(fruits)