from django.test import TestCase
from patient.models import Patient
from django.urls import reverse
import ast

class PatientTestCase(TestCase):
    def setUp(self):
        Patient.objects.create(patient_regNo='10', patient_name='Rahul', patient_email='rahul@gmail.com', patient_mobile='000')
        Patient.objects.create(patient_regNo='11', patient_name='Argo', patient_email='argo@gmail.com', patient_mobile='111')
        Patient.objects.create(patient_regNo='12', patient_name='Disha', patient_email='disha@gmail.com', patient_mobile='222')

    def test_patient_get_query(self):
        patient = Patient.objects.get(patient_regNo="10")
        self.assertEqual(str(patient), 'Rahul')
        self.assertTrue(isinstance(patient, Patient))
    
    
    def test_patients_get_req(self):
        url = reverse('patient:patient_list_create')
        response = self.client.get(url)
        self.assertEqual(len(ast.literal_eval(response.content.decode('utf-8'))), len([{"id":1,"patient_regNo":"10","patient_name":"Rahul","patient_email":"rahul@gmail.com","patient_mobile":"000","admitted_at":"2021-04-07T19:35:54.580287Z"},{"id":2,"patient_regNo":"11","patient_name":"Argo","patient_email":"argo@gmail.com","patient_mobile":"111","admitted_at":"2021-04-07T19:35:54.580742Z"},{"id":3,"patient_regNo":"12","patient_name":"Disha","patient_email":"disha@gmail.com","patient_mobile":"222","admitted_at":"2021-04-07T19:35:54.581303Z"}]))
        for i in list(ast.literal_eval(response.content.decode('utf-8'))):
            self.assertEqual(list(i.keys()), ['id', 'patient_regNo', 'patient_name', 'patient_email', 'patient_mobile', 'admitted_at'])
        self.assertEqual(response.status_code, 200)
    
    def test_patient_get_req(self):
        url = reverse('patient:patient_update_delete', args=['1'])
        response = self.client.get(url)
        self.assertEqual(len(ast.literal_eval(response.content.decode('utf-8'))), len({"id":1,"patient_regNo":"10","patient_name":"Rahul","patient_email":"rahul@gmail.com","patient_mobile":"000","admitted_at":"2021-04-07T19:35:54.580287Z"}))
        self.assertEqual(ast.literal_eval(response.content.decode('utf-8'))['patient_regNo'], '10')
        self.assertEqual(ast.literal_eval(response.content.decode('utf-8'))['patient_name'], 'Rahul')
        self.assertEqual(response.status_code, 200)
    
    def test_patient_post_req_1(self):
        url = reverse('patient:patient_list_create')
        response = self.client.post(url,{'patient_regNo': '12','patient_name': 'Tarun','patient_email':'tarun@gmail.vcom','patient_mobile':'222'})
        self.assertEqual(response.content.decode('utf-8'), '{"patient_regNo":["patient with this patient regNo already exists."]}')
        self.assertEqual(response.status_code, 400)
    
    def test_patient_post_req_2(self):
        url = reverse('patient:patient_list_create')
        response = self.client.post(url,{'patient_regNo': '13','patient_name': 'Tarun','patient_email':'tarun@gmail.vcom','patient_mobile':'222'})
        self.assertEqual(response.content.decode('utf-8')[:-26], '{"id":4,"patient_regNo":"13","patient_name":"Tarun","patient_email":"tarun@gmail.vcom","patient_mobile":"222","admitted_at":"2021-04-07T20:16:36.673952Z"}'[:-26])
        self.assertEqual(response.status_code, 201)
    
    def test_patient_put_req(self):
        url = reverse('patient:patient_update_delete', args=['1'])
        response = self.client.put(url,{'patient_regNo': '14','patient_name': 'Tarun1','patient_email':'tarun@gmail.vcom','patient_mobile':'222'}, content_type='application/json')
        self.assertEqual(response.content.decode('utf-8')[:-26], '{"id":1,"patient_regNo":"14","patient_name":"Tarun1","patient_email":"tarun@gmail.vcom","patient_mobile":"222","admitted_at":"2021-04-07T20:16:36.673952Z"}'[:-26])
        self.assertEqual(response.status_code, 200)
    
    def test_patient_delete_req(self):
        url = reverse('patient:patient_update_delete', args=['1'])
        response = self.client.delete(url)
        self.assertEqual(response.content.decode('utf-8'), '')
        self.assertEqual(response.status_code, 204)
        patient = Patient.objects.filter(patient_regNo="10").first()
        self.assertEqual(patient, None )