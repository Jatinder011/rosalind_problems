def fib(months, offsprings):
    parent = 1
    child = 1
    for y in range(months - 1):
        child, parent = parent, parent + (child * offsprings)
    return child

fib(5, 3)