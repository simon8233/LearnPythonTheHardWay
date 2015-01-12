# -*- encoding=UTF-8 -*-

def ex33 (loop_size,increment):
    numbers = []
    i = 0 
    for i in range(0,10,increment):
        print "At the top i is %d" %i
        numbers.append(i)
        print "Numbers now: " , numbers
        print "At the bottom i is %d " % i
    return numbers 
    

for num in ex33(10,2):
    print num 
