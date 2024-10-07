import re

out = []
regex = re.compile("^([A-F0-9]{2}\-){5}[A-F0-9]{2}$")

while(1):
    str = input()
    if str == ".":
        break
    
    if regex.match(str):
        out.append("true\n")
    else:
        out.append("false\n")

print("".join(out))
