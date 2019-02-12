# When 'while' finish(break or False), 
# the rest codes out of while loops star running.

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("What is your favorite food? ")

# When store information in a dictionary, 
# insert as below:
    responses[name] = response

    repeat = input("If there any others would like to respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
        
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + "'s favorite food is " + response + ".")