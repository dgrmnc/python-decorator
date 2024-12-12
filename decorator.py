def add_topping(topping_name):
    def decorator(func):
        def wrapped(*args, **kwargs):
            # get input from user:
            user_input = input(f"Would you like to add {topping_name} on your ice cream?(y/n): ").strip().lower()
            kwargs[topping_name] = user_input == 'y'
            return func(*args, **kwargs)
        return wrapped
    return decorator

# adding our decorators here
@add_topping('fudge')
@add_topping('sprinkles')
def get_ice_cream(flavor, sprinkles=False, fudge=False):
    if sprinkles and fudge:
        print(f"Here is your {flavor} flavor ice cream with fudge and sprinkles.")
    elif sprinkles:
        print(f"Here is your {flavor} flavor ice cream with sprinkles.")
    elif fudge:
        print(f"Here is your {flavor} flavor ice cream with fudge.")
    else:
        print(f"Here is your {flavor} flavor ice cream with no fudge and sprinkles.")
    

get_ice_cream("Vanilla")

