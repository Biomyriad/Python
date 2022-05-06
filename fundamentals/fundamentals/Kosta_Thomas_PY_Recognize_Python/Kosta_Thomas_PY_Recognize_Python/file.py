num1 = 42                       # variable declaration, Primitive, Int
num2 = 2.3                      # variable declaration, Primitive, Float
boolean = True                  # variable declaration, Primitive, Boolean
string = 'Hello World'          # variable declaration, Primitive, String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, List, Initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, Dictionary, Initialize
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, Tuples, Initialize
print(type(fruit))              # log statement, type check, Tuple
print(pizza_toppings[1])        # log statement, List, access value
pizza_toppings.append('Mushrooms') # List, add value, String
print(person['name'])           # log statement, Dictionary, access value
person['name'] = 'George'       # Dictionary, change value, String
person['eye_color'] = 'blue'    # Dictionary, add value, String
print(fruit[2])                 # log statement, Tuples, access value

if num1 > 45:               # conditional, if
    print("It's greater")   # log statement, string
else:                       # else
    print("It's lower")     # log statement, string

if len(string) < 5:             # conditional, if, length check
    print("It's a short word!") # log statement, string
elif len(string) > 15:          # conditional, else if, length check
    print("It's a long word!")  # log statement, string
else:                           # else
    print("Just right!")        # log statement, string

for x in range(5):          # for loop, stop
    print(x)                # log statement, int
for x in range(2,5):        # for loop, start, stop
    print(x)                # log statement, int
for x in range(2,10,3):     # for loop, start, stop, step
    print(x)                # log statement, int
x = 0                       # variable declaration, Primitive, Int
while(x < 5):               # while loop, start, stop
    print(x)                # log statement, int
    x += 1                  # Primitive, Int, increment Value

pizza_toppings.pop()        # List, delete value
pizza_toppings.pop(1)       # List, access value (idx 1), remove value (obj)

print(person)               # log statement, Dictionary, access value(s)
person.pop('eye_color')     # Dictionary, remove value (obj)
print(person)               # log statement, Dictionary, access value(s)

for topping in pizza_toppings:      # for loop, sequence
    if topping == 'Pepperoni':      # conditional, if, access value, String
        continue                    # for loop, continue
    print('After 1st if statement') # log statement, string
    if topping == 'Olives':         # conditional, if, access value, String
        break                       # for loop, break

def print_hello_ten_times():        # function
    for num in range(10):           # for loop, stop
        print('Hello')              # log statement, string

print_hello_ten_times()             # Function call

def print_hello_x_times(x):         # function, parameter
    for num in range(x):            # for loop, stop, access value
        print('Hello')              # log statement, string

print_hello_x_times(4)              # Function call, argument

def print_hello_x_or_ten_times(x = 10): # function, parameter, default parameter value
    for num in range(x):            # for loop, stop, access value
        print('Hello')              # log statement, string

print_hello_x_or_ten_times()        # Function call, with default parameter value
print_hello_x_or_ten_times(4)       # Function call, argument


"""
Bonus section
"""

# print(num3)                   # NameError: name <variable name> is not defined
# num3 = 72                     # variable declaration, Primitive, Int
# fruit[0] = 'cranberry'        # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])# KeyError: 'favorite_team'
# print(pizza_toppings[7])      # IndexError: list index out of range
#   print(boolean)              # IndentationError: unexpected indent
# fruit.append('raspberry')     # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)                  # AttributeError: 'tuple' object has no attribute 'pop'