hrs = input("Enter Hours:")
h = float(hrs)
if (h>40):
    h= 40+ float((h-40)*1.5)
rate = input("Enter Rate:")
rate= float(rate)
pay= float(rate*h)
print(pay)

