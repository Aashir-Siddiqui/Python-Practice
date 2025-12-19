import math
from functools import wraps
from functools import reduce

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())
print(greet("Aashir"))

def freeze_point(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return f"Freezing point of water is {fahrenheit}°F"

print(freeze_point(0))
print(freeze_point(-40))

def calculate_area(radius):
    area = math.pi * (radius ** 2)
    return f"Area of circle with radius {radius} is {area:.2f}"

print(calculate_area(5))

def my_funtion(x, y):
    return x * y

print(my_funtion(4, 5))
print(my_funtion(y=4, x=5))

def total(*args):
    return sum(args)

print(total(1, 2, 3, 4))

def user_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

user_info(name="Aashir", age=22)

x = 10  # global

def test():
    x = 5  # local
    print(x)

test()
print(x)

def outer(func):
    def inner():
        print("Before calling the function")
        func()
        print("After calling the function")
    return inner

# def say_hello():
#     print("Hello!")
    
# decorated_function = outer(say_hello)
# decorated_function()
    
@outer
def say_hello():
    print("Hello!")
    
say_hello()


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

result = add(3, 5)
print("Result:", result)

def check_zero (func):
    def inner(a, b):
        if b == 0:
            return "Division by zero is not allowed."
        return func(a, b)
    return inner

@check_zero
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello")

hello()

def decor1(func):
    def wrapper():
        print("Decor 1")
        func()
    return wrapper

def decor2(func):
    def wrapper():
        print("Decor 2")
        func()
    return wrapper

@decor1
@decor2
def test():
    print("Function")

test()


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """This is an example function."""
    pass
print(example.__name__)  # Output: example

def login_required(func):
    def wrapper(user):
        if not user.get("is_logged_in"):
            return "User must be logged in to access this function."
        return func(user)
    return wrapper

@login_required
def view_profile(user):
    return f"Profile of {user['name']}"

user1 = {"name": "Aashir", "is_logged_in": True}
user2 = {"name": "John", "is_logged_in": False}

print(view_profile(user1))
print(view_profile(user2))


square = lambda x: x * x
print(square(5))

x = lambda a, b, c: a + b + c
print(x(5, 10, 15))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

numbers = [1, 2, 3, 4, 5]
results = list(map(lambda x: x * 2, numbers))
print(results)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

total = reduce(lambda a, b: a + b, numbers)
print(total)

students = [
    ("Aashir", 85),
    ("Ali", 92),
    ("Sara", 78)
]

sorted_student = sorted(students, key=lambda x: x[1])
print(sorted_student)

operations = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b
}

print(operations["add"](10, 5))

def factorial(n):
    if (n == 1):
        return 1
    return n * factorial(n - 1)

print(factorial(5))

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(6))

def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

my_list = [11, 2, 30, 33, 23]
print(sum_list(my_list))

def find_max(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        max_of_rest = find_max(nums[1:])
        return nums[0] if nums[0] > max_of_rest else max_of_rest

print(find_max(numbers))
    
def find_max_loop(nums):
    max_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val
    
print(find_max_loop(numbers))