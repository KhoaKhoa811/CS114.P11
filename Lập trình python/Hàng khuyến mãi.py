import re

a = list(map(int, input().split()))

b = []

for i in range(len(a)):
    b.append(input())
    
m = input()
m = float(m)

temp = 0
for i in range(len(a)):
    if "lower than in-store" in b[i]:
        match = re.findall(r'([\d\.]+)', b[i])
        temp += a[i] * (1 - float(match[-1][0]) / 100)
    elif "higher than in-store" in b[i]:
        match = re.findall(r'([\d\.]+)', b[i])
        temp += a[i] * (1 + float(match[-1][0]) / 100)

if m >= temp:
    print("true")
else:
    print("false")