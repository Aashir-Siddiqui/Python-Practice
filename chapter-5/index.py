# match

status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Unknown")

developer = "jsDeveloper"
salary = "100000"

match developer:
    case "pythonDeveloper":
        print(salary)
    case "jsDeveloper":
        print(salary)
    case "deveOps":
        print(salary)
    case _:
        print("Not Found")
        
        
# range 

for i in range(1, 11):
    match i:
        case i if 1 <= i <= 3:
            print(f"{i} is in range 1-3")
        case i if 4 <= i <= 6:
            print(f"{i} is in range 4-6")
        case i if 7 <= i <= 10:
            print(f"{i} is in range 7-10")
        case _:
            print(f"{i} is out of range")


print(list(range(1, 11)))
print(list(range(5)))
print(list(range(0, 21, 5)))
print(list(range(10, 0, -1)))


# array

import array as arr
numbers = arr.array('i', [1, 2, 3, 4, 5])
print(type(numbers))

num = arr.array('i', [1, 2, 3, 4, 5])
print(num)

for n in num:
    print(n)

print(num[0])
num.append(6)
print(num)
num.insert(2, 10)
print(num)
num.remove(3)
print(num)
print(num.pop())
print(num)
num.reverse()
print(num)
print(num.index(4))
print(num.count(2))
num.extend([7, 8, 9])
print(num)
new_array = arr.array(num.typecode, (x * 2 for x in num))
print(new_array)
for n in new_array:
    print(n)
squares = arr.array('i', (x**2 for x in range(1, 6)))
print(squares)
for s in squares:
    print(s)
import sys
print("Size of array:", sys.getsizeof(squares))
print("Length of array:", len(squares))