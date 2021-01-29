import re
N = int(input())
for i in range(N):
    if re.match(r'^[987]\d{9}$',input()):
        print("YES")
    else:
        print("NO")
