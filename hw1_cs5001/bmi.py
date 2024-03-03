'''
Kangning Li
CS 5001, Spring 2024
Homework 1 - BMI
'''

def main():
    print("Welcome to my simple BMI calculator!")

    height = float(input("What is the subject's height in inches? "))
    weight = float(input("What is the subject's weight in pounds? "))

    print(f"height = {height:.1f} weight = {weight:.1f}")

    bmi = (weight * 0.453592) / (height * 0.0254) ** 2

    print(f"Subject's BMI is {bmi:.1f}")

if __name__ == "__main__":
    main()
    
