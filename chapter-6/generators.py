import sys

def simple_gen():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")
    yield 3

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))

def count_up(n):
    for i in range(1, n + 1):
        yield i

for num in count_up(5):
    print(num)

list_data = [i for i in range(1000000)]
gen_data = (i for i in range(1000000))

print(sys.getsizeof(list_data))
print(sys.getsizeof(gen_data))

def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1

gen = infinite_numbers()
print(next(gen))
print(next(gen))

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for f in fibonacci(7):
    print(f)

def filter_even(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

def square(nums):
    for n in nums:
        yield n * n

nums = range(10)
result = square(filter_even(nums))

print(list(result))
