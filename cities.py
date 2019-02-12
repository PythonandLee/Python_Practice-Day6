# Strat with 'while' is True to run the program, and stop when meets break.

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you finish.) "

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print("I would like to visit " + city.title() + ", too!")