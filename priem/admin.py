from django.contrib import admin

# Register your models here.
from .models import Department, Discipline, Speciality, Exam_scale, Exam, Satisfactory_mark

class DepartmentAdmin(admin.ModelAdmin):
	search_fields = ['name']

class DisciplineAdmin(admin.ModelAdmin):
	search_fields = ['name']

class SpecialityAdmin(admin.ModelAdmin):
	search_fields = ['name']

class Exam_scaleAdmin(admin.ModelAdmin):
	search_fields = ['speciality__name', 'discipline__name']

class ExamAdmin(admin.ModelAdmin):
	search_fields = ['speciality__name', 'discipline__name']

class Satisfactory_markAdmin(admin.ModelAdmin):
	search_fields = ['name']


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Exam_scale, Exam_scaleAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Satisfactory_mark, Satisfactory_markAdmin)