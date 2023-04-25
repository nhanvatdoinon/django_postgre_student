import django_filters


from .models import Teacher

class FilterTeacher(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'name':['icontains']
        #    ,'phone':['icontains']
         #   ,'address':['icontains']
            ,'age':['lt','gt']
            ,'gender':['exact']
        }
        # fields = '__all__'
