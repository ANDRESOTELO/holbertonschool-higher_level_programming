# Python - Classes and Objects
Classes and objects are the two main aspects of object oriented programming. A class creates a new type where objects are instances of the class.

Objects can store data using ordinary variables that belong to the object. Variables that belong to an object or class are referred to as fields. Objects can also have functionality by using functions that belong to a class. Such functions are called methods of the class. This terminology is important because it helps us to differentiate between functions and variables which are independent and those which belong to a class or object. Collectively, the fields and methods can be referred to as the attributes of that class.

The simplest class possible is shown in the following example:

    class Person:
    	  pass  # An empty block

    p = Person()

## Methods
We have already discussed that classes/objects can have methods just like functions except that we have an extra self variable.

   class Person:
   	 def say_hi(self):
	      print('Hello, how are you?')

   p = Person()
   p.say_hi()

Output:
	Hello, how are you?