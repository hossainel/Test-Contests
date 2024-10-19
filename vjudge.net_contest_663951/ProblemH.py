# author @hossainel
n, x = map(int, input().split())
s = input()
t = input()

op = x%n
c = 0

for i in range(len(s)):
    d = (i-op+n)%n
    if s[d]!=t[i]: c = c + 1
print(c)
