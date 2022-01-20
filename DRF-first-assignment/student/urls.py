
from django.urls import path, include
from student import views

urlpatterns = [
    path('', views.GetStudent.as_view(), name='student_list_create'),
    path('<int:id>', views.UpdateDelStudent.as_view(), name='student_update_delete')
]