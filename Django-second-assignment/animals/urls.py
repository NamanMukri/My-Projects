from django.urls import path
from . import views

urlpatterns=[
path('mammals/', views.mammals, name="mammals"),
path('birds/', views.birds, name="birds"),
path('fishes/', views.fishes, name="fishes"),

]
