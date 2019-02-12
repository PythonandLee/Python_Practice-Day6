# Use '%' to get the remainder, 
# so we can use boolean to determine if it is a multiple.
number = input("Please insert a number, I will tell you if it is even or odd. \
Please insert: ")
number = int(number)

if number % 2 == 0:
    print("The number " + str(number) + " is even.")
else:
    print("The number " + str(number) + " is odd.")