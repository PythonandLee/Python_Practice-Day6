# Define 'topping = input()' in 'while' loops to 
# determine the input values over and over again when 'while' is True.
prompt = "\nPlease insert a pizza topping you want to add: "

while True:
     topping = input(prompt)
     
     if topping == 'quit':
         break
     else:    
         print("We will add '" + topping + "' for your pizza.")
     