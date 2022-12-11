from django.contrib import admin
from app_1.models import person,Group,issue,car
from django.db import models



@admin.register(person)

class personAdmin(admin.ModelAdmin):
    search_fields = ['first_name']
    list_display = ('first_name', 'last_name', 'age','gender','date')
    #fields = (('first_name', 'last_name'), 'age', 'gender','date')
    #exclude = ['age']
    list_filter = ['gender']
    list_per_page = 5 
    #date_hierarchy = 'pub_date'
    #empty_value_display = '-empty-'
    #empty_value_display = 'unknown'
    list_display_links = ('first_name', 'last_name')
    list_select_related = ()
    person_fields = {"slug": ("date",)}
    #list_select_related = ('author', 'category')#multiple models
    #radio_fields = {"group": admin.HORIZONTAL}  #foreign key
    ordering = ['first_name']
    #autocomplete_fields = ['question']    #foreign key
    #raw_id_fields = ("age",)  #must be a foreign key or a many-to-many field.
    #readonly_fields = ('age',)  #age automatic default
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(person=request.user)
# class Media:
#     css = {
#         "all": ("my_styles.css",)
#     }
#     js = ("my_code.js",)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    
    list_display = ['products_list', ]

@admin.register(issue)
class issueAdmin(admin.ModelAdmin):
    list_display = ('person','issue_name','join_date','Discharge_date')
    list_filter = ['issue_name']
    list_per_page = 2 



@admin.register(car)
class carAdmin(admin.ModelAdmin):
    list_per_page = 2 
 

    







    '''@admin.display(empty_value='unknown')
    def age_view(self, person):
         return person.age
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    birthday = models.DateField()

    @admin.display(boolean=True)
    def born_in_fifties(self):
        return 1950 <= self.birthday.year < 1960

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'born_in_fifties')

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name','gender','date')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('add_template','remove_template'),
        }),
    )'''
'''class Meta:
        model = person
        exclude = ['last_name']'''

'''@admin.display(description='Name')
def upper_case_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name)).upper()

class personAdmin(admin.ModelAdmin):
    list_display = (upper_case_name,)

    @admin.display(description='Birth decade')
    def decade_born_in(self):
        return '%d's' % (self.birthday.year // 10 * 10)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'decade_born_in')'''

    

