Python 3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Enter "help" below or click "Help" above for more information.
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()
Welcome to Python 3.13's help utility! If this is your first time using
Python, you should definitely check out the tutorial at
https://docs.python.org/3.13/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To get a list of available
modules, keywords, symbols, or topics, enter "modules", "keywords",
"symbols", or "topics".

Each module also comes with a one-line summary of what it does; to list
the modules whose name or summary contain a given string such as "spam",
enter "modules spam".

To quit this help utility and return to the interpreter,
enter "q", "quit" or "exit".

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> exit()
>>> a = 5
>>> b = 10
>>> print(a + b)
15
>>> 
================== RESTART: /Users/rilanbutts/Documents/first_assignment.py ==================
Traceback (most recent call last):
  File "/Users/rilanbutts/Documents/first_assignment.py", line 1, in <module>
    first_assignment.py
NameError: name 'first_assignment' is not defined
>>> name = "Rilan"
>>> age = 22
>>> height = 5.5
>>> print(f"Howdy! my name is {name}! I am {age} years old and {height} feet tall.")
Howdy! my name is Rilan! I am 22 years old and 5.5 feet tall.
>>> num1 = 10
>>> num2 = 5
>>> print("the sum of num1 and num2 is num1 + num2")
the sum of num1 and num2 is num1 + num2
>>> print(f"the sum of {num1} and {num2} is {num1 + num2}")
the sum of 10 and 5 is 15
>>> print(f"the difference when you subtract {num2} from {num1} is (num1 - num2}")
SyntaxError: f-string: single '}' is not allowed
>>> SyntaxError: f-string: single '}' is not allowed
SyntaxError: invalid syntax
>>> print(f"the difference when you subtract {num2} from {num1) is {num1 - num2}")
SyntaxError: f-string: unmatched ')'
>>> print(f"the difference when you subtract {num2} from {num1} is {num1 - num2}")
the difference when you subtract 5 from 10 is 5
>>> print(f"the product of {num1} and {num2} is {num1 * num2}")
the product of 10 and 5 is 50
>>> print(f"the result of divind {num1} by {num2} is {num1 / num2}")
the result of divind 10 by 5 is 2.0
>>> number = float(input("enter a number, and I'll tell you what kind it is: "))
enter a number, and I'll tell you what kind it is: 5
>>> if number > 0:
...     print("this number is postive. glad to hear is!!")
...     elif number < 0:
        
SyntaxError: invalid syntax
elif number < 0:
    
SyntaxError: invalid syntax
if number > 0:
    print("this number is postive. glad to hear is!!")
elif number < 0:
    print("this number is negative. BOOOOO!!")
else:
    print("Zero it is. A beautiful balance")

    
this number is postive. glad to hear is!!
