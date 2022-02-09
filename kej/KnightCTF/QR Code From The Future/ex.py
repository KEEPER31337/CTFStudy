arr = ["X","P","G","S","{","D","E","_","p","b","q","r","_","t","b","g","_","r","i",
"b","y","i","r","q","_","s","e","b","z","_","f","g","n","g","v","p","_","g","b",
"_","q","l","a","n","z","v","p","}"]
exclude = ["{","}","_"]

for i in arr:
    if i in exclude:
        print(i, end='')
    elif (i.isupper() and ord(i)-13 < ord('A')) or (i.islower() and ord(i)-13 < ord('a')):
        print(chr(ord(i) + 13), end='')
    else:
        print(chr(ord(i) - 13), end='')