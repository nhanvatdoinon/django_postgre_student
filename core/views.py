from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import Q
from .filters import FilterStudent
from tuan1 import settings
from .models import Student
from .forms import  AddStudentForm,RegistrationForm,LoginForm
from django.contrib import messages, auth

@method_decorator(login_required(login_url="login"), name='dispatch')
class Home(View):
    def get(self,request):
        all_student = Student.objects.all()
        paginator = Paginator(all_student,6 )
        page_num = request.GET.get('page')
        page = paginator.get_page(page_num)
        filters = FilterStudent(request.GET, queryset=all_student)
        context = {'filters': filters, 'allstudent': filters.qs,'page': page}
        return render(request,'admin.html',context)

def search(request):
    if request.method == "GET":
        q = request.GET['q']
        if q:
            student_search = Student.objects.filter(Q(name__icontains=q)|Q(phone__icontains=q)|Q(address__icontains=q))
        else:
            student_search = Student.objects.all()
        return render(request, 'admin.html', {'allstudent': student_search})

@login_required(login_url="login")
def add_student(request):
    fm = AddStudentForm
    if request.method == "POST":
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/student')
    else:
        return render(request,'add-student.html',{'form':fm})

@login_required(login_url='/login')
def delete_student(request,id):
    std_delete = Student.objects.get(id=id)
    if request.method == 'POST':
        std_delete.delete()
        return redirect('/student')
    return render(request,'delete-student.html')
    # data = request.POST
    # id = data.get('id')
    # std_delete = Student.objects.get(id=id)
    # std_delete.delete()
    # return redirect('/student')

@login_required(login_url='/login')
def edit_student(request, id):
    std_edit = Student.objects.get(id=id)
    form = AddStudentForm(request.POST, instance=std_edit)
    if form.is_valid():
        form.save()
        return redirect('/student')
    return render(request,'edit-student.html',{'form':form})

def home(request):
    return render(request,'home.html')
def register(request):
    if request.user.is_authenticated:
        return redirect('student')
    else:
        form = RegistrationForm()
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                mydict = {'username': form.cleaned_data['username']}
                html_template = 'register_email.html'
                html_message = render_to_string(html_template, context=mydict)
                subject = 'Xin chào '
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['nguyenkimtoanmta@gmail.com']
                massage = EmailMessage(subject, html_message, email_from, recipient_list)
                massage.content_subtype = 'html'
                massage.send()
                messages.success(request, "Đăng kí thành công")
                return redirect('/login')
        return render(request,'register.html',{'form':form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('student')
    else:
        form = LoginForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username = username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/student')
            else:
                messages.info(request,'Tài khoản hoặc mật khẩu không đúng')
                #return render(request, 'login.html', {'form': form})
        else:
            return render(request,'login.html',{'form':form})

@login_required()
def logout(request):
    auth.logout(request)
    return redirect('login')

