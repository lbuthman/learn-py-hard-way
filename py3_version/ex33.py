numbers = []


def loopy(toppy, increment):
    i = 0
    while i < toppy:
        print("At the top i is %d." % i)
        numbers.append(i)

        i += increment
        print("Numbers now:", numbers)
        print("At the bottom i is %d." % i)

print("The numbers: ")

for num in numbers:
    print(num)

loopy(10, 2)
