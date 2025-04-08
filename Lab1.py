#Function to calculate the area of a triangle

def triangleArea(base, height):

    area = (1/2) * base * height

    return area

 #Function to calculate perimeter of a triangle

def trianglePerimeter(base, side1, side2):
    

    perimeter = base + side1 + side2

    return perimeter

print("Welcome, user.")

# Ask user for input

userchoice = input("To calculate the area of the triangle, enter 1.\nTo calculate the perimeter of the triangle, enter 2.\n")

# Check userchoice and call appropriate function

if userchoice == "1":

    base = float(input("What is the base of the tiangle?\n"))
    height = float(input("What is the height of the tiangle?\n"))

    area = triangleArea(base, height)
    print("The area of the triangle is", area, "square units.")

elif userchoice == "2":
    
    base = float(input("What is the base?\n"))
    side1 = float(input("What is side1?\n"))
    side2 = float(input("What is side2?\n"))

    perimeter = trianglePerimeter(base, side1, side2)

    print("The perimeter of the triangle is", perimeter, "units")

else:

    print("Invalid Option! Please enter 1 or 2.")
