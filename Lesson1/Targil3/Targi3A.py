#Deviding a 4 digit Number to Alfim,Meot.Asarot,Ahadot
num = int(input("Enter 4 digit number:"))
print("Alafim=" + str(num // 1000))
print("Meot=" + str((num % 1000) // 100))
print("Asarot=" + str((num % 100) // 10))
print("Ahadot=" + str(num % 10))
