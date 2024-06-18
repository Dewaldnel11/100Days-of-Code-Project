def add(*args):
    print(args)
    print(type(args))

    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6, 7, 23, 33, 45, 56))

def calculate(**kwargs):

    calculate(add=3, multiply=5)

calculate()