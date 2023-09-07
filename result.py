def main():
    dollars = dollars_to_float(input("How much was the meal? ").rstrip())
    percent = percent_to_float(input("What percentage would you like to tip? ").rstrip())
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
   
    try: 
        dollars_float = float(d)
        return dollars_float
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return 0.0  

def percent_to_float(p):
    
    try:
        percent_float = float(p) / 100.0  
        return percent_float
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return 0.0  
main ()