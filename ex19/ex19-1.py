# -*- encoding=UTF-8 -*-

def swap(a,b):
    if isinstance(a,int) and isinstance(b,int):
        tmp = b
        b = a
        a = tmp
        print "a = %d , b =%d" % ( a, b)
    elif isinstance(a,float) and isinstance(b,float):
        tmp = b
        b = a
        a = tmp
        print "a = %f , b =%f" % ( a, b)
    elif isinstance(a,basestring) and isinstance (b,basestring):
        tmp = "string"
        tmp += b 
        b = "string"+a
        a = tmp
        print "a = %s , b =%s" % ( a, b)
    elif isinstance(a,int) and isinstance(b,float):
        tmp = b
        b = a
        a = tmp
        print "a = %f , b = %d" % (a,b)
    elif isinstance(a,int) and isinstance(b,basestring):
        tmp = "string"
        tmp += b
        b = a
        a = tmp
        print "a = %s , b = %d" % (a,b)

swap(1,2)
swap(1.0,2.0)
swap("1","2")
swap(1,2.0)
swap(1,"2")
