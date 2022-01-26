#Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
#Sample string : 'Net4U'
#Expected output: {'N': 1, 'e': 1, 't': 2, '4': 1, 'U': 1}
s=input("Enter a string:") #input a string of letters
dict={}  #create a empty dictionary
for i in s:
    dict[i]=s.count(i)
print("Charcter counter",dict)


