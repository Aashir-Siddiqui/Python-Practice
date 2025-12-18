numbers = {1, 2, 2, 3, 4, 4}
print(numbers)   # {1, 2, 3}

s = set({1,3,3,4})
print(s)

# print(numbers[0])  ❌ error
print(3 in numbers)
numbers.add(5)
print(numbers)
numbers.update([6, 7, 8])
print(numbers)
numbers.remove(3)
print(numbers)
numbers.discard(7)
print(numbers)
print(numbers.pop())
print(numbers)

for value in numbers:
    print(value)


a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a | b)

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(a - b)

print(a.symmetric_difference(b))

fs = frozenset([1, 2, 3])

# fs.add(4)  ❌

x = {1, 2}
y = {1, 2, 3}

print(x.issubset(y))  # True

print(y.issuperset(x))  # True

print(x.isdisjoint({4, 5}))  # True

emails = ["a@test.com", "b@test.com", "a@test.com"]
unique_emails = set(emails)
print(unique_emails)
