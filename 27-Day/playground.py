def add(*args):
    # print(args[0])
    sum = 0
    # for n in args:
    #     print(n)
    for num in args:
        sum += num
    return sum


print(add(1, 2, 3, 4, 5))
# print(add(3, 5, 6, 2, 1))


# # 2 EXAMPLE
# def names(*args):
#     for name in args:
#         print(name)
# names('Rohan', 'Mohan', 'Sohan', 'Dohan')


def calculate(n, **kwargs):
    # print(kwargs)
    # print(kwargs['add'])
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=5, multiply=10)



class Demo:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')

data = Demo(make='BMW')

print(data.model)





































