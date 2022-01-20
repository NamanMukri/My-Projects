sIn programming, a variable is nothing more than a name for something so you
can use the name rather than the something as you code. Programmers use these variable
names to make their code read more like English and because they have lousy memories. If
they didn’t use good names for things in their software, they’d get lost when they tried to
read their code again.

underscore in the variable name: We use this character a lot to put an imaginary
space between words in variable names.

### **Script 1**: variables

Refer script_1/script_1_sample.py and write a script to list count of each animal in the Forest and also categorize them in Herbivorous and carnivorous and print their count. List of animals shown below
 <br />
Lion =2<br />
White Tiger=2<br />
red deer=50<br />
elephant=10<br />
spider monkey=100<br />
zebra=17<br />
rhinoceroses=10<br />
Black Panther=10<br />
Harpy Eagles=12<br />
White backed vulture=5<br />
Herbivorous are 3,4,5,6,7<br />
Carnivorous are 1,2,8,9,20<br />

 <br />

**Expected Output:**

There are 2 Lions <br />
There are 2 White Tigers<br />
There are 50 Red deers<br />
There are 10 Elephants<br />
There are 100 spider monkeys<br />
There are 17 zebras<br />
There are  10 rhinoceroses<br />
There are 10 Black Panthers<br />
There are 12 Harpy Eagles<br />
There are  5 White-backed vultures<br />
There are total <> Herbivorous animals<br />
There are total <> Herbivorous animals<br />
<br />



Note: <> is to be replaced with the addition of animal counts
 <br />**Write the code in script_1/script_1.py**


###  Script 2. Strings

A string is usually a bit of text you want to display to someone or “export” out of the program you are writing. Python knows you want something to be a string when you put either " (doublequotes) or ' (single- quotes) around the text. You saw this many times with your use of print when you put the text you want to go to the string inside " or ' after the print.  <br />Then Python prints it. Strings may contain the format characters you have discovered so far. You simply put the formatted variables in the string, and then a % (percent) character, followed by the variable. The only catch is that if you want multiple formats in your string to print multiple variables, you need to put them inside ( ) (parentheses) separated by , (commas). It’s as if you were telling me to buy you a list of items from the store and you said, “I want milk, eggs, bread, and soup.” Only as a programmer we say, “(milk, eggs, bread, soup).”

Write a script to do the following:
 <br />With one print statement to print all months in a year name each in one line. Hint: use \n escape sequence
 <br />Wiy one Print statement all days in a Week in one single line separated by Comma. Hint use formatter to print
 <br />With one print statement and not using any escape sequence print  number 1 to 10 one below each other. Hint: Use """ to print


Note: You can only use 3 print statements in this assignment


**Expected output**: <br />
January <br />
February <br />
March <br />
April <br />
May <br />
June <br />
July <br />
August <br />
September <br />
October <br />
November <br />
December <br />
Monday, Tuesday, Wednesday, Thursday, Friday, Saturday <br />
1 <br />
2 <br />
3 <br />
4 <br />
5 <br />
6 <br />
7 <br />
8 <br />
9 <br />
10 <br />
 <br />


**Write code in file script_2/script_2.py**


### **Script 3**: List, tuple, Boolean; <br />
 A list is exactly what its name says—a container of things that are organized in order. It’s not complicated; you just have to learn a new syntax. First, there’s how you make a list:  <br />
hairs = ['brown', 'blond', 'red']  <br />
eyes = ['brown', 'blue', 'green']  <br />
weights = [1, 2, 3, 4] <br />

A tuple is created by placing all the items (elements) inside parentheses (), separated by commas. The parentheses are optional, however, it is a good practice to use them. <br />
A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.). <br />

The Python Boolean type is one of Python’s built-in data types. It’s used to represent the truth value of an expression. For example, the expression 1 <= 2 is True, while the expression 0 == 1 is False.
 <br /><br /><br />
**Script**<br />
In a list, Add all days in a week into a list and print them <br />
Similarly add all the days in a week in a tuple and print them <br />
Print True or false for following mathematical expressions: <br />
1<2 <br />
99>=8 <br />
345678+77777<66666-90 <br />
7896*5555 == 8989898 <br />

**Expected Output**: <br />
[‘Monday’, ‘Tuesday’,’Wednesday’,’Thursday’,’Friday’,’Saturday’,’Sunday’] <br />
("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday") <br />
True <br />
True <br />
False <br />
False <br />

**Write code in file script_3/script_3.py**  <br />

### **Script 4**: Input <br />

Up until now, our programs were static. The value of variables was defined or hardcoded into the source code. <br />

To allow flexibility, we might want to take the input from the user. In Python, we have the input() function to allow this. The syntax for input() is: <br />

input([prompt]) <br />

where prompt is the string we wish to display on the screen. It is optional. <br />

>>> num = input('Enter a number: ') <br />
Enter a number: 10 <br />
>>> num <br />
'10' <br />

This prompts the user with “Enter a number:?” and puts the result into the variable num. This is how you ask someone a question and get the answer. <br />



**Script**: Write a python script to ask Argo his age, height, weight and calculate his BMI <br />

The Body Mass Index (BMI) or Quetelet index is a value derived from the mass (weight) and height of an individual, male or female. The BMI is defined as the body mass divided by the square of the body height and is universally expressed in units of kg/m2, resulting from the mass in kilograms and height in meters. The formula is: <br />

BMI = round(weight/ (height * height), 1) <br />
where, <br />
mass or weight is in Kg, <br />
height is in meters <br /> <br />
**Expected Output:** <br />
> Hi Argo, What is your Age? <br />
27 <br />
> What is your Weight in Kg? <br />
65 <br />
> What is your Height in metres? <br />
1.79 <br />
The BMI is 20.2             -> #Return statement<br />

**Write code in file script_4/script_4.py**
**Add Logic in bmi_script_4 function and return the output**<br />

### **Script 5**: If else Ternary <br />

Decision-making is required when we want to execute a code only if a certain condition is satisfied. <br />
if test expression: <br />
    Body of if <br />
else: <br />
    Body of else <br />

The if…elif…else statement is used in Python for decision making. <br />

if test expression: <br />
    Body of if <br />
elif test expression: <br />
    Body of elif <br />
else:  <br />
    Body of else <br />
Refer: https://www.programiz.com/python-programming/if-elif-else <br />

**Script:** <br />
Using the above BMI Script. Ask the User his name and then use of their name to ask their weight and height.  <br />
Based on Output of BMI Index, tell the user if they are underweight, healthy, overweight, or Obese <br />


BMI	             Weight status <br />
Below 18.5	underweight <br />
18.5-24.9	normal <br />
25.0-29.9	overweight <br />
30.0 +           obese  <br />

**Expected Output 1**: <br />
> What is your Name: <br />
Argo <br />
> Hi Argo, What is your Height in metres? <br />
1.79 <br />
> What is your weight: <br />
65 <br />
Your BMI is 20.2 which means you are healthy.                 -> #Return statement<br /> <br /> <br />

**Expected Output 2**: <br />
> What is your Name: <br />
Rahul <br />
> Hi Rahul, What is your height: <br />
1.70 <br />
> What is your weight: <br />
88 <br />
Your BMI is 30.5 which means you are obese.                    -> #Return statement<br /><br />

**Write code in script_5/script_5.py**<br />
**Add Logic in bmi_script_5 function and return the output**<br />

### **Script 6: Loops**  <br />

Relation of loops with lists:  <br />
You should now be able to do some programs that are much more interesting. If you have been keeping up, you should realize that now you can combine all the other things you have learned with if- statements and boolean expressions to make your programs do smart things. <br />
However, programs also need to do repetitive things very quickly. We are going to learn for loops in this exercise to build and print lists. <br />
The best way to do this is with a list. A list is exactly what its name says—a container of things that are organized in order.  <br />

What you do is start the list with the [ (left bracket), which “opens” the list. Then you put each item you want in the list separated by commas, just like when you did function arguments.  <br />
Lastly, you end the list with a ] (right bracket) to indicate that it’s over. Python then takes this list and all its contents and assigns them to the variable.  <br />

**Script:** <br />
Create these 3 lists: <br />
numbers = [1,2,3,4,5] <br />
Weekdays = [‘Monday’, ‘Tuesday’,’ Wednesday’,’ Thursday’,’ Friday’,’ Saturday’,’ Sunday’] <br />
Num = [‘222’,’100’,’85,’500’,’300’’] <br />

Print numbers in list ‘numbers’ one below the others using a for loop <br />
Print numbers in list ‘numbers’ one below the others using a while loop <br />
Print the days of the week from list ‘Weekdays’ using For loop <br />
Print the days of the week  from list ‘Weekdays’ using the While loop <br />
Calculate the sum of all numbers in the array Num using for loop <br />
Calculate the sum of all numbers in the array Num using while loop <br />


Expected Output: <br />
1 <br />
2 <br />
3 <br />
4 <br />
5 <br />
 <br />
1 <br />
2 <br />
3 <br />
4 <br />
5 <br />
 <br />
Monday <br />
Tuesday <br />
Wednesday <br />
Thursday <br />
Friday <br />
Saturday <br />
Sunday <br />
 <br />
Monday <br />
Tuesday <br />
Wednesday <br />
Thursday <br />
Friday <br />
Saturday <br />
Sunday <br />
 <br />
The sum from for loop:1207 <br />
The sum from while loop:1207 <br />
 <br />
 
 Write code in script_6/script_6.py

### **Script 7**: Command Line <br />


Command line arguments are simply arguments that are specified after the name of the program in the system's command line, and these argument values are passed on to your program during program execution. <br />
Python sys module stores the command line arguments into a list, we can access it using sys.argv. This is very useful and simple way to read command line arguments as String. Let’s look at a simple example to read and print command-line arguments using python sys module. <br />

Example: test.py <br />
import sys <br />
 <br />
print(type(sys.argv)) <br />
print('The command line arguments are:') <br />
for i in sys.argv: <br />
    print(i) <br />
Output: <br />
> Python test.py 1 2 3 4 5 <br />
The command line arguments are: <br />
1 <br />
2 <br />
3 <br />
4 <br />
5 <br />
 <br /> 
**Script**: Modify the same BMI script which you wrote in “Script 5” <br />
Replace Input type of name, weight and Height from user input to command Input <br />
 <br /> 

**Expected Output 1**:
> python bmi.py Argo 1.79 65 <br />
Name: Argo <br />
Height: 1.79 <br />
Weight 65 <br />
Your BMI is 20.2 which means you are healthy.<br />
 <br />

**Expected Output 2**: <br />
> python bmi.py Rahul 1.7 88 <br />
Name: Rahul  <br />
Height: 1.7 <br /> 
Weight 88 <br />
Your BMI is 30.5 which means you are obese. <br />

Write code in script_7/script_7.py

