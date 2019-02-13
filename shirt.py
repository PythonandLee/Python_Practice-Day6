# Create a 'def' function and give defaults 
# if the values are required frequently.

# When all valuations are given defaults, don't need to consider orders.
def make_shirt(size = 'L', words = 'I love Python'):
    print("\nI want a " + size + " size shirt, and with '" + words + 
        "' printed on it.")

make_shirt()
make_shirt(size = 'XL')    
make_shirt(words= 'work')