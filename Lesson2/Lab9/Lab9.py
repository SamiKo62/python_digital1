'''
Creat a menue:
1. Dog detailes, dog name, age of a dog *7
2. Friends list, make a list of 5 friends
enter a friend and cheak if he is in the list
3. N azzert input a name and calculate azzert
'''
while (True):
 select=input(" please select from menue :\n1. Dog detailes: \n2. Friends list: \n3. N.Azzert: \n4. Exit \n")
 if(select=="1"):
    name=input(" Enter the name of the dog: ")
    age=input(" Enter the age of the dog: ")
    print("Dog name is:" +str (name) + "\n  Dog age is:" + str(int(age)*7))
 elif(select=="2"):
    list_name=[]
    list_name.append(input("Enter friend no1:"))
    list_name.append(input("Enter friend no2:"))
    list_name.append(input("Enter friend no3:"))
    list_name.append(input("Enter friend no4:"))
    list_name.append(input("Enter friend no5:"))
    print("My friends" + str(list_name))

 elif(select=="3"):
    num=int (input("Enter numnber to calculate factorial:"))
    factorial = 1
    # check if the number is negative, positive or zero
    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)
 elif(select =="4"):
     print("Bye Bye")
     break
 else:
     print("Enter from menue 1-4 only")


