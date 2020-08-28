C = input("Enter temperature in celsius: ")
c = round(float(C), 2)
F = (float(C)*9/5+32)

print(str(c) + chr(176) +" in Celsius is equivalent to " + str(F) +  chr(176)+" Fahrenheit.")