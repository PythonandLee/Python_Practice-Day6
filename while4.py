# Use 'remove.()' to with 'while' loops to delet all specific elements in the list.
# Use 'pop()' to automatically remove the last elements in the list.
# Make correct command with 'while' loops for the elements you want to determine.

sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'chicken', 'pastrami', 'fruit']
finished_sandwiches = []

print("Sorry, pastrami sandwiches are sold out.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_order)
    print("I made your " + sandwich_order + " sandwich.")
    
print("\nThese are your orders: ")
for sandwich in finished_sandwiches:
    print(sandwich + " sandwich")