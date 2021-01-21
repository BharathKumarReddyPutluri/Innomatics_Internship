N = set(input().split())
print(all(N > set(input().split()) for _ in range(int(input()))))
