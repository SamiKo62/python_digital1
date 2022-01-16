#Write a program that show a Menu 1-4
#1.input a number and print number**3
#2. input 4 IP Address put them in a list and print the list
#3. input 4 DNS adress and put them ib a dictionary with ther ip address
#4. input a string and check if the string is a polindrom
#if the user did not press 1-4 print you have to press 1-4 only
select=input("Chouse 1-4:\n.....\n1.Insert number and ** it by  3\n2.Insert in a list 4 ip address\n3.Insert to a Dictioary 4 DNS\n4 Insert a string and check if its a polindrom\n")
if (select=="1"):
    print("The number is:"+ str((int(input("Enter a Number:" )))**3))
elif(select=="2"):
    list_ip=[]
    list_ip.append(input("Enter IP addres no1:"))
    list_ip.append(input("Enter IP addres no2:"))
    list_ip.append(input("Enter IP addres no3:"))
    list_ip.append(input("Enter IP addres no4:"))
    print("list_ip is:" + str(list_ip))
elif(select=="3"):
    dns_dict={}
    dns_dict.update({input("Enter URL :"):input("Enter IP address:")})
    dns_dict.update({input("Enter URL :"): input("Enter IP address:")})
    dns_dict.update({input("Enter URL :"): input("Enter IP address:")})
    dns_dict.update({input("Enter URL :"): input("Enter IP address:")})
    print(dns_dict)
elif(select=="4"):
      word=input("Enter a word :")
      if(word==word[::-1]):
          print("It is a Polindrom")
      else:
          print("Sorry it is not a polindrom")
else:
     print("You Have to select 1-4 only")