# Python - Errors & Exceptions
## Syntax Error

Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python:

       >>> while True print('Hello world')
       File "<stdin>", line 1, in ?
       while True print('Hello world')
                   ^
	SyntaxError: invalid syntax

## Exceptions

Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal: you will soon learn how to handle them in Python programs. Most exceptions are not handled by programs, however, and result in error messages as shown here:

     >>> 10 * (1/0)
     Traceback (most recent call last):
      File "<stdin>", line 1, in ?
     ZeroDivisionError: division by zero

## Author
Andrés Sotelo - Holberton School Colombia
