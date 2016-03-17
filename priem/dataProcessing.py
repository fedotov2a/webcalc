# -*- coding: utf-8 -*-

from django.db import connection
from django.db.models import Q
from .models import Speciality, Department, Exam, Exam_scale, Discipline

def isBachelor(departmentId):
    return (departmentId >= 1 and departmentId <= 17) or (departmentId >= 25 and departmentId <= 35)

def isForeignLanguage(discip_id, disciplinesId, dataForm):
    return (discip_id == 5 and dataForm[discip_id] != '' and dataForm[discip_id] != None and 87 in disciplinesId)

def isDisciplineContainsSpeciality(discip_id, disciplinesId, dataForm):
    return (dataForm[discip_id] != '' and dataForm[discip_id] != None and (discip_id - 1) in disciplinesId)

def isResultSpecialities(countDiscipline, disciplinesId, prof):
    return (countDiscipline == (3 - prof) or (countDiscipline == (2 - prof) and len(disciplinesId) == (4 - prof)))

def printResult(result, totalResult, abiturientScores):
    if len(result) == 0:
        return u"<h1>К сожалению, мы ничего не нашли :(</h1>"
    
    res = '''<div class="container">
                <div class="row">
                    <div class="col-sm-12">'''
    for department_name in result.keys():
        # print(department_name)
        res += '''<div class="row">
                    <div class="col-sm-12">
                        <h2>''' + department_name + "</h2>"
        for speciality in result[department_name]:
            for speciality_name in speciality.keys():
                res += '''<div class="napr" style="background-color: #ccc;">
                            <div class="spoiler folded">
                                <a href="javascript:void(0);">''' + speciality[speciality_name][0] + " " + speciality_name + " " + u'<span style="background-color:#0f0; margin-left:5px;">' + str(totalResult[speciality_name]) + '</span>' + u'<span style="float:right;color:#000;font-size:22px;">↴</span>' + '''</a>
                            </div>'''
                # print(speciality[speciality_name][0] + " " + speciality_name + " " + str(totalResult[speciality_name]))
                res += u'''<div class="spoiler-text">
                            <table class="table table-bordered result">
                                <thead>
                                    <tr>
                                      <th>Предмет</th>
                                      <th>Минимальный балл</th>
                                      <th>Ваш балл</th>
                                    </tr>
                                </thead>
                                <tbody>'''
                for discipline_name in speciality[speciality_name][1]:
                    res += "<tr>"
                    if abiturientScores[speciality_name].has_key(discipline_name):
                        res += "<td>" + discipline_name + "</td>" + "<td>" + str(speciality[speciality_name][1][discipline_name]) + "</td>" + "<td>" + str(abiturientScores[speciality_name][discipline_name]) + "</td>"
                    else:
                        res += "<td>" + discipline_name + "</td>" + "<td>" + str(speciality[speciality_name][1][discipline_name]) + "</td>" + "<td></td>"
                    res += "</tr>"
                res += '''</tbody></table></div></div>'''
        res += '</div></div><br><div class="myHR">.</div>'
    res += "</div></div></div>"
    return res

def processing(form):
    prof = False
    # print (Speciality.objects.filter(short_name__contains=u"(П)").filter(education_form_type = u"normal").filter(department_id__in=[26, 16, 14])[0].code)
    result = []
    dataForm = []
    for f in form:
        dataForm.append(f.value())

    achivmentScore = dataForm[15] + 3*(dataForm[16] + dataForm[17]) + 2*(dataForm[18] + dataForm[19] + dataForm[20])

    specialities = []
    if dataForm[0] == 'secondary':
        prof = False
        specialities = Speciality.objects.exclude(short_name__contains=u"(П)").filter(education_form_type = dataForm[1])
    elif dataForm[0] == 'secondaryProfessional':
        prof = True
        specialities = Speciality.objects.filter(short_name__contains=u"(П)").filter(education_form_type = dataForm[1])

    specialityId = []
    departmentId = []
    for speciality in specialities:
        if isBachelor(speciality.department_id):
            specialityId.append(speciality.id)
            departmentId.append(speciality.department_id)

    totalResult = {}
    abiturientScores = {}
    for spec_id in specialityId:
        # filter speciality in table exam
        exams = Exam.objects.filter(speciality_id=spec_id)
        disciplinesId = []
        for exam in exams:
            disciplinesId.append(int(exam.discipline_id))

        # count need exam
        countDiscipline = 0
        total = achivmentScore
        abiturScore = {}
        for discip_id in range(2, 15):
            if isForeignLanguage(discip_id, disciplinesId, dataForm) or isDisciplineContainsSpeciality(discip_id, disciplinesId, dataForm):
                countDiscipline = countDiscipline + 1
                total += int(dataForm[discip_id])
                if discip_id == 5:
                    discip_name = Discipline.objects.filter(id=87)[0].name
                else:
                    discip_name = Discipline.objects.filter(id=discip_id - 1)[0].name
                
                abiturScore[discip_name] = dataForm[discip_id]

        resultSpecAndDiscipID = {}
        
        if isResultSpecialities(countDiscipline, disciplinesId, prof):
            # print(total)
            for exam in exams:
                resultSpecAndDiscipID[str(exam.speciality_id)] = disciplinesId
                spec_name = Speciality.objects.filter(id=int(exam.speciality_id))[0].name
                abiturientScores[spec_name] = abiturScore
                totalResult[spec_name] = total

            result.append(resultSpecAndDiscipID)
            countDiscipline = 0

    # print(result)

    # print(abiturientScores)

    #----------------------------------------------------------------
    scale = []
    result_2 = []
    temp = {}
    temp_2 = {}
    data = []
    result_3 = {}
    discipline_names = []
    for spec in result:
        for key in spec.keys():
            dep_id = Speciality.objects.filter(id=int(key))[0].department_id
            department = Department.objects.filter(id=dep_id)[0].name
            spec_name = Speciality.objects.filter(id=int(key))[0].name
            spec_code = Speciality.objects.filter(id=int(key))[0].code

            if not result_3.has_key(department):
                result_3[department] = []

            for val in spec.values()[0]:
                discipline_names.append(Discipline.objects.filter(id=val)[0].name)
                scale.append(Exam_scale.objects.filter(speciality_id=int(key)).filter(discipline_id=val)[0].ball_3)

            # print(scale)
            for x, y in zip(discipline_names, scale):
                temp[x] = y

            data.append(spec_code)
            data.append(temp)
            temp_2[spec_name] = data
            result_2.append(temp_2)

            result_3[department].append(temp_2)

            discipline_names = []
            data = []
            scale = []
            temp = {}
            temp_2 = {}

    #---------------------------------------------------------------

    res = printResult(result_3, totalResult, abiturientScores)
    # print("----------------------")
    # print(res)
    return res