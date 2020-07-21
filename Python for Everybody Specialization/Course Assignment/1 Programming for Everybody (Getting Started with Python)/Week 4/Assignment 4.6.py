def computepay(hour, rate):
   if hour > 40:
        hour = 40+((hour-40)*1.5)
   payment = hour*rate
   return payment

hrs = input("Enter Hours:")
hrs=float(hrs)
rate = input("Enter Rate:")
rate=float(rate)
pay= str(computepay(hrs,rate))
print ("Pay "+pay)