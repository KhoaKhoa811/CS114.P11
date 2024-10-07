n = input()
m = input()

a = ' '.join(n).split(' ')
b = ' '.join(m).split(' ')

if a[1] == '.' and b[0] == '.':
    print("No")
elif a[0] == '.' and b[1] == '.':
    print("No")
else:
    print("Yes")


