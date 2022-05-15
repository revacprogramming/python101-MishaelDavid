
def computepay(hours, rate):
    if hours > 40:
        overtime = (hours-40)*(rate*1.5)
        pay = (40*rate)+overtime      
    else:
        pay = (hours*rate)
    return pay    

h = float(input("Enter hours: "))
r = float(input("Enter rate: "))
        
t = computepay(h,r)

print(t)