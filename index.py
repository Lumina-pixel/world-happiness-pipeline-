s = input("enter a string: ")

result = ""
cap = True

for ch in s:
    if ch==" ":
        result+=ch
        cap = True
    else:
        if cap:
            result += ch.upper()
            cap = False
        else:
            result += ch
    
print(result)