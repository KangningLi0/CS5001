'''
Kangning Li
CS 5001, Spring 2024
Homework 1 - ATM

Test case #1:
Input: $ 2024
Output: 40 fifties, 1 twenties, 0 tens, 0 fives, 4 ones

Test case #2:
Input: $ 5001
Output: 100 fifties, 0 twenties, 0 tens, 0 fives, 1 ones
'''

def main():
    money = int(input("Welcome to PDQ Bank! Amount to withdraw? $ "))
    print("Cha-ching! You asked for $ " + str(money))
    print("That breaks down to:")

    fifty = money // 50
    money -= fifty * 50
    print(str(fifty) + " fifties")

    twenty = money // 20
    money -= twenty * 20
    print(str(twenty) + " twenties")

    ten = money // 10
    money -= ten * 10
    print(str(ten) + " tens")

    five = money // 5
    money -= five * 5
    print(str(five) + " fives")

    print(str(money) + " ones")

if __name__ == "__main__":
    main()
    
