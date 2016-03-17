from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default="")

    def __unicode__(self):
        return self.name

class Discipline(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100, default="")
	ege = models.SmallIntegerField(default=0)
	date = models.DateField(blank=True, null=True, default=None)
	code = models.PositiveIntegerField(blank=True, null=True, default=None)

	def __unicode__(self):
		return self.name

class Speciality(models.Model):
	id = models.AutoField(primary_key=True)
	department = models.ForeignKey('Department')
	code = models.CharField(max_length=15)
	name = models.CharField(max_length=255)
	education_form_type = models.CharField(max_length=50, default='normal')
	plan_all = models.IntegerField(default=0)
	plan_contract = models.IntegerField(default=0)
	plan_paid = models.IntegerField(default=0)
	applications_all = models.IntegerField(default=0)
	applications_contract = models.IntegerField(default=0)
	applications_paid = models.IntegerField(default=0)
	hors_concours = models.IntegerField(default=0)
	medal = models.IntegerField(default=0)
	olympiad = models.IntegerField(default=0)
	original = models.IntegerField(default=0)
	contest_all = models.IntegerField(default=0)
	contest_contract = models.IntegerField(default=0)
	contest_paid = models.IntegerField(default=0)
	short_name = models.CharField(max_length=100)
	original_all = models.PositiveIntegerField(default=0)
	original_contract = models.PositiveIntegerField(default=0)
	original_paid = models.PositiveIntegerField(default=0)
	group_id = models.PositiveIntegerField(blank=True, null=True, default=None)
	education_level_id = models.PositiveIntegerField(blank=True, null=True, default=None)
	export_to_fis = models.PositiveSmallIntegerField(default=1)
	fis_id = models.CharField(max_length=45)
	original_first_wave = models.IntegerField(default=0)
	plan_hors_concours = models.IntegerField(default=0)
	original_hors_concours = models.IntegerField(default=0)
	fis_suffix = models.CharField(max_length=45)
	contest_hors_concours = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name

class Exam_scale(models.Model):
	speciality = models.ForeignKey('Speciality')
	discipline = models.ForeignKey('Discipline')
	interview_form = models.SmallIntegerField(default=0)
	ball_3 = models.IntegerField(default=0)
	ball_4 = models.IntegerField(default=0)
	ball_5 = models.IntegerField(default=0)

	def __unicode__(self):
		return self.speciality.name + " | " + self.discipline.name

class Exam(models.Model):
	speciality = models.ForeignKey('Speciality')
	discipline = models.ForeignKey('Discipline')
	order = models.SmallIntegerField(default=0)
	exam_form = models.CharField(max_length=15)
	result_form = models.CharField(max_length=4)

	def __unicode__(self):
		return self.speciality.name + " | " + self.discipline.name

class Satisfactory_mark(models.Model):
	code = models.CharField(max_length=15)
	name = models.CharField(max_length=100)
	mark = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return self.name