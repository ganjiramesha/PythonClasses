
#A simple program to check if a number is even or odd
'''
number = int(input("enter the number : "))
if number//2==0:
    print("The given number is even")
else:
    print("The given number is odd")


#2. Write a program to check if a year is a leap year or not

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(year," is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a leap year")
elif year % 4 == 0:
    print(year," is a Leap Year")
else:
    print(year," is NOT a Leap Year")


#3. Write a program to assign students A,B,C,D, and Fail grades basis their scores 

grade = int(input("Enter the obtained marcks: "))
if grade >=80:
    print(grade, "marcks comes under the grade A")
elif grade >=60 and grade<=80:
    print(grade, "marcks comes under the grade B")
elif grade>=40 and grade<=60:
    print(grade, "marcks are comes under the grade C")
else:
    print(grade,"marcks comes under the grade D")
 
#4. Write a Python program that takes the total purchase amount as input and applies a discount based on the following conditions
        # If the amount is ₹5000 or more, apply a 20% discount.
        # If the amount is between ₹3000 and ₹4999, apply a 15% discount.
        # If the amount is between ₹1000 and ₹2999, apply a 10% discount.
        # If the amount is less than ₹1000, no discount is applied.

volume = int(input("Enter the purchase value: "))
if volume >=5000:
    print(volume, "amount eligible for 20 percentage discount")
elif volume >=3000 and volume<=4999:
    print(volume, "amount eligible for 15 percentage discount")
elif volume >=1000 and volume<=2999:
    print(volume, "amount eligible for 10 percentage discount")
else:
    print(volume, "amount does not eligibel for any percentage of discount")


#5. Write a program to check if a number is a perfect square

number = int(input("Enter a number: "))
if int(number ** 0.5) * int(number ** 0.5) == number:
    print(number," is a perfect square.")
else:
    print(number, "is not a perfect square.")


#6. Write a program to check if a triangle is valid based on all the three angles
angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))
if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3) == 180:
    print("The given angles form a valid triangle.")
else:
    print("The given angles do not form a valid triangle.")



#7. Write a program which takes the height and weight of the user, calculates the BMI and gives the category.
        # 18.5 or less : under weight
        # 18.5-24.9    : Normal
        # 25-29.9       :over weight
        # 30-34.9       :obese
        # 35-39.9       :over obese
        # 40 or greater :Extremly obese

weight =  (float(input("Enter the weight: ")))
if weight >=40:
    print(weight, "is Extremly obese")
elif weight <=39.9 and weight>=35:
    print(weight, "over obese")
elif weight <=34.9 and weight>=30:
    print(weight, "obese")
elif weight <=29.9 and weight>=25:
    print(weight, "over weight")
elif weight <=24.9 and weight>=18.5:
    print(weight, "Normal")
else:
    print(weight, "under weight")

'''


height =  (float(input("Enter the height: ")))
weight = (float(input("enter the weight: ")))
Name = str(input("Enter your name: "))
BMI = (weight/height**2)

if BMI >=40:
    print( "Extremly obese")
elif BMI <=39.9 and BMI>=35:
    print( "over obese")
elif BMI <=34.9 and BMI>=30:
    print("obese")
elif BMI <=29.9 and BMI>=25:
    print("over weight")
elif BMI <=24.9 and BMI>=18.5:
    print("Normal")
else:
    print("Hi {} your height is {}, weight is {} and your BMI {} hence you are under weight".format(Name, height, weight, BMI))
 

