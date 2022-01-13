def first(a, b, c):
    print(a, b, c)
first(1, 2, 3)


def second(a=1, b=2, c=3):
    print(a, b, c)
second()


def third(a=1, b=2, c=3):
    print(a, b, c)
third(5, 6, 7)



def four(a=1, b=2, c=3):
    print(a, b, c)
four(11)

def five(a=1, b=2, c=3):
    print(a, b, c)
five(11, c=12)

