# -*- coding: utf-8 -*-

from django import forms
from django.forms import TextInput, CheckboxInput, RadioSelect
from django.utils.translation import ugettext as _

EDUCATION_CHOICES =           [('secondary',_(u'Среднее')), ('secondaryProfessional',_(u'Среднее профессиональное'))]
EDUCATION_FORM_TYPE_CHOICES = [('normal',_(u'Очная')), ('correspondence',_(u'Заочная'))]
# ACHIVMENT_CHOICES = [('volunteer','Волонтер'), ('essay','Сочинение')]

class DataForm(forms.Form):
    education =               forms.ChoiceField(label='', choices=EDUCATION_CHOICES, widget=RadioSelect(attrs={'class':'big-radio education-radio'}))
    educationFormType =       forms.ChoiceField(label='', choices=EDUCATION_FORM_TYPE_CHOICES, widget=RadioSelect(attrs={'class':'big-radio education-radio'}))
    russian =                 forms.CharField(label=_(u'Русский язык'), widget=TextInput(attrs={'type':'number', 'min':'0', 'max':'100', 'class':'form-control ball-box'}))
    math =                    forms.CharField(label=_(u'Математика'), widget=TextInput(attrs={'type':'number', 'min':'0', 'max':'100', 'class':'form-control ball-box'}))
    literature =              forms.CharField(label=_(u'Литература'), widget=TextInput(attrs={'type':'number', 'min':'0', 'max':'100', 'class':'form-control ball-box'}))
    foreignLanguage =         forms.CharField(label=_(u'Иностранный язык'), widget=TextInput(attrs={'type':'number', 'min':'0', 'max':'100', 'class':'form-control ball-box'}))
    english =                 forms.CharField(label=_(u'Английский язык'), widget=TextInput(attrs={'type':'number', 'min':'0', 'max':'100', 'class':'form-control ball-box'}))
    german =                  forms.CharField(label=_(u'Немецкий язык'), widget=TextInput(attrs={'type':'number', 'min':'0', 'max':'100', 'class':'form-control ball-box'}))
    history =                 forms.CharField(label=_(u'История'), widget=TextInput(attrs={'type':'number', 'min':'0', 'max':'100', 'class':'form-control ball-box'}))
    socialScience =           forms.CharField(label=_(u'Обществознание'), widget=TextInput(attrs={'type':'number', 'min':'0', 'max':'100', 'class':'form-control ball-box'}))
    chemistry =               forms.CharField(label=_(u'Химия'), widget=TextInput(attrs={'type':'number', 'min':'0', 'max':'100', 'class':'form-control ball-box'}))
    biology =                 forms.CharField(label=_(u'Биология'), widget=TextInput(attrs={'type':'number', 'min':'0', 'max':'100', 'class':'form-control ball-box'}))
    geography =               forms.CharField(label=_(u'География'), widget=TextInput(attrs={'type':'number', 'min':'0', 'max':'100', 'class':'form-control ball-box'}))
    physics =                 forms.CharField(label=_(u'Физика'), widget=TextInput(attrs={'type':'number', 'min':'0', 'max':'100', 'class':'form-control ball-box'}))
    computerScience =         forms.CharField(label=_(u'Информатика и ИКТ'), widget=TextInput(attrs={'type':'number', 'min':'0', 'max':'100', 'class':'form-control ball-box'}))
    volunteer =               forms.BooleanField(label=_(u'Осуществление волонтерской деятельности (1 балл)'), widget=CheckboxInput(attrs={'class':'big-checkbox'}))
    certificate =             forms.BooleanField(label=_(u'Наличие аттестата о среднем общем образовании с отличием | Наличие золотой или серебрянной медали (3 балла)'), widget=CheckboxInput(attrs={'class':'big-checkbox'}))
    certificateProfessional = forms.BooleanField(label=_(u'Наличие диплома о среднем профессиональном образовании с отличием (3 балла)'), widget=CheckboxInput(attrs={'class':'big-checkbox'}))
    olympiad =                forms.BooleanField(label=_(u'Участие в олимпиадах (2 балла)'), widget=CheckboxInput(attrs={'class':'big-checkbox'}))
    champion =                forms.BooleanField(label=_(u'Наличие статуса чемпиона | Наличие золотого знака отличия ГТО (2 балла)'), widget=CheckboxInput(attrs={'class':'big-checkbox'}))
    other =                   forms.BooleanField(label=_(u'Участие в иных конкурсах и мероприятиях (2 балла)'), widget=CheckboxInput(attrs={'class':'big-checkbox'}))