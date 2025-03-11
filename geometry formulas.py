# different mathematical functions: -
'''
def area_of_circle(radius):
    return 3.14159 * radius * radius

def circumference_of_circle(radius):
    return 2 * 3.14159 * radius

def volume_of_cylinder(radius, height):
    return 3.14159 * radius * radius * height

def surface_area_of_cylinder(radius, height):
    return 2 * 3.14159 * radius * (radius + height)

def area_of_rectangle(length, width):
    return length * width

def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def area_of_square(side):
    return side * side

# Example function calls
radius = 5
height = 10
length = 8
width = 6
side = 4

print("Area of Circle:", area_of_circle(radius))
print("Circumference of Circle:", circumference_of_circle(radius))
print("Volume of Cylinder:", volume_of_cylinder(radius, height))
print("Surface Area of Cylinder:", surface_area_of_cylinder(radius, height))
print("Area of Rectangle:", area_of_rectangle(length, width))
print("Perimeter of Rectangle:", perimeter_of_rectangle(length, width))
print("Area of Square:", area_of_square(side))


'''

def calculate_speed_distance_time(speed=None, distance=None, time=None):
    """
    Calculates the missing variable based on Speed = Distance / Time.
    Provide any two values, and the function will return the third.
    """
    if speed is None and distance is not None and time is not None:
        return f"Speed = {distance / time} units/time"
    elif distance is None and speed is not None and time is not None:
        return f"Distance = {speed * time} units"
    elif time is None and speed is not None and distance is not None:
        return f"Time = {distance / speed} time units"
    else:
        return "Please provide exactly two values to calculate the third."

# Example function calls
print(calculate_speed_distance_time(speed=50, time=2))      # Distance = 100 units
print(calculate_speed_distance_time(distance=100, time=2))  # Speed = 50 units/time
print(calculate_speed_distance_time(speed=50, distance=100)) # Time = 2 time units
