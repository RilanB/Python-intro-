Python 3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Enter "help" below or click "Help" above for more information.
>>> age = int(input("how old are you"))
how old are you 
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    age = int(input("how old are you"))
ValueError: invalid literal for int() with base 10: ' '
>>> age = int(input("how old are you"))
how old are you 18
>>> 
======================== RESTART: /Users/rilanbutts/Documents/voter.py =======================
how old are you 22
CONGRATULATIONS!! you are elibile to vote. go make a difference in the world!
>>> 
======================== RESTART: /Users/rilanbutts/Documents/voter.py =======================
how old are you 17
OOPS! you're not eligible yet. But hey, only 1 more years to go!!
>>> 
======================== RESTART: /Users/rilanbutts/Documents/voter.py =======================
how old are you 35
CONGRATULATIONS!! you are elibile to vote. go make a difference in the world!
>>> 
