#Write a Python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'
s1=input("Enter string 1:")
s2=input("Enter string 2:")
st1=s1[ :2]+s2[2: ]
st2=s2[ :2]+s1[2: ]
print("Your string  1st is:" + st1)
print("your 2ed string is:" + st2)

