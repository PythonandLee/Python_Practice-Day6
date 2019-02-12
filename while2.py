# Use 'continue' to go back to the beginning, and run the program over again.
prompt = "\nPlease insert your age, I will let you know the price of a ticket."
prompt += "\nEnter 'quit' when you finish."
prompt += "\nPlease insert your age here: "
active = True

while active:
    age = input(prompt)
    
    if age == 'quit':
        active = False 

    else:
        age = int(age)
        if age < 3:
            print("For " + str(age) + ", it is free entry.")
            continue
        elif age < 13:
            print("For " + str(age) + ", the ticket price is $10")
            continue
        else:
            print("For " + str(age) + ", the ticket price is $15")
            continue 