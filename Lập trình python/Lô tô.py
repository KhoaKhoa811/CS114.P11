matrix = [[0] * 3 for _ in range(3)]

def contains(a, b):
    for i in range(len(a)):
        if a[i] not in b:
            return 0
    return 1

for i in range(3):
        matrix[i] = list(map(int, input().split()))
        
N = int(input())
mang = []

for i in range(N):
    val = int(input())
    mang.append(val)
    
check = []

a = 1

for i in range(3):
    for j in range(3):
        if matrix[i][j] in mang:
            check.append(a)
        a = a + 1    
            
if contains([1, 2, 3], check) or contains([4, 5, 6], check) or contains([7, 8, 9], check):
    print("Yes")
elif contains([1, 4, 7], check) or contains([2, 5, 8], check) or contains([3, 6, 9], check):
    print("Yes")
elif contains([1, 5, 9], check) or contains([3, 5, 7], check):
    print("Yes")
else:
    print("No")