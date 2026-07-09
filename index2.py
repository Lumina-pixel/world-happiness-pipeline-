sentence = input("enter a string: ")

for ch in sentence.lower():
    if ch in "aeiou":
        print("string has a vowel")
        break
else:
    print("no vowels")

