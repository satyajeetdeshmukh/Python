def add_numbers(*args):
    total = 0
    for x in args:
        total += x
    return total


y = add_numbers(3, 4, 5, 3, 2)

print(y)
