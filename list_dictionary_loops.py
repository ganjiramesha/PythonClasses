# Write a program that takes a sentence as input from the user and computes the frequency of each letter. Use a dictionary to maintain the count.
'''
# Get input from user
sentence = input("Enter a sentence: ")

# Initialize an empty dictionary to store letter frequency
letter_frequency = {}

# Loop through each character in the sentence
for char in sentence:
    # Consider only alphabetic characters
    if char.isalpha():
        char = char.lower()  # Convert to lowercase for case insensitivity
        letter_frequency[char] = letter_frequency.get(char, 0) + 1

# Print the letter frequency
print("Letter Frequency:")
for letter, count in letter_frequency.items():
    print(f"{letter}: {count}")

'''









#Write a function that takes a number as an input parameter and returns the corresponding text in words, for example, on input 452, the function should return ‘Four Five Two’. Use a dictionary for mapping digits to their string representation. 
'''
def number_to_words(num):
    # Dictionary to map digits to words
    digit_map = {
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
        '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
    }
    
    # Convert number to string and map each digit
    return ' '.join(digit_map[digit] for digit in str(num))

 
'''




#Write a function to multiple two non - negative numbers by repeated addition. For example 7 * 5 =  7 + 7 + 7 + 7 + 7
'''
def multiply_by_addition(a, b):
    result = 0
    for _ in range(b):  # Add 'a' to result 'b' times
        result += a
    return result

# Example usage
num1 = int(input("Enter first non-negative number: "))
num2 = int(input("Enter second non-negative number: "))

print(f"{num1} * {num2} = {multiply_by_addition(num1, num2)}")

'''




#Function that returns the sum of digits of a number, passed to it as an argument. Eg. 520 should return 7
'''
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10  # Extract the last digit and add to total
        num //= 10  # Remove the last digit
    return total

# Example usage
num = int(input("Enter a number: "))
print(f"Sum of digits of {num} is {sum_of_digits(num)}")

'''



#Write a short Python function that takes a positive integer n and returns the sum of the squares of all the even positive integers smaller than n.
'''
def sum_of_even_squares(n):
    return sum(i**2 for i in range(2, n, 2))

# Example usage
n = int(input("Enter a positive integer: "))
print(f"Sum of squares of even numbers less than {n} is {sum_of_even_squares(n)}")


# Write a short Python function, minmax(data), that takes a list of three or more numbers, and returns the smallest and largest numbers. 
def minmax(data):
    if len(data) < 3:
        return "List must contain at least three numbers"
    return min(data), max(data)

# Example usage
numbers = [12, 5, 34, 89, 2, 45]
smallest, largest = minmax(numbers)
print(f"Smallest: {smallest}, Largest: {largest}")


# Write a Short Python Function that takes a sequence of integer values and determines if there is a distinct pair of consecutive numbers in the sequence whose product is even
def has_even_product_pair(sequence):
    for i in range(len(sequence) - 1):
        if (sequence[i] * sequence[i + 1]) % 2 == 0:
            return True
    return False

# Example usage
numbers = [3, 7, 5, 2, 9]
print(has_even_product_pair(numbers))  # Output: True

numbers2 = [1, 3, 5, 7]  
print(has_even_product_pair(numbers2))  # Output: False


 Write a short Python program that takes two lists a and b of length n storing int values, and returns the dot product of a and b. 
That is returns an list c of length n such that c[i] = a[i].b[i] for  i = 0, .. n-1
Eg:

Input
a = [2, 3, 4, 6, 7]
b = [3, 4, 2, 3, 1]

Output

c = [6, 12, 8, 18, 7]

def dot_product(a, b):
    return [a[i] * b[i] for i in range(len(a))]

# Example usage
a = [2, 3, 4, 6, 7]
b = [3, 4, 2, 3, 1]

c = dot_product(a, b)
print("c =", c)




#Write a  function that takes a list as a parameter and returns True if there are duplicate elements in the list 
Eg:  [ 1, 2, 3, 4, 4, 5 ] this input should produce True, on the other hand [ 1, 2, 3, 4, 5 ] should produce False. 
def has_duplicates(lst):
    return len(lst) != len(set(lst))

# Example usage
print(has_duplicates([1, 2, 3, 4, 4, 5]))  # Output: True
print(has_duplicates([1, 2, 3, 4, 5]))     # Output: False



#Write a function that takes a list as a parameter and returns the sum of all odd number elements in that list.
def sum_of_odds(lst):
    return sum(num for num in lst if num % 2 != 0)

# Example usage
print(sum_of_odds([1, 2, 3, 4, 5]))  # Output: 9 (1 + 3 + 5)
print(sum_of_odds([2, 4, 6, 8]))     # Output: 0 (No odd numbers)



#Implement a function that flattens a nested list (e.g., [[1, 2], [3, 4]] → [1, 2, 3, 4]).
def flatten_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

# Example usage
nested = [[1, 2], [3, 4], [5, [6, 7]]]  # This contains deeper nesting
print(flatten_list(nested))  # Output: [1, 2, 3, 4, 5, [6, 7]] (Shallow flattening)

# Other Important use Cases: 

#Write a function to determine if an object is undergoing uniform or non-uniform motion given a list of positions over time. (Mechanics)
def check_motion_type(positions, time_intervals):
    if len(positions) != len(time_intervals):
        return "Error: Mismatch in positions and time intervals length."

    velocities = []
    for i in range(1, len(positions)):
        velocity = (positions[i] - positions[i - 1]) / (time_intervals[i] - time_intervals[i - 1])
        velocities.append(velocity)

    # Check if all velocities are the same
    if all(v == velocities[0] for v in velocities):
        return "Uniform Motion"
    else:
        return "Non-Uniform Motion"

# Example usage
positions = [0, 10, 20, 30, 40]  # Position at different time intervals
time_intervals = [0, 2, 4, 6, 8]  # Time values

print(check_motion_type(positions, time_intervals))  # Output: Uniform Motion

positions = [0, 10, 22, 35, 50]  # Changing velocity
print(check_motion_type(positions, time_intervals))  # Output: Non-Uniform Motion


#Given a list of daily stock prices, write a program to calculate the average stock price. (Finance)
def average_stock_price(prices):
    if not prices:
        return "Error: Price list is empty"
    
    avg_price = sum(prices) / len(prices)
    return round(avg_price, 2)  # Rounding to 2 decimal places

# Example usage
stock_prices = [150.5, 152.3, 148.9, 153.8, 151.2]  # Example daily stock prices
print("Average Stock Price:", average_stock_price(stock_prices))

#Implement a function to calculate the return on investment (ROI) given an initial and final list of stock prices. (Finance)
def calculate_roi(initial_prices, final_prices):
    if len(initial_prices) != len(final_prices) or not initial_prices:
        return "Error: Invalid input lists"

    roi_list = []
    for i in range(len(initial_prices)):
        roi = ((final_prices[i] - initial_prices[i]) / initial_prices[i]) * 100  # ROI formula
        roi_list.append(round(roi, 2))  # Rounding to 2 decimal places

    return roi_list

# Example usage
initial_prices = [100, 200, 150, 250]  # Example initial stock prices
final_prices = [120, 220, 160, 300]    # 

#Given a list of past monthly sales, calculate the average sales to predict next month’s demand. (Supply Chain)
def predict_next_month_sales(past_sales):
    if not past_sales:
        return "Error: Sales data is empty"
    
    average_sales = sum(past_sales) / len(past_sales)  # Calculate average sales
    return round(average_sales, 2)  # Rounding to 2 decimal places

# Example usage
past_sales = [500, 600, 550, 700, 750, 800, 650]  # Example monthl





#Store stocks and their quantity in a dictionary. Write a function to calculate the total portfolio value using real-time stock prices. (Finance) 
import yfinance as yf

# Function to fetch real-time stock prices and calculate portfolio value
def calculate_portfolio_value(portfolio):
    total_value = 0
    for stock, quantity in portfolio.items():
        try:
            stock_data = yf.Ticker(stock)
            stock_price = stock_data.history(period="1d")["Close"].iloc[-1]  # Get latest closing price
            total_value += stock_price * quantity
            print(f"{stock}: {stock_price} x {quantity} = {stock_price * quantity}")
        except Exception as e:
            print(f"Error fetching data for {stock}: {e}")

    return round(total_value, 2)

# Example Portfolio (Stock Symbol: Quantity)
portfolio = {
    "RELIANCE.NS": 10,
    "TCS.NS": 5,
    "INFY.NS": 8,
    "HDFCBANK.NS": 7
}

# Calculate Portfolio Value
total_portfolio_value = calculate_portfolio_value(portfolio)
print("\nTotal Portfolio Value: ₹", total_portfolio_value)


#Stock Price Analysis: Store daily stock prices in a dictionary and calculate the average, highest, and lowest prices. (Finance) 
# Function to analyze stock prices
def analyze_stock_prices(stock_prices):
    highest = max(stock_prices.values())  # Highest price
    lowest = min(stock_prices.values())   # Lowest price
    average = sum(stock_prices.values()) / len(stock_prices)  # Average price
    
    return {
        "Highest Price": highest,
        "Lowest Price": lowest,
        "Average Price": round(average, 2)
    }

# Example: Storing daily stock prices in a dictionary
stock_prices = {
    "2024-02-01": 2850.50,
    "2024-02-02": 2875.75,
    "2024-02-03": 2900.30,
    "2024-02-04": 2825.40,
    "2024-02-05": 2895.90,
    "2024-02-06": 2930.10
}

# Run analysis
result = analyze_stock_prices(stock_prices)

# Print results
for key, value in result.items():
    print(f"{key}: ₹{value}")




# Find Companies Listed in Either NYSE or NASDAQ but Not Both. (Finance)

# nyse_companies = {"Apple", "Microsoft", "IBM", "Tesla", "Goldman Sachs"} 
# nasdaq_companies = {"Tesla", "Amazon", "Google", "Microsoft", "Meta"}

# Define company sets
nyse_companies = {"Apple", "Microsoft", "IBM", "Tesla", "Goldman Sachs"} 
nasdaq_companies = {"Tesla", "Amazon", "Google", "Microsoft", "Meta"}

# Find companies listed in either NYSE or NASDAQ but not both
unique_companies = nyse_companies ^ nasdaq_companies

# Print the result
print("Companies listed in either NYSE or NASDAQ but not both:", unique_companies)
'''