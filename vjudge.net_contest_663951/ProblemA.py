# author @hossainel
import math

def log2(x): return int(math.log(x)/math.log(2))

for i in range(int(input())):
    b = 2**(log2(int(input())))
    print(b*(b-1))
