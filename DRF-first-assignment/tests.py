from django.test import TestCase
from student.models import Student
from django.urls import reverse
import ast

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(student_regNo='10', student_name='Rahul', student_email='rahul@gmail.com', student_mobile='000')
        Student.objects.create(student_regNo='11', student_name='Argo', student_email='argo@gmail.com', student_mobile='111')
        Student.objects.create(student_regNo='12', student_name='Disha', student_email='disha@gmail.com', student_mobile='222')

    def test_student_get_query(self):
        student = Student.objects.get(student_regNo="10")
        self.assertEqual(str(student), 'Rahul')
        self.assertTrue(isinstance(student, Student))
    
    
    def test_students_get_req(self):
        url = reverse('student:student_list_create')
        response = self.client.get(url)
        self.assertEqual(len(ast.literal_eval(response.content.decode('utf-8'))), len([{"id":1,"student_regNo":"10","student_name":"Rahul","student_email":"rahul@gmail.com","student_mobile":"000","created_at":"2021-04-07T19:35:54.580287Z"},{"id":2,"student_regNo":"11","student_name":"Argo","student_email":"argo@gmail.com","student_mobile":"111","created_at":"2021-04-07T19:35:54.580742Z"},{"id":3,"student_regNo":"12","student_name":"Disha","student_email":"disha@gmail.com","student_mobile":"222","created_at":"2021-04-07T19:35:54.581303Z"}]))
        for i in list(ast.literal_eval(response.content.decode('utf-8'))):
            self.assertEqual(list(i.keys()), ['id', 'student_regNo', 'student_name', 'student_email', 'student_mobile', 'created_at'])
        self.assertEqual(response.status_code, 200)
    
    def test_student_get_req(self):
        url = reverse('student:student_update_delete', args=['1'])
        response = self.client.get(url)
        self.assertEqual(len(ast.literal_eval(response.content.decode('utf-8'))), len({"id":1,"student_regNo":"10","student_name":"Rahul","student_email":"rahul@gmail.com","student_mobile":"000","created_at":"2021-04-07T19:35:54.580287Z"}))
        self.assertEqual(ast.literal_eval(response.content.decode('utf-8'))['student_regNo'], '10')
        self.assertEqual(ast.literal_eval(response.content.decode('utf-8'))['student_name'], 'Rahul')
        self.assertEqual(response.status_code, 200)
    
    def test_student_post_req_1(self):
        url = reverse('student:student_list_create')
        response = self.client.post(url,{'student_regNo': '12','student_name': 'Tarun','student_email':'tarun@gmail.vcom','student_mobile':'222'})
        self.assertEqual(response.content.decode('utf-8'), '{"student_regNo":["student with this student regNo already exists."]}')
        self.assertEqual(response.status_code, 400)
    
    def test_student_post_req_2(self):
        url = reverse('student:student_list_create')
        response = self.client.post(url,{'student_regNo': '13','student_name': 'Tarun','student_email':'tarun@gmail.vcom','student_mobile':'222'})
        self.assertEqual(response.content.decode('utf-8')[:-26], '{"id":4,"student_regNo":"13","student_name":"Tarun","student_email":"tarun@gmail.vcom","student_mobile":"222","created_at":"2021-04-07T20:16:36.673952Z"}'[:-26])
        self.assertEqual(response.status_code, 201)
    
    def test_student_put_req(self):
        url = reverse('student:student_update_delete', args=['1'])
        response = self.client.put(url,{'student_regNo': '14','student_name': 'Tarun1','student_email':'tarun@gmail.vcom','student_mobile':'222'}, content_type='application/json')
        self.assertEqual(response.content.decode('utf-8')[:-26], '{"id":1,"student_regNo":"14","student_name":"Tarun1","student_email":"tarun@gmail.vcom","student_mobile":"222","created_at":"2021-04-07T20:16:36.673952Z"}'[:-26])
        self.assertEqual(response.status_code, 200)
    
    def test_student_delete_req(self):
        url = reverse('student:student_update_delete', args=['1'])
        response = self.client.delete(url)
        self.assertEqual(response.content.decode('utf-8'), '')
        self.assertEqual(response.status_code, 204)
        student = Student.objects.filter(student_regNo="10").first()
        self.assertEqual(student, None )