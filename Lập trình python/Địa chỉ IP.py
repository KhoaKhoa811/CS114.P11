
def valid(str):
    length = len(str)
    if length > 3:
        return False
    
    if str[0] == "0" and length > 1:
        return False
    
    if int(str) > 255:
        return False
    
    return True

def update(str, current, list, result):
    substr = str[current + 1 : len(str)]
    
    if valid(substr):
        list.append(substr)
        result.append(".".join(list))
        list.pop()
    

def timDiaChiIP(str, previous, dots, list, result):
    length = len(str)
    
    for current in range(previous + 1, min(length - 1, previous + 4)):
        substr = str[previous + 1 : current + 1]
        if valid(substr):
            list.append(substr)
            
            if dots - 1 == 0:
                update(str, current, list, result)
            else:
                timDiaChiIP(str, current, dots - 1, list, result)
                
            list.pop()
        

str = input()
result = []
list = []
timDiaChiIP(str, -1, 3, list, result)
if len(result) != 0:
    print("\n".join(result))
