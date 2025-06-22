def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
def main():
    while True:
            try:
                 n= input("enter a temperature and its unit (e.g., '25 C' or '77 F')")
                 value,unit=n.split()
            
                 tempurature=float(value)
                 unit=unit.lower()
                 
            except ValueError:
                 print("valuError")
                 continue
            try:
                 if unit not in ("c","f"):
                      print("invslid unit")
            except TypeError:
                 print("type error")
                 continue

            if unit=="c":
                res= celsius_to_fahrenheit(tempurature)
                print("fahrenheit: ",res)
            else:
                res=fahrenheit_to_celsius(tempurature)
                print("celsius: ",res)
                 
main()
