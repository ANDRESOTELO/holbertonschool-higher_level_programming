# Python - More Data Structures: Set, Dictionary

Dictionaries are sometimes found in other languages as associative memories or associative arrays. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys

## Sets
Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
### Set syntax
Create with curly brackets {} or set() function
Here is a brief demonstration:
>>> x = {"a", "b", "c", "d", "a", "b"}
>>> print(x)
{"a", "b", "c", "d"}
>>> "a" in x
True
>>>"z" in x
False
### Operators
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a (unique letters in a)
{'a', 'r', 'b', 'c', 'd'}
>>> a - b (letters in a but not in b)
{'r', 'd', 'b'}
>>> a | b (letters in either a or b)
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b (letters in both a and b)
{'a', 'c'}
>> a ^ b (letters in a or b but not both)
{'r', 'd', 'b', 'm', 'z', 'l'}

### Set comprehensions supported
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}

 
## Filters

## Lambdas


