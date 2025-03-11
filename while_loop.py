'''
#1.Write a program to generate a Multiplication table using While Loop 
def multiplication_table(number, limit=10):
    """Generates a multiplication table for a given number up to a specified limit."""
    i = 1
    while i <= limit:
        print(f"{number} x {i} = {number * i}")
        i += 1
    print("-" * 20)  # Separator for better readability

# Generate tables for 5, 12, and 17
multiplication_table(5)
multiplication_table(12)
multiplication_table(17)

'''












'''
#Write a program to generate numbers from 1 to 10

for i in range(1, 11):
    print(i)

'''








#Write a program to generate only even numbers from 1 - 100 (Combination of While Loop  and If Condition) 
'''
num = 1  # Start from 1

while num <= 100:  # Loop until 100
    if num % 2 == 0:  # Check if the number is even
        print(num)
    num += 1  # Increment the number

'''
#Write a program to generate only odd numbers from 1 - 100 (Combination of While Loop  and If Condition) 

