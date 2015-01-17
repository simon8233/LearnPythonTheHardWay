# -*- encoding=UTF-8 -*-
from __future__ import print_function
def print_recursive (print_object,ident=False,need_tabs_in_print=0):
    print (ident)
    """ This is a function , print multiple list in list."""
    for iter_obj in print_object:        
        if isinstance(iter_obj,list):
            print_recursive(iter_obj,ident,need_tabs_in_print+1)
        else:
            if ident:
                for i in range(need_tabs_in_print):
                    print("\t", end='')
            print(iter_obj)

"""case = ['movie',['apple',['aa','bb'],'banana'],'orange']
print_recursive(case,True)
print_recursive(case,False)
#print_recursive(case,False,100)
#print_recursive(case,True,4)"""
