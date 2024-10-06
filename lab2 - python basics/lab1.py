"""
Basics -> List Practice
"""
import math

# Create a list named a with the elements 2, 4, 6, 8, and 10.
a = [2, 4, 5, 6, 8, 10]
print("List a: ", a)
print()
print("List Length: ", len(a))
print()

# Use a for loop to iterate over list a and print each item.
print("For loop through the list")
for i in a:
    print("Item: ", i)
print()

# Construct a while loop to process elements in list a
# For elements less than 7, directly print the value.
# For elements greater than 7, print their square.
x = 0
print()
print("While loop through the list")
while x < len(a):
    if a[x] < 7:
        print(a[x], ":", a[x])
        x += 1
        continue
    print(a[x], "^2:", a[x] ** 2)
    x += 1
print()

# Utilize the continue statement to skip the element 6.
print("Skip element 6")
y = 0
while y < len(a):
    if a[y] == 6:
        y += 1
        continue
    else:
        print("a: ", a[y])
        y += 1
print()

# For elements less than 7, directly print the value.
print("Values less than 7")
for i in a:
    if i < 7:
        print("i: ", i)
print()

# For elements greater than 7, print their square.
print("Values more than 7, print their square")
for i in a:
    if i > 7:
        print("i: ", round(math.sqrt(i), 2))
print()

"""
Ternary Operator
Implement the following logic using a single line of code: 
For an integer variable v, assign x a value of 10 if v < 3 , 20 if 3 ≤ v < 10 , and 40 if v ≥ 10.
"""
print("Ternary Operator")
v = 14
x = 10 if v < 3 else 20 if 3 <= v < 10 else 40
print(x)
print()

"""
Function Practice
Write a function that accepts two parameters. The function should:
Concatenate the parameters if both are strings.
Concatenate the parameters if both are lists.
Add the parameters together if both are numbers.
Test your code.
"""
print("Function Practice")


def function(a, b):
    return a + b


res = function("Hello ", "world")
print("Concentrate String: ", res)

res1 = function([1, 2, 3], [4, 5, 6])
print("Concentrate Lists: ", res1)

res2 = function(1, 2)
print("Numbers Addition: ", res2)
print()

'''
OOP Practice
Define a class Animal with an attribute name and a method make_sound() .
Create a subclass Dog derived from Animal with a modified attribute name
and a unique method bark().
'''
print("OOP Practice")


class Animal:
    # class attribute
    name = ""

    # class method
    def make_sound(self):
        print("Animal sound")


class Dog(Animal):
    # Overriding the constructor to set a default name for Dog
    def __init__(self, name):
        self.name = name

    # Overriding make_sound method
    def make_sound(self):
        print(f"{self.name}: Woof Woof")

    def getName(self):
        return self.name


dog = Dog("Lilly")
print("Dog Name:", dog.getName())
dog.make_sound()
print()

''' Dictionary Practice '''
# Construct a dictionary kvtable with the key-value pairs: {'a': 'x', 'b': 'y', 'c': 'z', 'd': 'w'}
kvtable = {'a': 'x', 'b': 'y', 'c': 'z', 'd': 'w'}
print("kvtable: ", kvtable)

# Create another dictionary kvtable2 with the key-value pairs: {'a': 'y', 'b': 'y', 'e': 'u', 'f': 'w'}
kvtable2 = {'a': 'y', 'b': 'y', 'e': 'u', 'f': 'w'}
print("kvtable2: ", kvtable2)

# Merge kvtable2 into kvtable using the method dict.update() and analyze the resulting dictionary.
kvtable.update(kvtable2)
print("After Merge: ", kvtable)
print()
# after merging table2 to table1, a:x pair got replaced with a:y


'''Tuple Practice'''
# Develop a function foo() designed to compute the product of an indefinite number of inputs.
print("Tuple Practice")
def foo(*args):
    product = 1
    for i in args:
        product *= i
    return product

# Create a tuple (5, 6, 7) , and use the function foo() to compute the product of the unpacked tuple values.
tuple=(5, 6, 7)
tuple2=(5, 10, 15, 20, 25, 30)
print(foo(tuple))
print(foo(tuple2))
print()


""" Magics """
'''List Comprehension'''
# Use list comprehension to construct a dictionary with the structure {1:2,2:3,3:4}
print("List Comprehension")
dic = {x: x + 1 for x in range(1, 4)}
print(dic)
print()

'''Tuple Unpacking'''
# Initialize a = 1 and b = (2, 3). Swap values to achieve a = (1, 2) and b = 3
a = 1
b = (2, 3)

a, b = (a, b[0]), b[1]

print("a: ", a, "\tb: ", b)
print()

'''Using Lambda Expression'''
# Create a lambda function designed to invert the key-value pairing of a dictionary. Assume there are no duplicate values in the dictionary {1:2, 2:3,3:4} .

'''Using F-strings'''
# Create a range iterator range(4, 100, 2.2) , iterate through it using a for loop, and utilize an F-string to output formatted strings like "loop_{index}, value_{value from the iterator}".

'''Combine Iterables'''
# Write a function to check if two lists [1, 2, 3, 4] and [1, 2, 4, 4] are identical using the zip function.
# Advanced: Use .any() and list comprehension to check list equality in a single line of code.

'''Context Manager'''
# Open and print the contents of a text file using a context manager to ensure proper handling of file operations.


"""Functional Programming"""
print("Functional Programming")

'''Map Practice'''
# Prepare a lambda function lambda x: x**2 and apply it to the list [1, 2, 3, 4, 5] using the map function.

'''Reduce Practice'''
# Develop a lambda function, then use it with list reduce to concat all  strings in a
# ['abc', 'bdf', '123'], the result should be "abc bdf 123", be aware of the space

# Develop a lambda function that inverts the key-value relationship in a dictionary, suitable even for dictionaries with duplicate values
# in the dictionary {1:2, 2:4, 3:4, 5:5} .