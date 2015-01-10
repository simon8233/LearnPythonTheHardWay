# -*- encoding=UTF-8 -*-

from sys import argv
script , arg1 , arg2 ,arg3 , arg4  = argv

print "The script is called:", script

print "Your first variable is : ", arg1
print "Your second variable is :" , arg2
print "Your third variable is :" , arg3
print "argv.len", len(argv)

for arg in argv:
    print arg
