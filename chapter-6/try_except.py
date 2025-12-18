try:
    x = 10 / 0
except ZeroDivisionError:
    print("Zero se divide nahi kar sakte")
    
try:
    num = int("abc")
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Zero division error")
    
# try:
#     file = open("test.txt")
#     data = file.read()
# except FileNotFoundError:
#     print("File nahi mili")
# finally:
#     file.close()

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Result:", x)

try:
    age = int(input("Apni age batao: "))
    print("Your age is:", age)
    if age < 0:
        raise ValueError("Age negative nahi ho sakti")
except ValueError as ve:
    print("Invalid age:", ve)
    
try:
    f = open("data.txt")
    print(f.read())
except FileNotFoundError:
    print("File not found")


# try    → test
# except → handle
# else   → success
# finally→ cleanup
