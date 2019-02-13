# When define a default to a valuation, make it after non-defined valuations,
# because Python is going to run the program as by order.
# If make mistake to orders, may come out with Error.

def pet(pet_name, animal_type='cat'):
    print("\nShe has a " + animal_type + " as pet.")
    print("Her " + animal_type + "'s name is " + pet_name.title() + ".")
    
pet(pet_name = 'goophy', animal_type = 'snail')
pet(pet_name = 'rocky')