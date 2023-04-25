from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from .models import Teacher
from .filters import FilterTeacher
from .forms import AddTeacherForm
from django.contrib import messages, auth
# Create your views here.
class Home(View):
    def get(self,request):
        all_teacher = Teacher.objects.all()
        paginator = Paginator(all_teacher,6 )
        page_num = request.GET.get('page')
        page = paginator.get_page(page_num)
        filters = FilterTeacher(request.GET, queryset=all_teacher)
        context = {'filters': filters, 'allteacher': filters.qs,'page': page}
        return render(request,'adminteacher.html',context)


@login_required(login_url="login")
def add_teacher(request):
    fm = AddTeacherForm
    if request.method == "POST":
        fm = AddTeacherForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/teacher')
    else:
        return render(request,'add-teacher.html',{'form':fm})
