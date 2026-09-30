from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('create/',views.create_students),
    path('students/',views.display_students),
    path('add/',views.AddStudent.as_view()),
    path('get/<int:id>',views.GetStudent.as_view()),
    path('update/<int:id>',views.UpdateStudent.as_view()),
    path('delete/<int:id>',views.DeleteStudent.as_view())
]