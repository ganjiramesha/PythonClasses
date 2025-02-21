# User-Defined While Loop 
a = int(input("Enter the a: ")) 
s = 1
b = int(input("Enter the range b: ")) 

while s <= b: 
	result = s * a 
	print(f"{s} x {a} = {result}") 
	s += 1
