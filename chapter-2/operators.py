# Arithmetic Operators

x = 5
y = 10

print("Addition:", x + y)          # Addition
print("Subtraction:", x - y)       # Subtraction
print("Multiplication:", x * y)    # Multiplication
print("Division:", y / x)          # Division
print("Modulus:", y % x)           # Modulus
print("Exponentiation:", x ** 2)   # Exponentiation
print("Floor Division:", y // x)  # Floor Division


# Assignment Operators

a = 2
a += 2
a -= 3
a *= 4
a /= 2
a %= 3
a **= 2
a //= 2
print("Final value of a:", a)

b = 3
print(b)

print(b := 3)


numbers = [1, 2, 3, 4, 5]
if (n := len(numbers)) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
    

# Comparison Operators

num1 = 10
num2 = 20

print("Equal:", num1 == num2)             # Equal
print("Not Equal:", num1 != num2)         # Not Equal
print("Greater Than:", num1 > num2)       # Greater Than
print("Less Than:", num1 < num2)          # Less Than
print("Greater Than or Equal To:", num1 >= num2)  # Greater Than or Equal To
print("Less Than or Equal To:", num1 <= num2)     # Less Than or Equal To


# Logical Operators

p = True
q = False

print("AND:", p and q)  # Logical AND
print("OR:", p or q)    # Logical OR
print("NOT:", not p)    # Logical NOT


# Identity Operators

m = ["apple", "banana"]
n = ["apple", "banana"]

print("Is m identical to n:", m is n)          # Identity Operator
print("Is m not identical to n:", m is not n)  # Identity Operator

f = [1, 2, 3]
g = [1, 2, 3]
print("Is f identical to g:", f is g)          # Identity Operator
print("Is f not identical to g:", f is not g)  # Identity Operator
print("Is f equal to g:", f == g)              # Equality Operator


#Membership Operators

fruits = ["apple", "banana", "cherry"]
print("Is 'banana' in fruits:", "banana" in fruits)        # Membership Operator
print("Is 'grape' not in fruits:", "grape" not in fruits)  # Membership Operator


#List comprehension with membership operator

nums = [10, 20, 30, 40]

print(20 in nums)       # True
print(50 not in nums)   # True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)

# Using 'in' operator to filter even numbers
filtered_numbers = [num for num in numbers if num in even_numbers]
print("Filtered numbers (even):", filtered_numbers)

# Using 'not in' operator to filter odd numbers
odd_numbers = [num for num in numbers if num not in even_numbers]
print("Odd numbers:", odd_numbers)


#Tuple comprehension with membership operator

colors = ("red", "green", "blue")

print("green" in colors)     # True
print("yellow" not in colors) # True


letters = ('a', 'b', 'c', 'd', 'e')
vowels = ('a', 'e', 'i', 'o', 'u')
vowel_letters = tuple(letter for letter in letters if letter in vowels)
print("Vowel letters:", vowel_letters)
consonant_letters = tuple(letter for letter in letters if letter not in vowels)
print("Consonant letters:", consonant_letters)


#Dictionary comprehension with membership operator

user = {
    "name": "Aashir",
    "age": 22
}

print("name" in user)      # True
print("Aashir" in user)    # False


students_score = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}

passed_students = {name: score for name, score in students_score.items() if score >= 80}
print("Passed students:", passed_students)

failed_students = {name: score for name, score in students_score.items() if score < 80}
print("Failed students:", failed_students)


# Operator Precedence

# | Priority | Operator                                                |   |
# | -------- | ------------------------------------------------------- | - |
# | 1️⃣      | `()`                                                    |   |
# | 2️⃣      | `**`                                                    |   |
# | 3️⃣      | `+x` `-x` `~x`                                          |   |
# | 4️⃣      | `*` `/` `//` `%`                                        |   |
# | 5️⃣      | `+` `-`                                                 |   |
# | 6️⃣      | `<<` `>>`                                               |   |
# | 7️⃣      | `&`                                                     |   |
# | 8️⃣      | `^`                                                     |   |
# | 9️⃣      | `                                                       | ` |
# | 🔟      | `==` `!=` `<` `>` `<=` `>=` `is` `is not` `in` `not in` |   |
# | 1️⃣1️⃣   | `not`                                                   |   |
# | 1️⃣2️⃣   | `and`                                                   |   |
# | 1️⃣3️⃣   | `or`                                                    |   |
# | 1️⃣4️⃣   | `=` `+=` `-=` etc                                       |   |

