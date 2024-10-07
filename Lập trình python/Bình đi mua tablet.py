import math
n = int(input())

count = 0
t = n ** 2
q = math.isqrt(int(t/2) + 1)

for i in range(1, q):
    a = t - i ** 2
    b = math.isqrt(a)
    if a == b*b and b > i:
        count += 1
        
print(count)