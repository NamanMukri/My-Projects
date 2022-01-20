# Django Rest Framework

#### Django Rest Framework First Assignment<br />

#### CRUD functionality with Django REST Framework

Four main API requests are GET, POST, PUT, DELETE.<br />
1. GET —This request is made when we wanna request some data from the server. Eg: Fetching weather forecast from the weather API.<br />
2. POST — This request is made when we wanna add data to the server. Eg: User Registration and Login.<br />
3. PUT — This request is for changing any Existing information in the server. Eg: Updating User Profile.<br />
4. DELETE — As the name indicates, this request is made where we wanna delete any existing information.<br />
Note: __str__() ->in every model you should define the standard Python class method __str__() to return a human-readable string for each object.<br />
<br />

**Steps for creating a DRF Project**<br />

1. Create a Django Project<br />
2. Install Django Rest Framework<br />
3. Create a model and add __str__ as a good practice to return human-readable string<br />
4. Create API Class<br />
5. Create API View<br />
6. List API view<br />
7. Update API View<br />
8. Delete API view:<br />
9. Create Serializer class<br />
10. Map your APi class with Url in urls.py<br />
11. Code is ready. Just run your server<br />

### Assignment:

Create a Backend of Student Management system using DRF. App name should be student<br />
1. Student Data(Models) which needs to be stored
2. Student registration number -> student_reg_no (Text field) -> This should be Unique but should not be a primary key
3. Student name -> student_name (Text field) -> 
4. Student Email -> student_email (Text field)
5. Student Mobile Number -> student_mobile (Text field)
6. reated at -> created_at (Text field)(default : current time)

#### Urls.py

1. Name in Django URL -> name is used for accessing that URL from your Django / Python code.
2. For example you have this in 'student/urls.py
3. url(r'^main/', views.main, name='main')
4. In point 2, "main" is the name of this URL
5. URL namespaces -> URL namespaces allow you to uniquely reverse named URL patterns even if different applications use the same URL names. At Line 21 in school/urls.py, path('student/', include(('student.urls', 'student'), namespace='student')),
6. namespace='student is set. Remember, Both Name and Namespace are important for the assignment
7. For this assignment's test cases we have used some predefined names and namespace
8. Those names are defined below in the problem statement describes as "Django Url name"
9. Please make sure you use those names in Django URLs or else your assignment's test will fail Summary: Namespace is "'student" set in school/urls.py file and name is to be set for each URL in 'student/urls which is stated in the problem statement

### Views


#### You have to use function based views for this assignment


**Part 1: GET and POST request for fetching Students**

Django URL name: student_list_create<br />

Actions:<br />

1. GET - get list of all students
2. POST - Add a new student 

```
1. GET
Response Format:
[{"id":id,"student_regNo":student_regNo,"student_name":student_name,"student_email":student_email,"student_mobile":student_mobile,"created_at":created_at},   {"id":id,"student_regNo":student_regNo,"student_name":student_name,"student_email":student_email,"student_mobile":student_mobile,"created_at":created_at}]
  
Request: /student/

Response: [{"id":2,"student_regNo":"123","student_name":"rahul","student_email":"rahul123@gmail.com","student_mobile":"0000000000","created_at":"2021-03-24T21:30:19.667926Z"},{"id":3,"student_regNo":"1234","student_name":"argo","student_email":"argo@gmail.com","student_mobile":"999999999","created_at":"2021-03-24T21:30:57.277179Z"}]

Response Code : 200
```

```
2. POST
Response Format:
{"id":id,"student_regNo":student_regNo,"student_name":student_name,"student_email":student_email,"student_mobile":student_mobile,"created_at":created_at}

Request: /student/

Response: {"id":4,"student_regNo":"12345","student_name":"Tarun","student_email":"Tarun@gmail.com","student_mobile":"777777777","created_at":"2021-03-24T21:39:11.495442Z"}

Response code: 201
```

**Part 2: Retrieve, Update and Delete**

Django URL name: student_update_delete<br />


1. GET - Retrive information of each student
2. PUT - Update any student information
3. DELETE - Remove student from the record

```
1.GET
Response Format:
{"id":id,"student_regNo":student_regNo,"student_name":student_name,"student_email":student_email,"student_mobile":student_mobile,"created_at":created_at}

Request: /student/2

Response: {"id":2,"student_regNo":"123","student_name":"rahul","student_email":"rahul123@gmail.com","student_mobile":"0000000000","created_at":"2021-03-24T21:30:19.667926Z"}

Response code: 200
```

``` 
2. PUT
Response Format: 
{"id":id,"student_regNo":student_regNo,"student_name":student_name,"student_email":student_email,"student_mobile":student_mobile,"created_at":created_at}

Request: student/2" -d "student_name=rahul1&student_regNo=123&student_email=test@gmail.com"

Response
{"id":2,"student_regNo":"123","student_name":"rahul1","student_email":"test@gmail.com","student_mobile":"0000000000","created_at":"2021-03-25T15:48:40.125929Z"}
Response code: 200
```


```
3. DELETE
No Response

Request: /student/2

Response code: 204
```
 
Note: id is the primary key which is being passed in the url<br />
 
Reference: https://www.django-rest-framework.org/api-guide/generic-views/


## Installation Steps
1. Open up your Terminal / Command Line
2. git clone the repository
3. cd into the directory of the step (the one you just git cloned)
4. make sure you have python3 installed
5. Install virtualenv by following the steps 
```
Mac
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate

Windows
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
```
6. Run 
```
python -m pip install -r requirements/requirements.txt
```
6. No Database setup needs to be done. Do not edit Database settings in settings.py

7. If everything runs fine till here, create the application using the command
```
python manage.py startapp student
```
8. Now uncomment the following lines
```
Line 21 in school/urls.py -> path('student/', include(('student.urls', 'student'), namespace='student')),
Line 41 in school/settings.py -> 'student',
```
Now Create File school/urls.py and add lines
```
from django.urls import path

from . import views
urlpatterns = []
```
9. Run 
```
python manage.py makemigrations
```
10. Now Run the Server using command
```
python manage.py runserver
```
11.  Great! Start Coding the assignment for above usecase
12. After Finishing the assignment, you can test them locally using command 
```
coverage run --source='.' manage.py test --no-input
```
12. Push the code into the repo using git, Check Pull Requests Tab. Open PR #1
13. Check if all the tests are Passed
14. Contact TA for the review
