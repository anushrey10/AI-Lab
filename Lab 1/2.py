"""Write a program that calculates the area of a rectangle using user-input length and width, and then compare it with the area of a square with side length half of the rectangle's width."""

def area():
        length = input("Enter length of rectangle : ")
        width = input("Enter width of rectangle : ") 

        length = int(length)
        width = int(width)
        
        side = width/2
        
        arec = length*width
        asqr = side*side
        
        print(f"Area of rectangle = {arec}")
        print(f"Area of square = {asqr}")
        
        if arec == asqr:
            print("Area of rectangle is same as Area of square")
            
        elif arec > asqr:
            print("Area of rectangle is greater than Area of square")
            
        else:
            print("Area of rectangle is less than Area of square")
        
    
area()