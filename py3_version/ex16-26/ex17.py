from sys import argv
# from os.path import  exists

script, from_file, to_file = argv

print("Copying file %s to %s" % (from_file, to_file))

# in_file = open(from_file)
# in_data = in_file.read()
#
# print("The input file is %d bytes long." % len(in_data))
#
# print("Does the output file really exist? %r" % exists(to_file))
#
# print("Ready, hit RETURN to continue or Control-C (^C) to quit.")
# input()
#
# out_file = open(to_file, 'w')
# out_file.write(in_data)

with open(from_file) as in_file:
    with open(to_file, 'w') as out_file:
        for line in in_file:
            out_file.write(line)

print("Alrighty then! Done ...")
in_file.close()
out_file.close()
