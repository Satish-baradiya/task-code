from django.shortcuts import render
from django.http import HttpResponse
from . models import Student, Teacher
from reportlab.pdfgen import canvas  
from django.http import HttpResponse  

# Create your views here.
def index(request):
    students = Student.objects.all()
    return render(request,"student/index.html",{
        "students":students
    })

def student(request,pk):
    students = Student.objects.filter(pk=pk)
    return render(request,"student/student.html",{
        "students":students
    })

def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    content = "This is certificate for" 
    p.drawString(100,700, content)  
    p.showPage()  
    p.save()  
    return response  
