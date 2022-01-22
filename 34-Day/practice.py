# age: int
# home: bool
# salary: float
# name: str
#
# age = 22
# home = True
# salary = 5345
# name = "hello"

def demo(age: int):
    if age >= 18:
        rto = "Drive"
    else:
        rto = "Not Drive"
    return rto


print(demo(43))


def salary(payment: int) -> float:
    if payment >= 1000:
        # get_payment = "Rich person"
        get_payment = payment * 1.2
    else:
        # get_payment = "Poor person"
        get_payment = payment * 1.0
    return get_payment


print(salary(225))
