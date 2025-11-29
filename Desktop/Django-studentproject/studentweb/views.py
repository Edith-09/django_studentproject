from django.shortcuts import redirect, render, get_object_or_404

from studentweb.models import Student

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')
def student(request):
    return render(request, 'student.html')
    if request.method  == 'POST':
        name=request.POST.get('name')
        reg_no=request.POST.get('regno')
        age=request.POST.get('age')
        course=request.POST.get('course')
        phoneno=request.POST.get('phoneno')

        Student.objects.create(name=name, regno=reg_no, age=age, course=course, phoneno=phoneno)
        return redirect('admin')
    return render(request, 'add_item.html')

def delete_item(request, id):
    student = get_object_or_404(Student,id=id)
    student.delete()
    return redirect('admin')

def update_item(request,id):
    student=get_object_or_404(Student,id=id)

    if request.method == 'POST':
        student.name=request.POST.get('name')
        student.regno=request.POST.get('regno')
        student.age=request.POST.get('age')
        student.course=request.POST.get('course')
        student.phoneno=request.POST.get('phoneno')

        student.save()
        return redirect('admin')

    return render(request,'update_item.html', {'student':student})

