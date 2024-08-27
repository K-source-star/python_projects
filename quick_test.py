#Question 1: Basic Data Types and Variables
x = 25
y = x ** 2
print(y)

a = 5
b = 2.0
c = a // b
print(c)

#Question 2: Control Flow (If Statements)
"""
value = (input("Enter a number: "))
number = int(value)
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")
""" 
def check_number():

    #This function prompts the user to enter a number and checks whether it is positive, negative, or zero.
  

    try:
        # Prompt the user to enter a number
        number = float(input("Please enter a number: "))

        # Check if the number is positive, negative, or zero
        if number > 0:
            print("The number is positive.")
        elif number < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")
    
    except ValueError:
        # Handle the case where the input is not a valid number
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    check_number()

#Question 3: Loops

for number in range(2, 21, 2):
    print (number)

number = None 

while number != 0:
    number = int(input("Please enter a number (0 to stop): "))

#Question 4: Functions
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
  
#Question 5: Lists and List Comprehensions

odd_numbers = [num for num in range(10, 31) if num % 2 != 0]
print(odd_numbers)
odd_numbers.append(100)
