from django.contrib import admin
from django.urls import path, include
from patient import views

urlpatterns = [
  path('', views.GetPatient.as_view(), name='patient_list_create'),
  path('<int:id>', views.UpdateDelPatient.as_view(), name='patient_update_delete') 
]