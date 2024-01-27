def homeSize(number):    
    rooms = int(number)    
    def squareFeet():
        x = int(input("What is the length of the room, in feet? "))
        y = int(input("what is the width of the room, in feet? "))
        return x * y    
    dimensions = []    
    for room in range(rooms):
        dimensions.append(squareFeet())        
    size = sum(dimensions)    
    return size


from math import pi
def circleCircumference(radius):
    radius = float(radius)
    circumference = 2.0 * pi * radius
    return circumference