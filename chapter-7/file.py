import os

f = open("chapter-7/data1.txt", "r")
content = f.read()
print(content)
f.close()

f_two = open("chapter-7/data2.txt")
for line in f_two:
    print(line)

f_two.close()


f_three = open("chapter-7/data3.txt")
print(f_three.readline())
f_three.close()

with open("chapter-7/data1.txt", "w") as f:
    f.write("Hello World")
    

if os.path.exists("chapter-7/newfile.txt"):
    print("New file exist")
else:
    with open("chapter-7/newfile.txt", "x") as f:
      f.write("New file created")



with open("chapter-7/newfile.txt", "a") as f:
    f.write("\nNew line added")

if os.path.exists("chapter-7/newfile.txt"):
    os.remove("chapter-7/newfile.txt")
else:
    print("File does not exist")

name = input("Enter name: ")
with open("chapter-7/users.txt", "a") as f:
    f.write(name + "\n")

