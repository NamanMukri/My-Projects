# Python Sixth Assignment

## Script 1: Comprehension

Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.) using sequences which have been already defined. Python supports the following 4 types of comprehensions:<br />
List Comprehensions<br />
Dictionary Comprehensions<br />
Set Comprehensions<br />
Generator Comprehensions<br />

#### Part 1: Write a python script to multiply the element with 2 in the array using List Comprehensions

Write the same script using Set and Generator Comprehensions<br />

**Update code in Files script_1/list_comprehension.py, script_1/set_comprehension.py, script_1/generic_comprehension.py**

List Expected Input/Output: <br />

	Add list elements seperated by space: 1 2 3 4
	Output list using list comprehensions: [2, 4, 6, 8]

Set Expected Input/Output: <br />

	Add set elements seperated by space: 1 2 3 4
	Output Set using set comprehensions: {8, 2, 4, 6}

Generic Expected Input/Output: <br />

	Add generic elements seperated by space 1 2 3 4
	Output generic list using generic comprehensions: [2, 4, 6, 8]

#### Part 2: Write the following dictionary<br />
{“a”: 25, “b”:4,”c”:1,”d”:100}<br />
Using Dict Comprehension calculate the square root of the numbers and store it back to the same key<br />

Expected Input/Output:

	{'a': 5.0, 'b': 2.0, 'c': 1.0, 'd': 10.0}

## Script 2: Lambda

In Python, an anonymous function is a function that is defined without a name.<br />
While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.<br />
Hence, anonymous functions are also called lambda functions.<br />

Example of Lambda Function in python<br />
Here is an example of a lambda function that doubles the input value.<br />

##### Program to show the use of lambda functions<br />

	double = lambda x: x * 2

	print(double(5))
	Output

	10

#### Part 1: <br />
Write a Python program to count the even, odd numbers in a given array of integers using Lambda. Take list as user Input. Hint : filter<br />

**Expected Input Output**

	Add list elements seperated by space 2 3 4 5 6

	Number of even numbers in the above array:  3

	Number of odd numbers in the above array:  2

Update code in script_2/lambda_1.py<br />


#### Part 2: Write a Python program to add two given lists using lambda. Hint : Map<br />
nums1 = [1, 4, 5, 6, 5] <br />
nums2 = [3, 5, 7, 2, 5] <br />

**Expected Input Output**

	Result: after adding two list
	[4, 9, 12, 8, 10]

Update code in script_2/lambda_2.py<br />


## Script 3: Functools<br />

Python functools module provides us various tools which allows and encourages us to write reusable code. Some of them are:<br />


You can create partial functions in python by using the partial function from the functools library.<br />
Partial functions allow one to derive a function with x parameters to a function with fewer parameters and fixed values set for the more limited function.<br />
**Example:<br />**

	from functools import partial

	def multiply(x,y):
		return x * y

	#create a new function that multiplies by 2
	dbl = partial(multiply,2)
	print(dbl(4))

	#Output
	8

**An important note: the default values will start replacing variables from the left. The 2 will replace x. y will equal 4 when dbl(4) is called
**<br />

##### Part 1: In file script_3/partial.py, Edit the function provided by calling partial() and replacing the first three variables in func(). Then print with the new partial function using only one input variable so that the output equals 3150.<br />



## Script 4: Recursion<br />

In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of the construct are termed recursive functions.<br />

Example:<br />
Factorial of a number is the product of all the integers from 1 to that number. For example, the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720. <br />

	def factorial(x):
	    """This is a recursive function
	    to find the factorial of an integer"""

	    if x == 1:
		return 1
	    else:
		return (x * factorial(x-1))


	num = 3
	print("The factorial of", num, "is", factorial(num))
	#Output
	The factorial of 3 is 6



#### Part 1: Write a Python program to calculate the value of 'a' to the power 'b' using recursion<br />

**Expected Input/Output:<br />**

	Enter the number 6
	Enter Power 2
	#Output
	36

Update code in script_4/power_recursion.py<br />

#### Part 2: Write a Python program to add all the elements in a list using recursion <br />

**Expected Input/Output:<br />**

	Add list elements seperated by space 2 3 4 5
	14
	
Update code in script_4/sum_recursion.py<br />
