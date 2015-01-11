# -*- encoding=UTF-8 -*-

def add(i):
    
    if i == 1:
        return 1
    else:
        return i + add(i-1)

print add(100)

