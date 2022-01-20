# Python second Assignment<br />
<br />
Before starting this project, Make sure you install virtual env in your system using the following steps<br />
<br />
	Install virtualenv by following the steps <br />
	Mac<br />
	python3 -m pip install --user virtualenv<br />
	python3 -m venv env<br />
	source env/bin/activate<br />
	<br />
	Windows<br />
	py -m pip install --user virtualenv<br />
	py -m venv env<br />
	.\env\Scripts\activate<br />
OR follow this link https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/<br />
<br />

## Script 1: Import Statements and Package<br />
<br />

#### What is an import?<br />
When a module is imported, Python runs all of the code in the module file. When a package is imported, Python runs all of the code in the package’s __init__.py file, if such a file exists. All of the objects defined in the module or the package’s __init__.py file are made available to the importer.<br />
Also, Python imports are case-sensitive. import Spam is not the same as import spam.<br />
Basic Definitions<br />
module: any *.py file. Its name is the file name.<br />
built-in module: a “module” (written in C) that is compiled into the Python interpreter, and therefore does not have a *.py file.<br />
package: any folder containing a file named __init__.py in it. Its name is the name of the folder.<br />
in Python 3.3 and above, any folder (even without a __init__.py file) is considered a package<br />
object: in Python, almost everything is an object - functions, classes, variables, etc.<br />
More Details : https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html<br />

#### Script:
Write a script to get circumference of a circle. <br />
Import math module to get value of pi. <br />
Take radius of circle as input from User<br />
<br />

**Write the code in script_1/circumference.py<br />** <br />

<br />

## Script 2: File Operations<br />
<br />
Files are named locations on disk to store related information. They are used to permanently store data in a non-volatile memory (e.g. hard disk).<br />
<br />
When we want to read from or write to a file, we need to open it first. When we are done, it needs to be closed so that the resources that are tied with the file are freed.<br />
<br />
Hence, in Python, a file operation takes place in the following order:<br />
Open a file<br />
Read or write (perform operation)<br />
Close the file<br />
<br /><br />
Python has a built-in open() function to open a file<br />
>>> f = open("test.txt")    # open file in current directory<br />
>>> f = open("C:/Python38/README.txt")  # specifying full path<br />


**Closing Files in Python**<br />
When we are done with performing operations on the file, we need to properly close the file.<br />
Closing a file will free up the resources that were tied with the file. It is done using the close() method available in Python.<br />
Python has a garbage collector to clean up unreferenced objects but we must not rely on it to close the file.<br />
<br />
f = open("test.txt", encoding = 'utf-8')<br />
#perform file operations<br />
f.close()<br />
<br />
**open method**<br />
open method is not entirely safe. If an exception occurs when we are performing some operation with the file, the code exits without closing the file.<br />
A safer way is to use a try...finally block.<br />
try:<br />
   f = open("test.txt", encoding = 'utf-8')<br />
   #perform file operations<br />
finally:<br />
   f.close()<br />
<br />
**Write:**<br />
In order to write into a file in Python, we need to open it in write w, append a or exclusive creation x mode.<br />
with open("test.txt",'w',encoding = 'utf-8') as f:<br />
   f.write("my first file\n")<br />
<br />
<br />
**Read:**<br />
To read a file in Python, we must open the file in reading r mode.<br />
f = open("test.txt",'r',encoding = 'utf-8')<br />
<br />
We can read a file line-by-line using a for loop. This is both efficient and fast.<br />

>>> for line in f:<br />
...     print(line, end = '')<br />
...<br />
This is my first file<br />
This file<br />
contains three lines<br />
<br />
<br />

#### Part 1:<br />
Read file sample.txt present in the repository and print its content.

**Write the code in script_2/file_operation_1.py<br />** <br />

#### Part 2:<br />
There is a directory named “numbers” present in the repository. It contains 10 files named from 1.txt , 2.txt, ….., 10.txt. <br />
Take a input from user from 1 to 10. Open file 1.txt and print its contents if the user selects 1. Similarly print contents of 2.txt if user selects 2 and so on<br />
If user selects any other number. Print “Incorrect Input”<br />
<br />
**Expected Input and Output:** <br />
->	Enter a number between 1 and 10: 3<br />
	Here are contents for 3.txt:<br />
	This is the content of 3rd file printed here<br />
	This is the content of 3rd file printed here<br />
	This is the content of 3rd file printed here<br />
<br />
-> 	Enter a number between 1 and 10: 15<br />
	>> Please select number between 1 and 10<br />

**Write the code in script_2/file_operation_2.py<br />** <br />

#### Part 3:<br />
Write a script to save data to a file.<br />
Take name of file as an Input from User. Once a user gives a file name. Take data to store in the file from that user and write to file<br />
<br />
	**Expected Input and Output:**<br />
	Python random.py<br />
	Enter the name of file: argo.txt<br />
	Enter the contents to be stored in a file: Hello world<br />
	A file named argo.txt is created with “Hello world ” as its contents<br />

**Write the code in script_2/file_operation_3.py<br />** <br />

#### Part 4:<br />
Copy contents of one file to another file. There is a file main.txt stored in the repository. Write a python script which copy contents of main.txt and store it into a new file duplicate.txt. Pass main.txt and duplicate.txt filenames as command line arguments<br />
<br />
**Expected Input and Output:**<br />
> $ cat main.txt<br />
      Hello world<br />
> $ cat duplicate.txt<br />
      Error: No such file exists<br />
>$ python run.py main.txt duplicate.txt<br />
      Copied file contents of main.txt to duplicate.txt<br />
>$ cat duplicate.txt<br />
     Hello world<br />

**Write the code in script_2/file_operation_4.py<br />** <br />

## Script 3: Collections Module<br />
The collection Module in Python provides different types of containers. A Container is an object that is used to store different objects and provide a way to access the contained objects and iterate over them. Some of the built-in containers are Tuple, List, Dictionary, etc. In this article, we will discuss the different containers provided by the collections module.<br />
<br />
<br />

#### 1. Counter<br />
Counter is a subclass of dictionary object. The Counter() function in collections module takes an iterable or a mapping as the argument and returns a Dictionary. In this dictionary, a key is an element in the iterable or the mapping and value is the number of times that element exists in the iterable or the mapping.<br />
<br />

#### 2. Orderdict<br />
The OrderedDict() function is similar to a normal dictionary object in Python. However, it remembers the order of the keys in which they were first inserted.<br />
<br />

##### Part 1:

Create a script that take Input any n numbers and create a dictionary and Orderdict from the input elements as keys and keep their values as 1 if input element is odd number and 0 if input element is even number<br />
Expected Input and output:<br />
<br />
> ->python main.py<br />
	No, of elements: 5<br />
	Input 1 : 2<br />
	Input 2 : 8<br />
	Input 3 : 1<br />
Input 4 : 3<br />
	Input 5 : 9<br />
	Dictionary: { 2: 0,  8: 0,  1: 1,  3: 1,  9: 1  }<br />
OrderedDict([(2, 0), (8, 0), (1, 1), (3, 1), (9, 1)])<br />
 <br />

> ->python main.py<br />
No, of elements: 5<br />
	Input 1 : 2<br />
	Input 2 : 10<br />
	Input 3 : 1<br />
Input 4 : 3<br />
	Input 5 : 2<br />
	Dictionary: { 2: 0,  10: 0,  1: 1,  3: 1  }<br />
OrderedDict([(2, 0), (10, 0), (1, 1), (3, 1)])<br />
<br />
<br />

**Write the code in script_3/ordered_dict.py<br />** <br />

#### DefaultDict:<br />
A DefaultDict is also a sub-class to dictionary. It is used to provide some default values for the key that does not exist and never raises a KeyError.<br />
DefaultDict objects can be initialized using DefaultDict() method by passing the data type as an argument.<br />

##### Part 2:<br />
Create a script to take input of n numbers. Add these element to list and DefaultDict and display them<br />
<br />
**Expected Input and Output:**<br />
> ->python main.py<br />
	No, of elements: 5<br />
	Input 1 : 2<br />
	Input 2 : 8<br />
	Input 3 : 1<br />
	Input 4 : 3<br />
	Input 5 : 9<br />
	List: [2,8,1,3,9]<br />
	OrderedDict: defaultdict(<class 'int'>, {1: 2, 2: 8, 3: 1, 4: 3, 5: 9})<br />

> ->python main.py<br />
	No, of elements: 5<br />
	Input 1 : 2<br />
	Input 2 : 8<br />
	Input 3 : 1<br />
	Input 4 : 1<br />
	Input 5 : 2<br />
	List: [2,8,1,1,2]<br />
	OrderedDict: defaultdict(<class 'int'>, {1: 2, 2: 8, 3: 1, 4: 1, 5: 2})<br />
<br />

**Write the code in script_3/default_dict.py<br />** <br />


#### ChainMap:<br />
A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries.<br />
Example: <br />
<br />
from collections import ChainMap  <br />
d1 = {'a': 1, 'b': 2} <br />
d2 = {'c': 3, 'd': 4} <br />
d3 = {'e': 5, 'f': 6} <br />
#Defining the chainmap  <br />
c = ChainMap(d1, d2, d3)  <br />
print(c)<br />
<br />
Output:<br />
ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})<br />

**No Assignment for ChainMap**<br />
<br />
<br />


#### NamedTuple:<br />
A NamedTuple returns a tuple object with names for each position which the ordinary tuples lack. For example, consider a tuple names student where the first element represents fname, second represents lname and the third element represents the DOB. Suppose for calling fname instead of remembering the index position you can actually call the element by using the fname argument, then it will be really easy for accessing tuples element. This functionality is provided by the NamedTuple.<br />

**No assignment for NamedTuple**<br />
 <br />
 <br />
<br />

## Script 4: Json<br />
Python has a built-in package called json, which can be used to work with JSON data.<br />
Script: A json file subjects.json is stored in repository. It contains data of subjects data<br />
Format: {"English": "92","Maths":"90","History":"90"}<br />
Write a python program to read the json file and add the subjects marks for the student<br />
<br />
Expected Input and output:<br />
> python main.py<br />
	Json : {"English": "92","Maths":"90","History":"90"}<br />
	Total Marks: 272<br />
 <br />
 
 **Write the code in script_4/json_parse.py<br />** <br />

 
## Script 5: String Operations<br />
Python has a set of built-in methods that you can use on strings.<br />

### Part 1:<br />
Write a python script which takes a sentence as Input and performs following actions on them<br />
Capitalize<br />
Lower<br />
Capitalize first letter<br />
Replace all d by h<br />
Replace all o by zm<br />
Find no, of times a occurred<br />
Count no. of letters string has<br />

	**Expected Input and Output:**
	> Enter a sentence: Hello World
	Capitalize : HELLO WORLD
	Lower: hello world
	Capitalize first letter: Hello world
	Replace all d by h: Hello Worlh
	Replace all o by zm: Hellzm Wzmrld 
	Find no, of times a occurred: 0
	Count no. of letters string has: 10
	
	
 **Write the code in script_5/string_1.py<br />** <br />


### Part 2:<br />
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. <br />
<br />

	**Expected Input and Output**:
	Enter string: hello
	Output: helloing
	
	Enter string : willing
	Output: willingly
	

 **Write the code in script_5/string_2.py<br />** <br />

