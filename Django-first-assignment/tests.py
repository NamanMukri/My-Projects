from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class SimpleTest(TestCase):
    
    def test_get_http_no_number(self):
        url = reverse('simpleapp:index')
        response = self.client.get(url+'')
        self.assertEqual(response.content.decode('utf-8'), "Send Parameter number in url")
        self.assertEqual(response.status_code, 200)
    
    def test_get_http_number(self):
        url = reverse('simpleapp:index')
        response = self.client.get(url+'?number=10')
        self.assertEqual(response.content.decode('utf-8'), "Square of Number 10 is 100")
        self.assertEqual(response.status_code, 200)
    
    def test_get_http_number_incorrect(self):
        url = reverse('simpleapp:index')
        response = self.client.get(url+'?no.=10')
        self.assertEqual(response.content.decode('utf-8'), "Send Parameter number in url")

    def test_post_no_http_number(self):
        url = reverse('simpleapp:index')
        response = self.client.post(url)
        self.assertEqual(response.content.decode('utf-8'), "Send Parameter number in data")
        self.assertEqual(response.status_code, 200)

    def test_post_http_number(self):
        url = reverse('simpleapp:index')
        response = self.client.post(url, {'number': '15'})
        self.assertEqual(response.content.decode('utf-8'), '{"data": "Square of Number 15 is 225"}')
        self.assertEqual(response.status_code, 200)
    
    def test_post_http_number_incorrect(self):
        url = reverse('simpleapp:index')
        response = self.client.post(url, {'no.': '15'})
        self.assertEqual(response.content.decode('utf-8'), "Send Parameter number in data")
        self.assertEqual(response.status_code, 200)
    
    def test_put_no_http_number(self):
        url = reverse('simpleapp:index')
        response = self.client.put(url+'')
        self.assertEqual(response.content.decode('utf-8'), "Send Parameter as /simpleapp/<number>")
        self.assertEqual(response.status_code, 200)
    
    def test_put_http_number(self):
        url = reverse('simpleapp:index')
        response = self.client.put(url+'10')
        self.assertEqual(response.content.decode('utf-8'), '{"data": "Square of Number 10 is 100"}')
        self.assertEqual(response.status_code, 200)
    
    def test_delete_no_http_number(self):
        url = reverse('simpleapp:index')
        response = self.client.put(url+'')
        self.assertEqual(response.content.decode('utf-8'), "Send Parameter as /simpleapp/<number>")
        self.assertEqual(response.status_code, 200)
    
    def test_delete_http_number(self):
        url = reverse('simpleapp:index')
        response = self.client.delete(url+'60')
        self.assertEqual(response.content.decode('utf-8'), '{"data": "Square of Number 60 is 3600"}')
        self.assertEqual(response.status_code, 200)


    # Array Addition tests
    def test_get_array_addition_1(self):
        url = reverse('simpleapp:array_addition')
        response = self.client.get(url+'')
        self.assertEqual(response.content.decode('utf-8'), "Send Parameter array as comma seperated numbers 2,3,4,5")
        self.assertEqual(response.status_code, 200)

    def test_get_array_addition_2(self):
        url = reverse('simpleapp:array_addition')
        response = self.client.get(url+'?array=2,4,7,10')
        self.assertEqual(response.content.decode('utf-8'), "<h1>Sum is 23</h1>")
        self.assertEqual(response.status_code, 200)
    
    def test_get_Array_addition_3(self):
        url = reverse('simpleapp:array_addition')
        response = self.client.get(url+'?array=666,777,0,-777,-888')
        self.assertEqual(response.content.decode('utf-8'), "<h1>Sum is -222</h1>")
        self.assertEqual(response.status_code, 200)
    
    def test_get_Array_addition_4(self):
        url = reverse('simpleapp:array_addition')
        response = self.client.get(url+'?array=1230,7777,6767,8888')
        self.assertEqual(response.content.decode('utf-8'), "<h1>Sum is 24662</h1>")
        self.assertEqual(response.status_code, 200)
    
    def test_get_Array_addition_incorrect(self):
        url = reverse('simpleapp:array_addition')
        response = self.client.get(url+'?list=1230,7777,6767,8888')
        self.assertEqual(response.content.decode('utf-8'), "Send Parameter array as comma seperated numbers 2,3,4,5")
    
    def test_post_array_addition_1(self):
        url = reverse('simpleapp:array_addition')
        response = self.client.post(url+'')
        self.assertEqual(response.content.decode('utf-8'), "Send Parameter array in data as comma seperated numbers 2,3,4,5")
        self.assertEqual(response.status_code, 200)
    
    def test_post_array_addition_2(self):
        url = reverse('simpleapp:array_addition')
        response = self.client.post(url, {'array': '2,2,2,0'})
        self.assertEqual(response.content.decode('utf-8'), '{"sum": "6"}')
        self.assertEqual(response.status_code, 200)
    
    def test_post_array_addition_3(self):
        url = reverse('simpleapp:array_addition')
        response = self.client.post(url, {'array': '1230,7777,6767,8888'})
        self.assertEqual(response.content.decode('utf-8'), '{"sum": "24662"}')
        self.assertEqual(response.status_code, 200)
    
    def test_post_array_addition_4(self):
        url = reverse('simpleapp:array_addition')
        response = self.client.post(url, {'array': '666,777,0,-777,-888'})
        self.assertEqual(response.content.decode('utf-8'), '{"sum": "-222"}')
        self.assertEqual(response.status_code, 200)

    def test_post_array_addition_incorrect(self):
        url = reverse('simpleapp:array_addition')
        response = self.client.post(url, {'list': '666,777,0,-777,-888'})
        self.assertEqual(response.content.decode('utf-8'), "Send Parameter array in data as comma seperated numbers 2,3,4,5")
    
    
    # Palindrome tests

    def test_get_palindrome_default(self):
        url = reverse('simpleapp:palindrome_check')
        response = self.client.get(url+'')
        self.assertEqual(response.content.decode('utf-8'), "Send Parameter string in url to check palindrome")
        self.assertEqual(response.status_code, 200)
    
    def test_get_palindrome_1(self):
        url = reverse('simpleapp:palindrome_check')
        response = self.client.get(url+'?string=000')
        self.assertEqual(response.content.decode('utf-8'), "<b>000</b> is a palindrome")
        self.assertEqual(response.status_code, 200)
    
    def test_get_palindrome_2(self):
        url = reverse('simpleapp:palindrome_check')
        response = self.client.get(url+'?string=google')
        self.assertEqual(response.content.decode('utf-8'), "<b>google</b> is not a palindrome")
        self.assertEqual(response.status_code, 200)
    
    def test_get_palindrome_3(self):
        url = reverse('simpleapp:palindrome_check')
        response = self.client.get(url+'?string=tattarrattat')
        self.assertEqual(response.content.decode('utf-8'), "<b>tattarrattat</b> is a palindrome")
        self.assertEqual(response.status_code, 200)
    
    def test_get_palindrome_incorrect(self):
        url = reverse('simpleapp:palindrome_check')
        response = self.client.get(url+'?text=tattarrattat')
        self.assertEqual(response.content.decode('utf-8'), "Send Parameter string in url to check palindrome")
    
    def test_post_palindrome_default(self):
        url = reverse('simpleapp:palindrome_check')
        response = self.client.post(url+'')
        self.assertEqual(response.content.decode('utf-8'), "Send Parameter string in data to check palindrome")
        self.assertEqual(response.status_code, 200)
    
    def test_post_palindrome_1(self):
        url = reverse('simpleapp:palindrome_check')
        response = self.client.post(url,{'string': 'tattarrattat'})
        self.assertEqual(response.content.decode('utf-8'), '{"result": "tattarrattat is a palindrome"}')
        self.assertEqual(response.status_code, 200)
    
    def test_post_palindrome_2(self):
        url = reverse('simpleapp:palindrome_check')
        response = self.client.post(url,{'string': 'yahoo'})
        self.assertEqual(response.content.decode('utf-8'), '{"result": "yahoo is not a palindrome"}')
        self.assertEqual(response.status_code, 200)
    
    def test_post_palindrome_3(self):
        url = reverse('simpleapp:palindrome_check')
        response = self.client.post(url,{'string': '98989'})
        self.assertEqual(response.content.decode('utf-8'), '{"result": "98989 is a palindrome"}')
        self.assertEqual(response.status_code, 200)
    
    def test_post_palindrome_3(self):
        url = reverse('simpleapp:palindrome_check')
        response = self.client.post(url,{'text': '98989'})
        self.assertEqual(response.content.decode('utf-8'), "Send Parameter string in data to check palindrome")
        self.assertEqual(response.status_code, 200)
    
    def test_put_palindrome_default(self):
        url = reverse('simpleapp:palindrome_check')
        response = self.client.put(url+'')
        self.assertEqual(response.content.decode('utf-8'), "Send parameter as /palindrome_check/<string>")
        self.assertEqual(response.status_code, 200)
    
    def test_put_palindrome_1(self):
        url = reverse('simpleapp:palindrome_check')
        response = self.client.put(url+'98989')
        self.assertEqual(response.content.decode('utf-8'), '{"result": "98989 is a palindrome"}')
        self.assertEqual(response.status_code, 200)
    
    def test_put_palindrome_2(self):
        url = reverse('simpleapp:palindrome_check')
        response = self.client.put(url+'gmail')
        self.assertEqual(response.content.decode('utf-8'), '{"result": "gmail is not a palindrome"}')
        self.assertEqual(response.status_code, 200)
    
    def test_delete_palindrome_default(self):
        url = reverse('simpleapp:palindrome_check')
        response = self.client.delete(url+'')
        self.assertEqual(response.content.decode('utf-8'), "Send parameter as /palindrome_check/<string>")
        self.assertEqual(response.status_code, 200)
    
    def test_delete_palindrome_1(self):
        url = reverse('simpleapp:palindrome_check')
        response = self.client.delete(url+'98989')
        self.assertEqual(response.content.decode('utf-8'), '{"result": "98989 is a palindrome"}')
        self.assertEqual(response.status_code, 200)
    
    def test_delete_palindrome_2(self):
        url = reverse('simpleapp:palindrome_check')
        response = self.client.delete(url+'gmail')
        self.assertEqual(response.content.decode('utf-8'), '{"result": "gmail is not a palindrome"}')
        self.assertEqual(response.status_code, 200)