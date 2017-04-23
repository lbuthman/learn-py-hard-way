def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r - arg2: %r" % (arg1, arg2))


def print_two_again(arg1, arg2):
    print("arg1: %r - arg2: %r" % (arg1, arg2))


def print_one(arg):
    print("I got one! %r" % arg)


def print_none():
    print("Dang. I got nuthin'")


print_two("peanut butter", "jelly")
print_two_again("peanut butter", "jelly")
print_one("I hate that song.")
print_none()
