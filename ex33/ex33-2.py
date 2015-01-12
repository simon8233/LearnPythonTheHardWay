# -*- encoding=UTF-8 -*-

def ex33 (loop_size,increment):
    numbers = []
    i = 0 
    while i < loop_size:
        print "At the top i is %d" %i
        numbers.append(i)
        i = i + increment
        print "Numbers now: " , numbers
        print "At the bottom i is %d " % i
    return numbers 
    
#print "The number: "

for num in ex33(10,2):
    print num 
