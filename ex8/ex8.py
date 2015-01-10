# -*- encoding=utf-8 -*_

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter , formatter , formatter , formatter )
print formatter % (
        " I had this thing.",
        "That you could type up right.",
        "But it didn't sing.",
        "so I said good night."
)
formatter = "%s %s %s %s"
print formatter % ("中文輸入","被小覷了","你還不努力","準備吃屎!?")
