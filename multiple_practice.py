num = input("Please insert a number, I will tell you if it is 10's multiple. ")
num = int(num)

if num % 10 == 0:
    print("The number: " + str(num) + " is 10's multiple.")
else:
    print("The number: " + str(num) + " is not 10's multiple.")