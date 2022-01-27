#Write a Python program to count repeated characters in a string.
#Sample string: 'thequickbrownfoxjumpsoverthelazydog'
#Expected output :
#o 4
#e 3
#u 2
#h 2
#r 2
#t 2

s1 = input("Enter a string:")
print("Duplicate charcters in the string: ")
for i in range(0, len(s1)):
    count = 1
    for j in range(i + 1, len(s1)):
        if (s1[i] == s1[j] and s1[i] != ' '):
            count = count + 1
            s1 = s1[:j] + '0' + s1[j + 1:]
    if (count > 1 and s1[i] != '0'):
        print(s1[i], " - ", count)

