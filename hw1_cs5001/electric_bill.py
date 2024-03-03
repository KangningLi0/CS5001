'''
Kangning Li
CS 5001, Spring 2024
Homework 1 - electric_bill
'''

def main():
    supplier_fee = float(input("What is the supplier fee per kWh? "))
    power_fee = float(input("What is the power fee per kWh? "))
    energy_used = float(input("How many kWh were used this month? "))

    total_bill = energy_used * supplier_fee + energy_used * power_fee

    print(f"Your electric bill this month is ${total_bill:.2f}")

if __name__ == "__main__":
    main()
    
