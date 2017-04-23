from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want to do that, hit Control-C (^C)."
print "If you do want to do that, hit Return."

raw_input("?")

print "Opening the file ..."
target = open(filename, 'w')

print "Truncating the file. Bye bye now ..."
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print "And that's it! Closing time ..."
target.close()
