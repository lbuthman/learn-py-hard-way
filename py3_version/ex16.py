from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want to do that, hit Control-C (^C).")
print("If you do want to do that, hit Return.")

input("?")

print("Opening the file ...")
target = open(filename, 'w')

print("Truncating the file. Bye bye now ...")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

result = line1 + '\n' + line2 + '\n' + line3 + '\n'

target.write(result)

print("And that's it! Closing time ...")
target.close()
