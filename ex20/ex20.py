# -*- encoding=UTF-8 -*-

from sys import argv

script , input_file = argv
line_count = 0

def print_all(f):
    print f.read()
def rewind(f):
    f.seek(0)

def print_a_line(f):
    global line_count
    line_count += 1
    print line_count , f.readline()

current_file = open(input_file)


print "First let's print the whole file:\n"

print_all(current_file)
# because print_all , let's file pointer go to end.
# using seek function go back head.
print "Now let's rewind , kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

print_a_line(current_file)
print_a_line(current_file)
print_a_line(current_file)
