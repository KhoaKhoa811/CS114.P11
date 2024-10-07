import math

def laSoNguyenTo(num):
    if num <= 1: 
        return 0
  
    if num == 2: 
        return 1
  
    if num % 2 == 0:
        return 0
  
    for i in range(3, int(math.sqrt(num))+1, 2):
        if (num % i) == 0: 
            return 0
  
    return 1

def mangSoNguyenTo(num):
    if num < 2: 
        return []

    mangSoNguyenTo = []
    for i in range(2, int(num/2) + 1):
        if(laSoNguyenTo(i)):
            mangSoNguyenTo.append(i)

    return mangSoNguyenTo

n = int(input())

mang = mangSoNguyenTo(n)

result = 0

for i in mang:
    temp = n - i
    if laSoNguyenTo(temp):
        result += 1
        
print(result)
