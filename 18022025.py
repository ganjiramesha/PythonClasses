"""
print("A"+9)
print(1+2)

# Data Types casting: -
 

city = "hyderabad"
age = 34
temparature = 28.3 
check = True
C = 4+3j

print(type(city))
print(type(age))
print(type(temparature))
print(type(check))
print(type(C))

P = int("b")
print(P)

R = int("4")
print(type(R))
print(R)

Q = str(250)
print(type(Q))

A = int(25.3)
print(A)
print(type(A))

"""
# if condition implementation in python

age = int(input("enter your age: "))
if age > 18:
    print("Allow him to the chamber")
elif age>=16 and age < 18:
    print("additional info required")
else:
    print("you are not allowed as your age is below 16")


# 

price = int(input("enter the product price: "))
if price >=1000:
    print("expensive")
elif price <=1000 and price >=800:
    print("medium")
elif price<=8000 and price >=500:
    print("low")
else:
    print("cheap")



