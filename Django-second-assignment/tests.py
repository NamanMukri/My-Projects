from django.test import TestCase
from animals.models import Mammal, Bird, Fish
from django.urls import reverse

class AnimalTestCase(TestCase):
    def setUp(self):
        Mammal.objects.create(name='lion', species='Panthera', gender='M', food='meat')
        Bird.objects.create(name='Parrot', species='parrata', food='insects')
        Fish.objects.create(species='GoldFisha', food='grain', count=100,color='yellow')

    def test_mammal_get_query(self):
        """Animals that can speak are correctly identified"""
        lion = Mammal.objects.get(species="Panthera")
        self.assertEqual(str(lion), 'lion')
        self.assertTrue(isinstance(lion, Mammal))
    
    def test_bird_get_query(self):
        """Animals that can speak are correctly identified"""
        lion = Bird.objects.get(species="parrata")
        self.assertEqual(str(lion), 'Parrot')
        self.assertTrue(isinstance(lion, Bird))
    
    def test_fish_get_query(self):
        """Animals that can speak are correctly identified"""
        lion = Fish.objects.get(color="yellow")
        self.assertEqual(str(lion), 'GoldFisha')
        self.assertTrue(isinstance(lion, Fish))
    
    def test_mammals_get_req(self):
        url = reverse('animals:mammals')
        response = self.client.get(url)
        self.assertEqual(response.content.decode('utf-8'), '{"data": [["lion", "Panthera", "M", "meat"]]}')
        self.assertEqual(response.status_code, 200)
    
    def test_bird_get_req(self):
        url = reverse('animals:birds')
        response = self.client.get(url)
        self.assertEqual(response.content.decode('utf-8'), '{"data": [["Parrot", "parrata", "insects"]]}')
        self.assertEqual(response.status_code, 200)
    
    def test_fish_get_req(self):
        url = reverse('animals:fishes')
        response = self.client.get(url)
        self.assertEqual(response.content.decode('utf-8'), '{"data": [["yellow", "GoldFisha", "grain", 100]]}')
        self.assertEqual(response.status_code, 200)

    def test_mammals_post_req(self):
        url = reverse('animals:mammals')
        response = self.client.post(url,{'name': 'tiger','species': 'Sumatran','gender':'M','food':'chicken'})
        self.assertEqual(response.content.decode('utf-8'), '{"created": {"name": "tiger"}}')
        self.assertEqual(response.status_code, 200)
        lion = Mammal.objects.get(species="Sumatran")
        self.assertEqual(str(lion), 'tiger')
    
    def test_bird_post_req(self):
        url = reverse('animals:birds')
        response = self.client.post(url,{'name': 'crow','species': 'crowa','food':'meat'})
        self.assertEqual(response.content.decode('utf-8'), '{"created": {"name": "crow"}}')
        self.assertEqual(response.status_code, 200)
        lion = Bird.objects.get(species="crowa")
        self.assertEqual(str(lion), 'crow')
    
    def test_fish_post_req(self):
        url = reverse('animals:fishes')
        response = self.client.post(url,{'color':'brown','species': 'Tuna','food':'grains','count':2000})
        self.assertEqual(response.content.decode('utf-8'), '{"created": {"species": "Tuna"}}')
        self.assertEqual(response.status_code, 200)
        lion = Fish.objects.get(color="brown")
        self.assertEqual(str(lion), 'Tuna')
    
    

