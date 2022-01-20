from . import views
from django.urls import path, include

urlpatterns = [
   
    path('simpleapp/',views.find_square1,name= "array_addition"),    
    path('simpleapp/<int:number>',views.find_square1,name= "array_addition"),
    path('palindrome_check/',views.check_palindrome1,name= "palindrome_check"),
    path('palindrome_check/<str:string>',views.check_palindrome2,name= "palindrome_check"),
    path('array_addition/',views.add_array,name= "index"),
    
]