# -*- encoding = utf-8 -*-

name = 'Zed A. Shaw'
age = 35
height = 74 # inches.
weight = 180 # lbs.
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


print "Let's talk about %s." % name
print "He's %d inches tall. " % height
print "He's %d pounds heavy." % weight
print "actually that's not too heavy."

print "He 's got %s eye and %s hair" %(eyes , hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this Line is tricky, try to get it exactly right.

print "If I add %d , %d,  and %d I get %d. " %(
        age , height , weight , age + height + weight)