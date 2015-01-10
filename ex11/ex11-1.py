#-*- coding: UTF-8 -*-
# in python 3.1 , with Chineses vaiable is work.
# and python 3.1 , haven't raw_input . just only input()
# clear to write down
print "請問可以有你的手機號碼嗎?" ,
是否 = raw_input()

print "請問你家住哪裡？",
哪裡 = raw_input()
print "中文變數真的可以用嗎？?",
變數判斷 = raw_input()

print "So , 答案是 %r, 住哪 %r and 中文變數可用？%r ." % ( 是否 , 哪裡 , 變數判斷 )
