class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def authenication_check(fun):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            fun(args[0])
    return wrapper


@authenication_check
def blog(user):
    print(f"Hello {user.name}")


obj = User("Arunesh")
obj.is_logged_in = True
blog(obj)



# EXERCISE

def login(fun):
    def wrapper(*args):
        print(f'You called {fun.__name__}{args}')
        print(f'It returned: {fun(args[0], args[1], args[2])}')
    return wrapper

@login
def nums(a, b, c):
    return a*b*c


nums(1, 2, 3)



























