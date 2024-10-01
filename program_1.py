# Program #1: Kilometer Converter, W5
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.
k1 = float(input('Kilometers: '))

def kilometer_conversion(kilometers):    
    miles = 0.0
    miles = kilometers * 0.6214
    # Return the variable to the calling function
    return miles

kilometers = k1
miles = kilometer_conversion(kilometers)

    # Call kilometer_conversion
kilometer_conversion(k1)
    # Display the miles
print('miles: ', miles,'mi.')
