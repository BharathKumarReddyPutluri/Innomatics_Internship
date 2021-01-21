K = int(input())
R = input().split()
S = set()
M = set()
for i in R:
    if i not in S:
        S.add(i)
    else:
        M.add(i)
print((S.difference(M)).pop())
                
