import re
text, pattern = input(), input()
m= list(re.finditer("(?=(%s))"%pattern,text))
if not m:
    print((-1,-1))
for i in m:
    print((i.start(1),i.end(1)-1))
