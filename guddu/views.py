from django.http import JsonResponse
from django.shortcuts import render
from .models import Student
from random import randint
from django.core.paginator import Paginator
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def create_students(req):
    students = []
    for i in range(1,101):
        student = Student(
            name = f'Student {i}',
            age = randint(18,80),
            marks = randint(35,100)
        )
        students.append(student)
    Student.objects.bulk_create(students)
    return JsonResponse({'status':'Students Added!'})


def display_students(req):
    all_stu = Student.objects.all()
    paginator = Paginator(all_stu,10)
    page_no = req.GET.get('page')
    stu_info = paginator.get_page(page_no)
    return render(req,'home.html',{'stu_info':stu_info})

@method_decorator(csrf_exempt,name='dispatch')
class AddStudent(View):
    def post(self,req):
        Student.objects.create(
            name = req.POST.get('name'),
            age = req.POST.get('age'),
            marks = req.POST.get('marks'),
            password = req.POST.get('password')
        )
        return JsonResponse({'status':'Student Added!'})

class GetStudent(View):
    def get(self,req,id):
        stu_obj = Student.objects.get(id=id)
        return JsonResponse({'student':stu_obj})

method_decorator(csrf_exempt,name='dispatch')
class UpdateStudent(View):
    def post(self,req,id):
        stu_obj = Student.objects.get(id=id)
        stu_obj.name = req.POST.get('name')
        stu_obj.age = req.POST.get('age')
        stu_obj.marks = req.POST.get('marks')
        stu_obj.password = req.POST.get('password')
        stu_obj.save()
        return JsonResponse({'status':'Student Updated!'})

class DeleteStudent(View):
    def get(self,req,id):
        student = Student.objects.get(id=id)
        student.delete()
        return JsonResponse({'status':'Student Deleted!'})