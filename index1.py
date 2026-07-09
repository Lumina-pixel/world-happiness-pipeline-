s = input("enter a string: ")
rev = ""
for ch in s:
    rev = ch+rev
print(rev)

if s==rev:
    print("palindrome")
else:
    print("not palindrome")
    