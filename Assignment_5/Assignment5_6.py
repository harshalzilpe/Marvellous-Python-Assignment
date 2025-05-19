""" 
    Celsius to Fahreheit Converter
    Accept temperature in Celsius and convert it to Fahrenheit using the formula:
    F = (C * 9/5) + 32
    Input:
    Enter temperature in Celsius: 25
    Output:
    Temperature is Fahrenheit is 77.0°F.
"""
def Converter(C):
    F = (C * 9/5) + 32
    return F

def main():
    no = float(input("temperature in Celsius: "))
    
    ret = Converter(no)
    print(f"Temperature is Fahrenheit is {ret}°F.")
    
if __name__ == "__main__":
    main()
""" 
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_6.py
    temperature in Celsius: 25
    Temperature is Fahrenheit is 77.0°F.
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_6.py
    temperature in Celsius: 46.2
    Temperature is Fahrenheit is 115.16°F.
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_6.py
    temperature in Celsius: -1.5
    Temperature is Fahrenheit is 29.3°F.
    macbook@Macbooks-MacBook-Pro Assignment_5 % python3 Assignment5_6.py
    temperature in Celsius: -25
    Temperature is Fahrenheit is -13.0°F.
    macbook@Macbooks-MacBook-Pro Assignment_5 %   
"""