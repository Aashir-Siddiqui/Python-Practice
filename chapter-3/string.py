name = "Aashir"

greeting = f"Hello, {name}!"
print(greeting)

# String Methods
text = "  Hello, World!  "
print(text.lower())
print(text.upper())
print(text.strip())
print(text.replace("World", "Python"))
print(text.split(","))
print("Hello" in text)
print("Python" not in text)
print(text.startswith("  He"))
print(text.endswith("!  "))
print(text.find("World"))
print(text.count("l"))
print(text.capitalize())
print(text.title())
print(text.center(30))
print(text.ljust(30))
print(text.rjust(30))
print(text.zfill(30))
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())


# String Slicing

sample = "PythonProgramming"

# P  y  t  h  o  n  P  r  o  g  r  a  m  m  i  n  g
# 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
# -17-16-15-14-13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1


print(sample[0:6])      # 'Python'
print(sample[6:])       # 'Programming'
print(sample[:6])       # 'Python'
print(sample[-11:-5])   # 'Progra'
print(sample[-5:])      # 'amming'
print(sample[::-1])     # 'gnimmargorPnohtyP'
print(sample[::2])      # 'Pto rgamn'
print(sample[1::2])     # 'yhnPormig'
print(sample[::3])      # 'Phamg'
print(sample[1:10:2])   # 'yhnPr'
print(sample[-1:-12:-1]) # 'gnimmargorP'
print(sample[-12::-1])  # 'nohtyP'
print(sample[5:0:-1])   # 'nohty'
print(sample[3:14:3])   # 'horm'
print(sample[4::-1])    # 'nohtyP'
print(sample[-3::-2])   # 'mrgamn'
print(sample[2:15:4])   # 'tarm'
print(sample[-15:-2:2]) # 'yhnormg'
print(sample[::4])      # 'Pham'
print(sample[1:-1:3])   # 'yorm'
print(sample[-1::-3])   # 'gmrh'
print(sample[::5])      # 'Prg'
print(sample[2::-1])    # 'htyP'
print(sample[-4:-15:-2]) # 'marny'
print(sample[3::4])     # 'horm'
print(sample[-2::-3])   # 'goyP'
print(sample[1:14:5])   # 'yag'


# String Formatting

name = "Alice"
age = 30
intro = "My name is {} and I am {} years old.".format(name, age)
print(intro)

