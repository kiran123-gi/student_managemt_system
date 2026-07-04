from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# CREATE + SEARCH + READ
def student_list(request):
    query = request.GET.get('q')
    
    if query:
        students = Student.objects.filter(name__icontains=query) | Student.objects.filter(roll_no__icontains=query)
    else:
        students = Student.objects.all()

    return render(request, 'student_list.html', {'students': students})


# CREATE
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})


# UPDATE
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'add_student.html', {'form': form})


# DELETE
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')
