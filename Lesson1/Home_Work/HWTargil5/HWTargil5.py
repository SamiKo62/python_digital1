#Write a Python program that accepts an integer (n) and computes the
#value of n+nn+nnn.
#Sample value of n is 5
#Expected Result : 615
n=int(input("Enter an integer number :"))
a=str(n)
a1=a+a
print(a1)
a2=a+a+a
print(a2)
sum=n+int(a1)+int(a2)
print(sum)














