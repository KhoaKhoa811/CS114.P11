matrix = [[0] * 4 for _ in range(4)]

for i in range(4):
    matrix[i] = list(map(int, input().split()))
    
d = input()

def xuLiMang(array):
    b = [i for i in array if i != 0]
    
    temp = []
    check = False
    
    if not b:
        return [0] * 4 
    
    for i in range(len(b)):
        if check:
            check = False
            continue
        if i < len(b) - 1 and b[i] == b[i + 1]:
            temp.append(b[i]*2)
            check = True
        else:
            temp.append(b[i])
            
    while len(temp) < len(array):
        temp.append(0)
        
    return temp

def layCot(index):
    column = [row[index] for row in matrix]
    return column

def thayCotMoi(index, array):
    for i in range(4):
        matrix[i][index] = array[i]

if d == "L":
    for i in range(4):
        mangMoi = xuLiMang(matrix[i])
        matrix[i] = mangMoi
elif d == "R":
    for i in range(4):
        temp = matrix[i]
        temp.reverse()
        mangMoi = xuLiMang(temp)
        mangMoi.reverse()
        matrix[i] = mangMoi
elif d == "U":
    for j in range(4):
        column = layCot(j)
        mangMoi = xuLiMang(column)
        thayCotMoi(j, mangMoi)
elif d == "D":
    for j in range(4):
        column = layCot(j)
        column.reverse()
        mangMoi = xuLiMang(column)
        mangMoi.reverse()
        thayCotMoi(j, mangMoi)
    
    
for i in range(4):
    print(" ".join(map(str, matrix[i])))
    