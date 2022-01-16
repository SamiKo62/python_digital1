#Dictionary exrcise
#Make a dictionary with 5 name ich name have a sum of money
#calculate the sum of the first name and the kast name
#and add aname the his money will be the sum that we calculate
#print the length os entries end check id idan is in the dictionary
my_dict={"David":1200,"Sam":1000,"Noa":1700,"Ofer":950,"Avi":2700}
print(my_dict)
summery=my_dict["David"]+my_dict["Avi"]
print("The sum of 1st name witih last name is:"  +  str(summery))
my_dict["Dudu"]=summery
print(my_dict)
print("length of dictionary:" + str(len(my_dict)))
print("idan" in my_dict)


