# Iterables? Which can be looped -> Lists, tuples, dictionaries, sets, strings, ranges. | does not have a __next__ method
# Iterator? Has a __next__ method
# All sequences are iterables
nums = [5, 10, 20]  # iterable
print(nums)
print(dir(nums))  # All methods available for nums


nums_iter = nums.__iter__()  # converts nums to iterator | Iterable -> iterator
print(
    nums_iter
)  # All methods available for # raise ValueError # <list_iterator object at 0x00000272BDE4BFD0>
# Bad practice to use dunder methods

nums_iter2 = iter(nums)  # Iterable -> iterator
# print(nums_iter2)  # <list_iterator object at 0x00000272BDE4BFA0>
# print(dir(nums_iter2))  # now has the __next__ method

# Conclusion: All iterators are iterables | But not the other way around
# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))

# Use while loop to iterate over all iterators
try:
    while next(nums_iter):
        print(next(nums_iter2))
except StopIteration:
    pass

# range(0, 100_000_000, 1) list with 100 million lots of memory
# Iterator remember one thing at a time | save memory
# __next__ & __iter__


class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):  # Its already an iterator
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            self.start += 1
            return self.start - 1


# Generator - clean | infinite_integer() -> iterator
# We prefer this because it is more verbose and concise than the methods in MyRange above
def infinite_integers():
    n = 0
    while True:
        yield n  # The value returned by infinite_integer | pauses here until next() is called
        n += 1


# When it has next


# Keep track of two numbers
def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        c = a + b
        a = b
        b = c


if __name__ == "__main__":
    print("--------------------------------------")
    x = MyRange(1, 5)
    # print(next(x))
    # print(next(x))
    # print(next(x))

    integers = infinite_integers()

    # print(next(integers))
    # print(next(integers))
    # print(next(integers))
    # print(next(integers))

    # Fibonacci sequence
    # 0 1 | 1 2 3 5 8 13 21 34 55
    for num in fib(10):
        print(num)
