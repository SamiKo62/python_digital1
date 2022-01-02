tomat= int(input("How many tomaatos:"))
tomat=tomat*3
cuc=int(input("How many cucumber:"))
cuc=cuc*2
kola=int(input("How many cola bottles:"))
kola=kola*5
chik=int(input("How many Kg of chicken:"))
chik=chik*20
print("Your shopping cart beffor Tax:" +str(tomat+cuc+kola+chik))
print("Your shopping cart with 17% Tax is: " +str("%.2f"%((tomat+cuc+kola+chik)*1.17)))









