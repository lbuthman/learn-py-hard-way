
def add(a, b):
    print("Adding %d + %d" % (a, b))
    return a + b


def subtract(a, b):
    print("Subtract %d - %d" % (a, b))
    return a - b


def multiply(a, b):
    print("Multiply %d * %d" % (a, b))
    return a * b


def divide(a, b):
    print("Divide %d / %d" % (a, b))
    return a / b

print("Let's do some Math with fun functions!")

age = add(30, 5)
height = subtract(72, 6)
weight = multiply(85, 2)
iq = divide(120, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

print("Here's a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("Roll that data into some dough and it becomes:", what, "- Bet you can't do that in your head.")
