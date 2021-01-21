# Enter your code here. Read input from STDIN. Print output to STDOUT
E,e = int(input()),input().split()
F,f = int(input()),input().split()
a=set(e)
b=set(f)
c=a.symmetric_difference(f)
print(len(c))
