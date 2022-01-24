#Write a Python program to convert height (in feet and inches) to
#centimeters.
h_ft=int(input("Hight in feet:"))
h_inch=int(input("Hight in inch:"))
h_inch=h_ft*12
h_cm=(h_inch*2.54)
print("Your Hight is:" +str(h_cm) + "cm")


