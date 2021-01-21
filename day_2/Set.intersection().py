# Enter your code here. Read input from STDIN. Print output to STDOUT
E,e = int(input()),input().split()
F,f = int(input()),input().split()
a=set(e)
b=set(f)
c=a.intersection(f)
print(len(c))
