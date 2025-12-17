x=5
x="Hello, World!"
print(x)


# Variable Types Casting

y=float(10.3)
print(y)
z=int(7.9)
print(type(z))


# Multiple Variable Assignment

a, b, c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)

x1 = y1 = z1 = "Orange"
print(x1, y1, z1)

fruits = ["apple", "banana", "cherry"]
x2, y2, z2 = fruits
print(x2, y2, z2)


# global variable example

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)