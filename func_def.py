
#Function Definition

#SmallCase
#Capitalized Case - firstName
#No Spaces



# def greeting():

#     print("Good Evening, How was your day!")
#     print("This is inside the function")


# #Calling

# greeting()



# name = "Raghav"
# print("Good Evening", name)

#functions that take input 



def greeting(name):

    print("Good Evening!", name)


def addNum(first_number, second_number):

    print(first_number + second_number)


# Write a function which calculates discounts and gives the final price, Input should be price, quantity and discount

# def finalPrice("price, quantity, discount"):

# print(price × quantity - discount)

# discount = 0.1
# sub_total = price * quantity 
# final_price = sub_total - (sub_total * discount)


def finalPrice(price, qty, discount):
    sub_total = price * qty
    final_price = sub_total - (sub_total * discount)
    print(final_price)


#By default we offer 5% discount, however we can change the discount basis a transaction

#function with default parameters - the default parameter can be overriden during the function calling

def finalPrice(price, qty, discount=0.05):

    return (price * qty) - ((price * qty) * discount)