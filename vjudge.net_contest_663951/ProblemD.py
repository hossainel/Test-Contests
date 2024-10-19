import math

def line(a,b,c,d): return math.sqrt((a-c)**2+(b-d)**2)
    

def line_pos(a,b,c,d,e,f):
    A = d-b
    B = a-c
    C = 0 - b * B - A * a
    dist = (A*e + B*f + C)/math.sqrt(A*A+B*B)
    if dist==0.0: return "TOUCH"
    elif dist<0: return "LEFT"
    else: return "RIGHT"

for _ in range(int(input())): print(line_pos(map(int, input().split())))
    
