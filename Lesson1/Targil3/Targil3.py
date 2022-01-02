#Taking  a number and devided it to Alfim, Meot,Asrot,Ahdot
num=9922
num1=num//1000
num2=num1*1000
num2=num-num2
num2=num2//100
num3=num2*100
num3=(num1*1000)+num3
num3=num-num3
num3=num3//10
num4=(num1*1000)+(num2*100)+(num3*10)
num4=num-num4
num4=num4//1
print("your Number is: " + str(num))
print("your Alafim is: " + str(num1))
print("your Meot is: " + str(num2))
print("your Asarot is: " + str(num3))
print("your Ahadot is: " + str(num4))
