#Write a Python program to sum all the items in a list.

l=input("Enter a list of numbers:") #Enter a list of numbers spareted by space
list=l.split()# spliting the list for each number
sum=0 # start sumarize from 0
for i in list:# start from beging of the list
    sum+=int(i) #Tack the first element add it to the second elment and ener it to sum and so on
print("The sum of the numbers in list : ",sum)






