# Use boolean and input function can apply to restaurant to ask reservation information.
people = input("Please insert the number of people. Please insert: ")
people = int(people)

if people > 7:
    print("Sorry, we don't have a table for " + str(people) + " people now.")
else:
    print("Now we have a table for " + str(people) +
         " people. Let me lead you to the table.")
