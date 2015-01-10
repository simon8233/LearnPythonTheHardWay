#!/usr/bin/python
# -*- encoding: utf-8 -*-

import os


def main():

    print "Hello World"
    print "中文輸入的哈囉 世界"

    print foo (43,25)

    print "=" * 10;
    print "這將執行"+os.getcwd();

    counter = 0
    counter += 1

    food = ['apple','banana','strawberry','blueberry']
    for str in food: 
        print str 

    for i in range(10):
        print i
def foo(var1 , var2):

    result = var1 + var2

    if result < 50:
        print '這個'
    elif (result >= 50) and ((var1 == 42)) or ((var2 == 24)):
        print '那個'
    else:
        print '嗯......'

    return result  




if __name__ == '__main__':
    main() 