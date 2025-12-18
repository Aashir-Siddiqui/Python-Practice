name = "Aashir"
age = 18
pi = 3.14159
salary = 125000.5

# | Specifier | Meaning |
# | --------- | ------- |
# | `%s`      | string  |
# | `%d`      | integer |
# | `%f`      | float   |

print("My name is %s and age is %d" % (name, age))

print("Value of pi is %.2f" % pi)

print("My name is {} and age is {}".format(name, age))

print("Name: {0}, Age: {1}".format(name, age))

print("Name: {name}, Age: {age}".format(name="Aashir", age=18))

price = 99.4567
print("Price: {:.2f}".format(price))

print(f"My name is {name} and age is {age}")

a = 10
b = 5
print(f"Sum is {a + b}")

print(f"Length: {len(name)}")

print(f"Status: {'Adult' if age >= 18 else 'Minor'}")

print(f"{price:.2f}")

score = 0.85
print(f"{score:.0%}")  # 85%

print(f"{5:03}")   # 005


# | Alignment | Syntax |
# | --------- | ------ |
# | Left      | `<`    |
# | Right     | `>`    |
# | Center    | `^`    |

print(f"{'Python':<10}")
print(f"{'Python':>10}")
print(f"{'Python':^10}")

text = "hello"
print(f"{text!r}")   # 'hello'

path = "C:\\Users\\Aashir"
print(fr"Path is {path}")

user = "Aashir"
status = "Active"

log = f"[INFO] User={user}, Status={status}"
print(log)

print(f"{-42:=6}")

print(f"{10:+}")
print(f"{-10:+}")
print(f"{42:_}")
print(f"{10:-}")
print(f"{-10:-}")
print(f"{10: }")
print(f"{-10: }")
num = 1000000
print(f"{num:,}")
print(f"{num:_}")
print(f"{num:b}")
print(f"{10:b}")
print(f"{10:o}")
print(f"{255:x}")
print(f"{255:X}")
print(f"{69:c}")
print(f"{42:d}")
print(f"{12345:e}")
print(f"{12345:E}")
print(f"{pi:f}")
print(f"{pi:.2f}")
print(f"{float('inf'):F}")
print(f"{123456.789:g}")
print(f"{123456.789:G}")
print(f"{1000000:n}")
rate = 0.85
print(f"{rate:%}")
print(f"{rate:.0%}")
print(f"{3.14159:.2f}")
print(f"{text!s}")
print(f"{'ñ'!a}")
print(f"Name: {name:<10} Salary: {salary:>12,.2f}")


# | Concept     | Meaning            |
# | ----------- | ------------------ |
# | `:`         | Formatting start   |
# | `< > ^`     | Alignment          |
# | `+ - space` | Sign control       |
# | `, _`       | Thousand separator |
# | `b o x X`   | Number base        |
# | `f e g %`   | Float formats      |
# | `!r`        | Debug output       |
# | `fr`        | Raw + formatted    |
