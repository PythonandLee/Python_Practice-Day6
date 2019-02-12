# Use 'pop()' to remove the last elements, and 'append()' to new list.

sandwich_orders = ['tuna', 'chicken', 'fruit']
finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_order)
    print("I made your " + sandwich_order + " sandwich.")
    
print("\nThese are your orders: ")
for sandwich in finished_sandwiches:
    print(sandwich + " sandwich")