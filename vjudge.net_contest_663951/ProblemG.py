# author @cwswastik
t = int(input())

for _ in range(t):
    n, x = map(int,input().split())
    b = list(map(int,input().split()))
    
    def check(cost):
        c = [b[0] + cost]
        for i in range(1, n):
            if b[i] - cost > c[i-1] + x:
                return False, []
            f = min(b[i] + cost, c[i-1] + x)
            c.append(f)

        return True, c
    
    l = 0
    r = 10**9

    
    while l < r:
        m = (l+r)//2
        if check(m)[0]:
            r = m
        else:
            l = m + 1

    print(l)
    print(*check(l)[1])
        
