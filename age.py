# Use 'input()' that users can key in relative information.
# Before use boolean to compare two numbers, remember to change input's type. 
age = input("Hello, how old are you? ")
age = int(age)

if age >= 18:
    print("Age: " + str(age) + ". You are at the legal age to drive.")
else:
    print("Age: " + str(age) + 
        ". You are not at the legal age and not allow to drive.")
