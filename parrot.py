# Define valuations to store messages, and redefine them by using '+=' to store 
# more than one messages in the same valustion.
# Use 'x = True/False' to be a sign. When active is True, the programe keeps working.
# When active is False, it breaks.
prompt = "\nTell me something, and I will repeat it back: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)