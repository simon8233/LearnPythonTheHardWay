# -*- encoding=UTF-8 -*-


#this one is like your scripts with argv

def print_two (*args):
    arg1,arg2 = args
    print "arg1: %r, arg2: %r" %(arg1,arg2)
def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" %(arg1,arg2)
def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothin'." 

def function_is_important():
    print "function is important within no argv"
def function_is_important(*argv):
    print "function is important with *argv"
def function_is_important(arg1,arg2):
    print "function is important with arg1 and arg2"

function_is_important("Zed","Shaw")
function_is_important("Zed","Shaw")
#function_is_important("First")
function_is_important()
