from django.shortcuts import redirect, render
from discussion.models import FacultyDiscussion, StudentDiscussion
from main.models import Student, Faculty, Course
from itertools import chain
from .forms import StudentDiscussionForm, FacultyDiscussionForm


# Create your views here.


''' We have two different user models.
    That's why we are filtering the discussions based on the user type and then combining them.'''


def context_list(course):
    try:
        studentDis = StudentDiscussion.objects.filter(course=course)
        facultyDis = FacultyDiscussion.objects.filter(course=course)
        discussions = list(chain(studentDis, facultyDis))
        discussions.sort(key=lambda x: x.sent_at, reverse=True)

        for dis in discussions:
            if dis.__class__.__name__ == 'StudentDiscussion':
                dis.author = Student.objects.get(student_id=dis.sent_by_id)
            else:
                dis.author = Faculty.objects.get(faculty_id=dis.sent_by_id)
    except:

        discussions = []

    return discussions


def discussion(request, code):
    course = Course.objects.get(code=code)
    discussions = context_list(course)
    if 'student_id' in request.session:
        student = Student.objects.get(student_id=request.session['student_id'])
        form = StudentDiscussionForm()
        context = {
            'course': course,
            'student': student,
            'discussions': discussions,
            'form': form,
        }
        return render(request, 'discussion/discussion.html', context)

    elif 'faculty_id' in request.session:
        faculty = Faculty.objects.get(faculty_id=request.session['faculty_id'])
        form = FacultyDiscussionForm()
        context = {
            'course': course,
            'faculty': faculty,
            'discussions': discussions,
            'form': form,
        }
        return render(request, 'discussion/discussion.html', context)
    else:
        return redirect('std_login')


def send(request, code, std_id):
    course = Course.objects.get(code=code)
    try:
        student = Student.objects.get(student_id=std_id)
    except:
        return redirect('discussion', code=code)
    if request.method == 'POST':
        form = StudentDiscussionForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            try:
                StudentDiscussion.objects.create(
                    content=content, course=course, sent_by=student)
            except Exception as e:
                discussions = context_list(course)
                form = StudentDiscussionForm(request.POST)
                context = {
                    'course': course,
                    'student': student,
                    'discussions': discussions,
                    'form': form,
                    'form_errors': form.errors,
                    'error_message': str(e),
                }
                return render(request, 'discussion/discussion.html', context)
            return redirect('discussion', code=code)
        else:
            discussions = context_list(course)
            form = StudentDiscussionForm(request.POST)
            context = {
                'course': course,
                'student': student,
                'discussions': discussions,
                'form': form,
                'form_errors': form.errors,
            }
            return render(request, 'discussion/discussion.html', context)
    else:
        return redirect('discussion', code=code)


def send_fac(request, code, fac_id):
    course = Course.objects.get(code=code)
    try:
        faculty = Faculty.objects.get(faculty_id=fac_id)
    except:
        return redirect('discussion', code=code)
    if request.method == 'POST':
        form = FacultyDiscussionForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            try:
                FacultyDiscussion.objects.create(
                    content=content, course=course, sent_by=faculty)
            except Exception as e:
                discussions = context_list(course)
                form = FacultyDiscussionForm(request.POST)
                context = {
                    'course': course,
                    'faculty': faculty,
                    'discussions': discussions,
                    'form': form,
                    'form_errors': form.errors,
                    'error_message': str(e),
                }
                return render(request, 'discussion/discussion.html', context)
            return redirect('discussion', code=code)
        else:
            discussions = context_list(course)
            form = FacultyDiscussionForm(request.POST)
            context = {
                'course': course,
                'faculty': faculty,
                'discussions': discussions,
                'form': form,
                'form_errors': form.errors,
            }
            return render(request, 'discussion/discussion.html', context)
    else:
        return redirect('discussion', code=code)
