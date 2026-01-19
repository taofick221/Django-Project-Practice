from django.contrib import admin
from My_Portfolio.models import Students,Profile,Contact

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','age','email','enrolment_date')
    search_fields=('name','age','email','enrolment_date')
    date_hierarchy='enrolment_date'
    list_filter=('name','age')

admin.site.register(Profile)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','message')