my_list = [10, 20, 30, 40, 50]

my_iterator = iter(my_list)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

class EvenNumbers:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max:
            raise StopIteration
        num = self.current
        self.current += 2
        return num

for n in EvenNumbers(10):
    print(n)
