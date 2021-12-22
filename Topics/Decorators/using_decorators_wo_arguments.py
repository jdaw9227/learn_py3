def decorator(decorating_function):
    print('decorator func ran first')
    return decorating_function


@decorator  # It means the decorator function is adding more function to the function below
def decorating_function():
    print('decorating function ran')


# my_func = decorator(decorating_function)
# my_func()
# instead of line 10 and 11 I can use @decorator and directly call the funciton being decorated


decorating_function()
