# Create a empty dictionary, and 'append' later in while loops.
# Use 'A[b]=c' to sotre information in dictionary. ->> A = { 'b':'c'}

# Dedine a boolean with 'True' to run while loops, 
# and change to 'False' in 'if-else' when want to stop.
survey = {}
prompt = "If you could visit one place in the world, where would you go?"

active = True

while active:
    name = input("\nWhat is your name? ")
    respond = input(prompt)
    
    survey[name] = respond
    
    repeat = input("\nIf any one want to answer this, too? (yes/no) ")
    if repeat == 'no':
        active = False 

print("\n --- Survey Results --- ")
for name, respond in survey.items():
    print(name.title() + " wants to go to " + respond.title() + ".")