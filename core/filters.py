import django_filters


from .models import Student

class FilterStudent(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'name':['icontains']
        #    ,'phone':['icontains']
         #   ,'address':['icontains']
            ,'age':['lt','gt']
            ,'gender':['exact']
        }
        # fields = '__all__'
