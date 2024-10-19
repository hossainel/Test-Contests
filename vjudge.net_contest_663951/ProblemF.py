# author @hossainel
a = int(input())
ay = [int(i) for i in input().split()]

m = 2
for i in ay:
    k = 0
    for j in range(2,max(ay)+1):
        t = sum([1 for i in ay if i%j==0])
        if (t>=k): k = t; m = j
    
print(m)
        
    
