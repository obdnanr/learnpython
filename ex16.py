from sys import argv

script, filename = argv

print '''we;re going to erase %r." '''% filename
print '''If you don't want that hit ctrl-c (^C).
If you don want that, hit RETURN.'''

raw_input("?")

print "opening the file..."

print "opening the file.."
target = open(filename, 'w')

print "truncating the file. goodbye!"
target.truncate()

print "now i'm going to ask you for three lines>"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and finally, we close it."
target.close()
