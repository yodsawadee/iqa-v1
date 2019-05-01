from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseRedirect, HttpResponse
import csv
from .models import StudyProgram, Professor, AssessmentResult, Committee, AUN, AvailableTime, Issue, Comment
from .forms import StudyProgramForm, ProfessorForm, AssessmentResultForm, CommitteeForm, AunForm, AvailableTimeForm, IssueForm, CommentForm



import datetime, calendar
import math

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# -------------------------------- main_menu -------------------------------- #

@login_required(login_url="/login")
def main_menu(request):
    return render(request, 'main_page/main_menu_page.html')

@login_required(login_url="/login")
def assessment_menu(request):
    return render(request, 'main_page/assessment_menu_page.html')

@login_required(login_url="/login")
def iqa_menu(request):
    return render(request, 'main_page/iqa_menu_page.html')

@login_required(login_url="/login")
def faculty_menu(request):
    return render(request, 'main_page/faculty_menu_page.html')

#@user_passes_test(lambda u: u.is_superuser, login_url='all_committee')
@login_required(login_url="login")
def committee_menu(request):
    return render(request, "main_page/committee_menu_page.html")


# --------------------------------------------------------------------------- #




# -------------------------------- iqa_menu -------------------------------- #

@login_required(login_url="/login")
def all_notification(request):
    sp = StudyProgram.objects.all()

    notify_not_enough_rp = []
    number_of_responsible_professor = 3

    for study_program in sp:
        #print(study_program.responsible_professors.count())
        if(study_program.responsible_professors.count() < number_of_responsible_professor):
            notify_not_enough_rp.append(study_program)
    
    ########################################################################
    page = request.GET.get('page')
    paginator = Paginator(notify_not_enough_rp, 10)

    try:
        notify_not_enough_rp = paginator.page(page)
    except PageNotAnInteger:
        notify_not_enough_rp = paginator.page(1)
    except EmptyPage:
        notify_not_enough_rp = paginator.page(paginator.num_pages)
    ########################################################################
    
    
    context = {'notify_not_enough_rp':notify_not_enough_rp}
    return render(request, 'iqa_menu/notice/notice.html', context)

@login_required(login_url="/login")
def committee_recommendation(request):
    return render(request, 'iqa_menu/committee_recommendation/committee_recommendation.html')


# ASSESSMENT CALENDAR
@login_required(login_url="/login")
def assessment_calendar(request, month = datetime.datetime.today().month, year = datetime.datetime.today().year):
    today = datetime.datetime.today()

    date_name = list(calendar.day_abbr)
    month_name = datetime.date(year, month, 1).strftime('%B')
    day_in_month = calendar.monthcalendar(year, month)
    print("DATEM: ", day_in_month)

    
    if(month == 12):
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
        
    
    if(month == 1):
        prev_month = 12
        prev_year = year - 1
    else:
        prev_month = month - 1
        prev_year = year
        
    # get all dates that have appointments
    available_time_list = AvailableTime.objects.all()
    #available_time = available_time_list[0]
    
    
    if(month < 10):
        string_month = "0" + str(month)
    else:
        string_month = str(month)
    
    have_appointment_in_morning_list = []
    have_appointment_in_afternoon_list = []
    for available_time in available_time_list:
        appointed_date = str(available_time.appointment_date)
        appointment_year = appointed_date[0:4]
        appointment_month = appointed_date[5:7]
        appointment_day = appointed_date[8:10]
        
        if(string_month == appointment_month and str(year) == appointment_year):
            if(available_time.available_in_morning == "yes"):
                if appointment_day not in have_appointment_in_morning_list:
                    have_appointment_in_morning_list.append(int(appointment_day))

            if(available_time.available_in_afternoon == "yes"):
                if appointment_day not in have_appointment_in_afternoon_list:
                    have_appointment_in_afternoon_list.append(int(appointment_day))
        
    
    print(have_appointment_in_morning_list)
    print(have_appointment_in_afternoon_list)
    
    conflict_list = check_appointment_conflict()  
    
    # ECHO PRINTING: check if the conflict list is correct!
    # for item in conflict_list:
    #     print(item[0].code,":",item[1],":",item[2],":",end=" [")
    #     for faculty in item[3]:
    #         print(faculty.code, end=", ")
    #     print("]")
 

    conflict_date_list = []
    for item in conflict_list:
        conflict_date = str(item[1])
        conflict_year = conflict_date[0:4]
        conflict_month = conflict_date[5:7]
        conflict_day = conflict_date[8:10]
        if(string_month == conflict_month and str(year) == conflict_year):
            if conflict_day not in conflict_date_list:
                conflict_date_list.append(int(conflict_day))

    if(len(conflict_date_list) > 0):
        is_conflict = True
    else:
        is_conflict = False

    context = {'date_name':date_name,'day_in_month':day_in_month,'month':month , 'month_name':month_name, 'next_month':next_month,'prev_month':prev_month, 
                'year':year, 'next_year':next_year,'prev_year':prev_year, 'have_appointment_in_afternoon_list':have_appointment_in_afternoon_list,
                'have_appointment_in_morning_list':have_appointment_in_morning_list, 'conflict_date_list':conflict_date_list, 'is_conflict':is_conflict }

         
    return render(request, 'iqa_menu/assessment_calendar/assessment_calendar.html', context)

@login_required(login_url="/login")
def assessment_calendar_detail(request, day = 0, month = 0, year = 0):
    if(day < 10):
        day = '0' + str(day)
    else:
        day = str(day)
    
    if(month < 10):
        month = '0' + str(month)
    else:
        month = str(month)
    
    year = str(year)

    date = year + '-' + month + '-' + day

    print("SELECTED DATE: ",date)
    #SLEEPY WA, FIX this LATER
    morning_appointment_dict = {}
    afternoon_appointment_dict = {}

    at = AvailableTime.objects.all()
    for appointment in at:
        if(str(appointment.appointment_date) == date and appointment.available_in_morning == "yes"):
            c = appointment.appointed_committee.all()
            morning_appointment_dict.update({appointment:c})
    
    for appointment in at:  
        if(str(appointment.appointment_date) == date and appointment.available_in_afternoon == "yes"):
            c = appointment.appointed_committee.all()
            afternoon_appointment_dict.update({appointment:c})
          
    #print("OBJECT TIME: ",str(at[0].appointment_date))
    context = { 'date': date,'morning_appointment_dict':morning_appointment_dict, 'afternoon_appointment_dict':afternoon_appointment_dict}
    return render(request,  'iqa_menu/assessment_calendar/assessment_calendar_detail.html', context)

def check_appointment_conflict():
    #print("check appointment conflict")

    at = AvailableTime.objects.all()
    conflict_list = []
    for appointment in at:
        for c_appointment in at:
            if(appointment.appointment_date == c_appointment.appointment_date): # check if it is different date
                if(appointment.appointed_program != c_appointment.appointed_program): # confirm that it is different program
                    if(appointment.available_in_morning == c_appointment.available_in_morning and appointment.available_in_morning == "yes"): # case of morning assessment
                        # check if same professor
                        committees_a = appointment.appointed_committee
                        committees_a = committees_a.all()
                        
                        committees_b = c_appointment.appointed_committee
                        committees_b = committees_b.all()

                        result = check_committee_conflict(committees_a, committees_b)
                        for committee in result:
                            conflict_list.append([committee,appointment.appointment_date, appointment.appointed_program, "morning"])
                            conflict_list.append([committee,appointment.appointment_date, c_appointment.appointed_program, "morning"])

                    if(appointment.available_in_afternoon == c_appointment.available_in_afternoon and appointment.available_in_afternoon == "yes"):
                        # check if same professor
                        committees_a = appointment.appointed_committee
                        committees_a = committees_a.all()
                        
                        committees_b = c_appointment.appointed_committee
                        committees_b = committees_b.all()

                        result = check_committee_conflict(committees_a, committees_b)
                        for committee in result:
                            conflict_list.append([committee,appointment.appointment_date, appointment.appointed_program, "afternoon"])
                            conflict_list.append([committee,appointment.appointment_date, c_appointment.appointed_program, "afternoon"])
    
    conflict_list = eliminate_same_item(conflict_list)
    conflict_list = conflict_grouping(conflict_list)
    
    return conflict_list

def check_committee_conflict(committee_list_a, committee_list_b):
    #print("check professor conflict")
    conflict_list = []
    for committee in committee_list_a:
        if committee in committee_list_b:
            if committee not in conflict_list:
                conflict_list.append(committee)
    
    return conflict_list

def eliminate_same_item(conflict_list):
    new_conflict_list = [] # no redundant
    for item in conflict_list:
        #print(item[0].code,":",item[1],":",item[2].code,":",item[3])
        not_in = True
        for i in range(len(new_conflict_list)):
            if(item[0].code == new_conflict_list[i][0].code and
               item[1] == new_conflict_list[i][1] and
               item[2].code == new_conflict_list[i][2].code and
               item[3] == new_conflict_list[i][3]):
               not_in = False
               break

        if(not_in == True):
            new_conflict_list.append(item)

    return new_conflict_list

def conflict_grouping(conflict_list):
    new_conflict_list = []

    grouping_list = []
    for i in range(len(conflict_list)):
        group = []
        for j in range(len(conflict_list)):
            if(conflict_list[i][0].code == conflict_list[j][0].code and
               conflict_list[i][1] == conflict_list[j][1] and
               conflict_list[i][3] == conflict_list[j][3] and
               (conflict_list[j][2] not in group)):
               group.append(conflict_list[j][2])
        
        grouping_list.append([conflict_list[i][0],conflict_list[i][1],conflict_list[i][3], group])
    
    #return grouping_list
    for group in grouping_list:
        not_in = True
        for i in range(len(new_conflict_list)):
            if(new_conflict_list[i][0] == group[0] and
               new_conflict_list[i][1] == group[1] and
               new_conflict_list[i][2] == group[2]):
               not_in = False
               break

        if(not_in == True):
            new_conflict_list.append(group)

    return new_conflict_list



@login_required(login_url="/login")
def view_conflict_detail(request):
    conflict_date_list = check_appointment_conflict()

    conflict_date_dict = {}
    for item in conflict_date_list:
        # FORMAT STRING
        key = str(item[0].professor_id.name_surname) + " " + (str(item[1])) + " " + item[2]
        conflict_date_dict.update({key:item[3]})

    context = {'conflict_date_dict':conflict_date_dict }
    return render(request, 'iqa_menu/assessment_calendar/appointment_conflict.html', context)

# --------------------------------------------------------------------------- #



# -------------------------------- faculty_menu -------------------------------- #

@login_required(login_url="/login")
def all_faculty_program(request, page_number = 1):
    #Filters: 
    # 1 - faculties
    # 2 - degree
    # 3 - status
    # 4 - inter/thai
    # 5 - modify/new
    
    faculties_list = {
        'AAI':'วิทยาลัยอุตสาหกรรมการบินนานาชาติ', 
        'ADM':'คณะบริหารและจัดการ', 
        'AGI':'คณะอุตสาหกรรมเกษตร', 
        'AMI':'คณะเทคโนโลยีการเกษตร', 
        'ARC':'วิทยาลัยนวัตกรรมการผลิตขั้นสูง', 
        'CHP':'คณะสถาปัตยกรรมศาสตร์', 
        'EIR':'วิทยาเขตชุมพรเขตรอุดมศักดิ์', 
        'ENG':'คณะวิศวกรรมศาสตร์', 
        'ICX':'วิทยาลัยนานาขาติ', 
        'IDE':'คณะครุศาสตร์อุตสาหกรรมและเทคโนโลยี', 
        'ITX':'คณะเทคโนโลยีสารสนเทศ', 
        'LBA':'คณะศิลปศาสตร์', 
        'MED':'วิทยาลัยแพทยศาสตร์นานาชาติ', 
        'MSE':'วิทยาลัยสังคีต', 
        'NNT':'วิทยาลัยนาโนเทคโนโลยี', 
        'SCI':'คณะวิทยาศาสตร์', 
        }    

    degree_list = {
        'B':'ปริญญาตรี',
        'M':'ปริญญาโท',
        'D':'ปริญญาเอก',
    }

    study_program_list = StudyProgram.objects.all()

    # Get all program relating to that faculty
    temp_list = []
    for program in study_program_list:
        # !!!
        if(str(request.user.username).upper() == program.code[0:3]):
            temp_list.append(program)
    
    study_program_list = temp_list

    # PAGINATOR THINGSY
    page = request.GET.get('page')
    paginator = Paginator(study_program_list, 10)

    try:
        studyPrograms = paginator.page(page)
        print(type(studyPrograms))
    except PageNotAnInteger:
        print("Paginator: PageNotAnIntegerException")
        studyPrograms = paginator.page(1)
    except EmptyPage:
        print("Paginator: EmptyPageException")
        studyPrograms = paginator.page(paginator.num_pages)


    prev_page = page_number - 1
    if(page_number - 1 < 1):
        prev_page = 1 

    current_page = page_number

    next_page = page_number + 1
    
    total_program = StudyProgram.objects.count()
    #print(total_program)
    if(next_page > math.ceil(total_program/10)):
        next_page = current_page

    context = {'studyPrograms':studyPrograms, 'faculties_list':faculties_list, 'degree_list':degree_list,
               'next_page':next_page, 'current_page':current_page, 'prev_page':prev_page }


    return render(request, 'faculty_menu/faculty_study_program/all_faculty_study_program.html', context)


def faculty_program_detail(request, program_id):
    detail = get_object_or_404(StudyProgram, pk=program_id)

    professor_list = []
    for professor in detail.responsible_professors.all():
        professor_list.append(professor)

    assessment_list =[]
    assessments = AssessmentResult.objects
    for assessment in assessments.all():
        #print("asssessment",assessment.program_id)
        #print("name",detail.name)
        if(str(assessment.program_id) == detail.name):
            #print("KAO")
            assessment_list.append(assessment)

    context = {
        'program_detail': detail, 
        'professors':professor_list, 
        'assessment_list':assessment_list, 
        'program_id': program_id
        }

    return render(request, 'faculty_menu/faculty_study_program/faculty_program_detail.html', context )

#@login_required(login_url="/login")
#def committee_appointment(request):
#    return render(request, 'faculty_menu/committee_appointment/committee_appointment.html')


# --------------------------------------------------------------------------- #





# ---------------------------------------------- listItem & detail --------------------------------------------- #


# ALL PROGRAMS
@login_required(login_url='login')
def all_programs(request, page_number = 1, faculty = "-"):
    #Filters: 
    # 1 - faculties
    # 2 - degree
    # 3 - status
    # 4 - inter/thai
    # 5 - modify/new
    
    faculties_list = {
        'AAI':'วิทยาลัยอุตสาหกรรมการบินนานาชาติ', 
        'ADM':'คณะบริหารและจัดการ', 
        'AGI':'คณะอุตสาหกรรมเกษตร', 
        'AMI':'คณะเทคโนโลยีการเกษตร', 
        'ARC':'วิทยาลัยนวัตกรรมการผลิตขั้นสูง', 
        'CHP':'คณะสถาปัตยกรรมศาสตร์', 
        'EIR':'วิทยาเขตชุมพรเขตรอุดมศักดิ์', 
        'ENG':'คณะวิศวกรรมศาสตร์', 
        'ICX':'วิทยาลัยนานาขาติ', 
        'IDE':'คณะครุศาสตร์อุตสาหกรรมและเทคโนโลยี', 
        'ITX':'คณะเทคโนโลยีสารสนเทศ', 
        'LBA':'คณะศิลปศาสตร์', 
        'MED':'วิทยาลัยแพทยศาสตร์นานาชาติ', 
        'MSE':'วิทยาลัยสังคีต', 
        'NNT':'วิทยาลัยนาโนเทคโนโลยี', 
        'SCI':'คณะวิทยาศาสตร์', 
        }    

    degree_list = {
        'B':'ปริญญาตรี',
        'M':'ปริญญาโท',
        'D':'ปริญญาเอก',
    }
    # degree_list = {'b':'Bachelor', 'm':'Master', 'd':'Doctor'}

    # # status_list = {}

    from_item = (page_number * 10) - 10
    to_item = page_number * 10

    # page_number_list = [1,1,2,3,4] ##########

 

    ########################################################################
    studyProgram_list = StudyProgram.objects.all()
    page = request.GET.get('page')
    
    # filtering faculties
    if(faculty != "-"):
        faculty = faculty[0:3]
        faculty = faculty.upper()
    
        temp_study_list = []
        for item in studyProgram_list:
            if(item.code[0:3] == faculty):
                temp_study_list.append(item)
        
        studyProgram_list = temp_study_list
    # done

    # filtering degree
    degree = "-"
    if(degree != "-"):
        temp_study_list = []
        for item in studyProgram_list:
            if(item.code[10] == degree):
                temp_study_list.append(item) 
        studyProgram_list = temp_study_list
    # done

    paginator = Paginator(studyProgram_list, 10)

    try:
        studyPrograms = paginator.page(page)
    except PageNotAnInteger:
        studyPrograms = paginator.page(1)
    except EmptyPage:
        studyPrograms = paginator.page(paginator.num_pages)

    # return render(request, 'study_program/all_program.html', { 'studyPrograms': studyPrograms })
    ########################################################################

    program_list = []
    
    # check searching program
    found = False
    faculty_search = request.GET.get('faculty_name')
    if(faculty_search != None):
        #print(faculty_search)
        for item in StudyProgram.objects.all():
            #print(item.name)
            if(item.name == faculty_search):
                found = True
                program_list.append(item)
                #search_list = item

    if(found == True):
        prev_page = 1
        current_page = 1
        next_page = 1
        prev_two_page = 1
        next_two_page = 1

        return render(request, 'study_program/all_program.html', {
            'studyPrograms': studyPrograms,
            'faculties':faculties_list,
            'degree': degree_list,
            # 'programs': program_list, 
            'current_page': current_page, 
            'prev_page': prev_page, 
            'next_page': next_page
            }) 

    else:
        for item in StudyProgram.objects.all():
            program_list.append(item)
        
        # get 10 items/ page
        program_list = program_list[from_item:to_item]

        # adjust page button
        prev_page = page_number - 1
        if(page_number - 1 < 1):
            prev_page = 1 

        current_page = page_number

        next_page = page_number + 1
        
        total_program= StudyProgram.objects.count()
        print(total_program)
        if(next_page > math.ceil(total_program/10)):
            next_page = current_page

        
        return render(request, 'study_program/all_program.html', {
            'studyPrograms': studyPrograms,
            'faculties':faculties_list,
            'degree': degree_list,
            # 'programs': program_list, 
            'current_page': current_page, 
            'prev_page': prev_page, 
            'next_page': next_page
            })


# PROGRAM DETAIL
@login_required(login_url="login")
def program_detail(request, program_id):
    detail = get_object_or_404(StudyProgram, pk=program_id)

    professor_list = []
    for professor in detail.responsible_professors.all():
        professor_list.append(professor)

    assessment_list =[]
    assessments = AssessmentResult.objects
    for assessment in assessments.all():
        #print("asssessment",assessment.program_id)
        #print("name",detail.name)
        if(str(assessment.program_id) == detail.name):
            #print("KAO")
            assessment_list.append(assessment)

    return render(request, 'study_program/program_detail.html', {
        'program_detail': detail, 
        'professors':professor_list, 
        'assessment_list':assessment_list, 
        'program_id': program_id})


# ALL PROFESSOR
@login_required(login_url="login")
def all_professors(request, page_number=1):

    from_item = (page_number * 10) - 10
    to_item = page_number * 10

    p = Professor.objects # get object
    assessments = p.all() # get all objects
    total_assessment = p.count() # get length of object

    ########################################################################
    professor_list = Professor.objects.all()
    page = request.GET.get('page')
    #print(page)
    paginator = Paginator(professor_list, 10)

    try:
        professors = paginator.page(page)
    except PageNotAnInteger:
        professors = paginator.page(1)
    except EmptyPage:
        professors = paginator.page(paginator.num_pages)

    # return render(request, 'study_program/all_program.html', { 'professors': professors })
    ########################################################################
    
    assessment_list = []

    for assessment in assessments:
        assessment_list.append(assessment)
    
    # get 10 items/ page
    assessment_list = assessment_list[from_item:to_item]

    # adjust page button
    prev_page = page_number - 1
    if(page_number - 1 < 1):
        prev_page = 1  

    current_page = page_number

    next_page = page_number + 1
    if(next_page > math.ceil(total_assessment/10)):
        next_page = current_page

    return render(request, 'professor/all_professor.html', {
        'professors': professors,
        # 'professors': assessment_list, 
        'current_page': current_page, 
        'prev_page': prev_page, 
        'next_page':next_page
        })


# PROFESSOR DETAIL
@login_required(login_url="login")
def professor_detail(request, professor_id):
    profile = get_object_or_404(Professor, pk=professor_id)

    responsible_program = []
    for program in profile.responsible_program.all():
        responsible_program.append(program)

    committee_list = []
    c = Committee.objects
    committees = c.all()
    for committee in committees:
        #print("c:",committee.professor_id)
        #print("p:", profile.name_surname)
        if(str(committee.professor_id) == profile.name_surname):
            #print("KAO IF")
            committee_list.append(committee)
    '''
    for comittee_per_year in profile.committee_profile.all():
        committee_list.append(comittee_per_year)
    '''
   
    return render(request, 'professor/professor_profile.html', {
        'professor_profile': profile, 
        'responsible_program':responsible_program, 
        'committee_list':committee_list, 
        'professor_id':professor_id})


# ALL ASSESSMENTS
@login_required(login_url="login")
def all_assessments(request, page_number=1):
        
    from_item = (page_number * 10) - 10
    to_item = page_number * 10

    ar = AssessmentResult.objects # get object
    assessments = ar.all() # get all objects
    total_assessment = ar.count() # get length of object

    ########################################################################
    assessment_list = AssessmentResult.objects.all()
    page = request.GET.get('page')
    #print(page)
    paginator = Paginator(assessment_list, 10)

    try:
        assessments = paginator.page(page)
    except PageNotAnInteger:
        assessments = paginator.page(1)
    except EmptyPage:
        assessments = paginator.page(paginator.num_pages)

    # return render(request, 'study_program/all_program.html', { 'assessments': assessments })
    ########################################################################
    
    assessment_list = []

    for assessment in assessments:
        assessment_list.append(assessment)
    
    # get 10 items/ page
    assessment_list = assessment_list[from_item:to_item]

    # adjust page button
    prev_page = page_number - 1
    if(page_number - 1 < 1):
        prev_page = 1  

    current_page = page_number

    next_page = page_number + 1
    if(next_page > math.ceil(total_assessment/10)):
        next_page = current_page

   
    return render(request, 'assessment/all_assessment.html', {
        'assessments': assessments,
        # 'assessments': assessment_list, 
        'current_page': current_page, 
        'prev_page': prev_page, 
        'next_page':next_page})


# ASSESSMENT RESULT
@login_required(login_url="login")
def assessment_result(request, assessment_id):
    detail = get_object_or_404(AssessmentResult, pk=assessment_id)

    commitee_list = []
    for committee in detail.committee_id.all():
        commitee_list.append(committee)

    #assessment_result.aun_id
    #print("AEE")
    aun_result = get_object_or_404(AUN, assessment_id=assessment_id)
    #print(aun_result)
    return render(request, 'assessment/assessment_result.html', {'assessment_result': detail, 'commitee_list':commitee_list, 'assessment_id': assessment_id,'aun_result':aun_result})


# ALL COMMITTEES
@login_required(login_url="login")
def all_committees(request, page_number=1):
        
    from_item = (page_number * 10) - 10
    to_item = page_number * 10

    c = Committee.objects # get object
    committees = c.all() # get all objects
    total_committee = c.count() # get length of object

    ########################################################################
    committee_list = Committee.objects.all()
    page = request.GET.get('page')
    #print(page)
    paginator = Paginator(committee_list, 10)

    try:
        committees = paginator.page(page)
    except PageNotAnInteger:
        committees = paginator.page(1)
    except EmptyPage:
        committees = paginator.page(paginator.num_pages)

    # return render(request, 'study_program/all_program.html', { 'committees': committees })
    ########################################################################

    committee_list = []

    for committee in committees:
        committee_list.append(committee)
    
    # get 10 items/ page
    committee_list = committee_list[from_item:to_item]

    # adjust page button
    prev_page = page_number - 1
    if(page_number - 1 < 1):
        prev_page = 1  

    current_page = page_number

    next_page = page_number + 1
    if(next_page > math.ceil(total_committee/10)):
        next_page = current_page

   
    return render(request, 'committee/all_committee.html', {
        'committees': committees,
        'committee_list': committee_list, 
        'current_page': current_page, 
        'prev_page': prev_page, 
        'next_page':next_page})
  

# COMMITTEE PROFILE
@login_required(login_url="login")
def committee_profile(request, committee_id):
    detail = get_object_or_404(Committee, pk=committee_id)

    assessment_list = []
    for assessment in detail.assessment_programs.all():
        assessment_list.append(assessment)
    
    id_kub = detail.professor_id.id
    print(id_kub)
    return render(request, 'committee/committee_detail.html', {'committee_detail': detail, 'professor_profile':id_kub, 'assessment_list': assessment_list, 'committee_id':committee_id})

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




#---------------------------------------- CREATE -------------------------------------------------------------------------------------------------------------------------------------------#


# create study program
@user_passes_test(lambda u: u.is_superuser, login_url='all_program')
@login_required(login_url="login")
def create_study_program(request):
    form = StudyProgramForm(request.POST or None, files = request.FILES or None)
    if form.is_valid():
        #print("kao if")
        form.save()
        #print("save leaw")
        form = StudyProgramForm()
        return redirect('all_program')

    context = { 'form': form }
    return render(request, "study_program/create_study_program.html", context)


# create professor
@user_passes_test(lambda u: u.is_superuser, login_url='all_program')
@login_required(login_url="login")
def create_professor(request):
    form = ProfessorForm(request.POST or None, files = request.FILES or None)
    if form.is_valid():
        form.save()
        form = ProfessorForm()
        return redirect('all_professor')

    context = { 'form': form }
    return render(request, "professor/create_professor.html", context)


@user_passes_test(lambda u: u.is_superuser, login_url='all_program')
@login_required(login_url="login")
def create_professor_fromStudyProgram(request, program_id):
    form = ProfessorForm(request.POST or None, files = request.FILES or None)
    if form.is_valid():
        form.save()
        form = ProfessorForm()
        return redirect('program_detail', program_id = program_id)

    context = { 'form': form }
    return render(request, "professor/create_professor.html", context)


# create committee
@user_passes_test(lambda u: u.is_superuser, login_url='all_committee')
@login_required(login_url="login")
def create_committee(request):
    form = CommitteeForm(request.POST or None, files = request.FILES or None)
    if form.is_valid():
        form.save()
        form = CommitteeForm()
        return redirect('all_committee')

    context = { 'form': form }
    return render(request, "committee/create_committee.html", context)


# create assessment result
@user_passes_test(lambda u: u.is_superuser, login_url='all_assessment')
@login_required(login_url="login")
def create_assessment_result(request):
    form = AssessmentResultForm(request.POST or None, files = request.FILES or None)
    if form.is_valid():
        form.save()
        form = AssessmentResultForm()
        return redirect('create_aun')

    context = { 'form': form }
    return render(request, "assessment/create_assessment_result.html", context)

# create AUN result
@user_passes_test(lambda u: u.is_superuser, login_url='all_assessment')
@login_required(login_url="login")
def create_aun_result(request):
    form = AunForm(request.POST or None, files = request.FILES or None)
    if form.is_valid():
        form.save()
        form = AunForm()
        return redirect('all_assessment')

    context = { 'form': form }
    return render(request, "assessment/create_aun.html", context)

#-----------------------------------------------------------------------------------------------#



#---------------------------------------- EDIT --------------------------------------------------#

@user_passes_test(lambda u: u.is_superuser, login_url='all_program')
@login_required(login_url="login")
def edit_study_program(request, program_id):
    study_program = get_object_or_404(StudyProgram, pk=program_id)
    if request.method == "POST":
        #form = StudyProgramForm(request.POST, request.FILES, instance=study_program)
        form = StudyProgramForm(data = request.POST, files = request.FILES, instance=study_program)
        if form.is_valid():
            form.save()
            #ini_obj = form.save(commit=False)
            #ini_obj.save()
            return redirect('program_detail', program_id = program_id)

    else:
        form = StudyProgramForm(instance=study_program)

    context = {
        'form':form
    }
    return render(request, "study_program/edit_study_program.html", context)


@user_passes_test(lambda u: u.is_superuser, login_url='all_program')
@login_required(login_url="login")
def edit_professor_profile(request, professor_id):
    professor = get_object_or_404(Professor, pk=professor_id)
    if request.method == "POST":
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('professor_profile', professor_id = professor_id)

    else:
        form = ProfessorForm(instance=professor)

    context = {
        'form':form
    }
    return render(request, "professor/edit_professor_profile.html", context)


@user_passes_test(lambda u: u.is_superuser, login_url='all_assessment')
@login_required(login_url="login")
def edit_assessment_result(request, assessment_id):
    assessment = get_object_or_404(AssessmentResult, pk=assessment_id)
    if request.method == "POST":
        form = AssessmentResultForm(request.POST, instance=assessment)
        if form.is_valid():
            form.save()
            return redirect('assessment_result', assessment_id = assessment_id)

    else:
        form = AssessmentResultForm(instance=assessment)

    context = {
        'form':form
    }
    return render(request, "assessment/edit_assessment_result.html", context)


@user_passes_test(lambda u: u.is_superuser, login_url='all_committee')
@login_required(login_url="login")
def edit_committee_profile(request, committee_id):
    committee = get_object_or_404(Committee, pk=committee_id)
    if request.method == "POST":
        form = CommitteeForm(request.POST, instance=committee)
        if form.is_valid():
            form.save()
            return redirect('committee_profile', committee_id = committee_id)

    else:
        form = CommitteeForm(instance=committee)

    context = {
        'form':form
    }
    return render(request, "committee/edit_committee_profile.html", context)

#-----------------------------------------------------------------------------------------------------#



#------------------------------- Committeee Appointment ----------------------------------------------#

#@user_passes_test(lambda u: u.is_superuser, login_url='all_committee')
@login_required(login_url="login")
def committee_appointment(request):

    at = AvailableTime.objects # get object
    atObject = at.all() # get all objects
    total_AvailableTime = at.count() # get length of object

    available_list = []

    for available_time in atObject:
        print(available_time.user)
        if(available_time.user == request.user.username):
            available_list.append(available_time)
    
    print("AVAILABLE TIME:",available_list)
    page = request.GET.get('page')
    #print(page)
    paginator = Paginator(available_list, 10)

    try:
        available_time_for_user = paginator.page(page)
        print(type(available_time_for_user))
    except PageNotAnInteger:
        print("KAO NOTiNT")
        available_time_for_user = paginator.page(1)
    except EmptyPage:
        print("KAO EMPTY PAGE")
        available_time_for_user = paginator.page(paginator.num_pages)

    context = {'available_time_for_user': available_time_for_user }
    return render(request, 'faculty_menu/committee_appointment/committee_appointment.html', context)



#@user_passes_test(lambda u: u.is_superuser, login_url='all_committee')
@login_required(login_url="login")
def create_committee_appointment(request):
    if request.user.is_authenticated:
        user = request.user.username


    form = AvailableTimeForm(request.POST or None, files = request.FILES or None)
    print(form['user'].data)
    print(form['appointment_date'].data)

    
    if form.is_valid():
        print("FORM IS VALID")
        try:
            # no date, user, and program are the same
            ae = AvailableTime.objects.get(appointment_date=form['appointment_date'].data, user=form['user'].data, appointed_program=form['appointed_program'].data)
            print("--- get ---")
            print(ae.appointment_date)
            print(ae.user)
            #print(ae.appointed_program)
            print("-----------")
            if(str(ae.appointment_date) != str(form['appointment_date'].data)):
                print("create new object: date is not the same")
                form.save()
                form = AvailableTimeForm()
                return redirect('committee_appointment')
                
        except AvailableTime.DoesNotExist:
            print("create new object: totally new object")
            form.save()
            form = AvailableTimeForm()
            return redirect('committee_appointment')
        
        except AvailableTime.MultipleObjectsReturned:
            print("already exist!!!")
            return redirect('committee_appointment')
        else:
            # check if this case really in???
            print("kao HMMM!?!?!")
            return redirect('committee_appointment')
    else:
        print("form INVALID")
    
    form = AvailableTimeForm(initial={'appointment_date':str(datetime.datetime.now())[0:10],'user':user})
    context = {'form': form }
    print("EWWW")

    return render(request, 'faculty_menu/committee_appointment/create_appointment_time.html', context)


#@user_passes_test(lambda u: u.is_superuser, login_url='all_committee')

@login_required(login_url="login")
def edit_committee_appointment(request, available_time_id):
    available_time = get_object_or_404(AvailableTime, pk=available_time_id)
    print(available_time)
    if request.method == "POST":
        form = AvailableTimeForm(request.POST, instance=available_time)
        if form.is_valid():
            form.save()
            return redirect('committee_appointment')

    else:
        form = AvailableTimeForm(instance=available_time)

    context = {
        'form':form
    }
    return render(request, 'faculty_menu/committee_appointment/edit_appointment_time.html', context)


#------------------------------------------------------------------------------------------------------------#
def export_studyprogram_csv(request):
    response = HttpResponse(content_type='text/xlsx')
    response['Content-Disposition'] = 'attachment; filename="studyprogram.csv"'
    response.write(u'\ufeff'.encode('utf8'))

    writer = csv.writer(response)
    writer.writerow(['Program', 'Program Status', 'Degree & Major', 'Program Collaborations with Other Insitues', 'docs'])
    
    studyPrograms = StudyProgram.objects.all().values_list('name', 'program_status', 'degree_and_major', 'collaboration_with_other_institues', 'pdf_docs')
    for studyProgram in studyPrograms:
        writer.writerow(studyProgram)

    return response

    # response = HttpResponse(content_type='text/xlsx')
    # response['Content-Disposition'] = 'attachment; filename="records.xlsx"'
    # response.write(u'\ufeff'.encode('utf8'))
    # writer = csv.writer(response) 
    # writer.writerow([''])          
    # writer.writerow(['บริษัท สยาม รีเทล ดีเวลล็อปเม้นท์ จำกัด'])
    # show_date = "รายงานสรุปการเก็บเงินประจำวัน ตั้งแต่วันที่ "+str(date_start)+" ถึง "+str(date_end)
    # writer.writerow([show_date])
    # writer.writerow([''])
    # writer.writerow(['Lease Number','Shop Name','Customer Name',
    # 'วันที่เริ่มต้นสัญญา','วันที่สิ้นสุดสัญญา','ประเภทของสัญญา',
    # 'ยอดรวมทั้งสิ้น','ยอดจดยอด','เก็บเงินสด','EDC ศูนย์ฯ','EDC ร้านค้า','Voucher','Remark'])
    # writer.writerow([''])


def export_professor_csv(request):
    response = HttpResponse(content_type='text/xlsx')
    response['Content-Disposition'] = 'attachment; filename="professor.csv"'
    response.write(u'\ufeff'.encode('utf8'))

    writer = csv.writer(response)
    writer.writerow(['academic_title', 'name_surname', 'date_of_birth', \
        'bsc', 'bsc_grad_institute', 'bsc_year', 'msc', 'msc_grad_institute', 'msc_year', 'phd', 'phd_grad_institute', 'phd_year', \
            'phone', 'email', 'university', 'additional_degree'])
    
    professors = Professor.objects.all().values_list('academic_title', 'name_surname', 'date_of_birth', \
        'bsc', 'bsc_grad_institute', 'bsc_year', 'msc', 'msc_grad_institute', 'msc_year', 'phd', 'phd_grad_institute', 'phd_year', \
            'phone', 'email', 'university', 'additional_degree')
    for professor in professors:
        writer.writerow(professor)

    return response


def export_assessment_csv(request):
    response = HttpResponse(content_type='text/xlsx')
    response['Content-Disposition'] = 'attachment; filename="assessments.csv"'
    response.write(u'\ufeff'.encode('utf8'))

    writer = csv.writer(response)
    writer.writerow(['committee_id', 'program_id', 'year', 'curriculum_status', 'curriculum_status_year', 'curriculum_standard', 'pdf_docs'])
    
    assessmentss = AssessmentResult.objects.all().values_list('committee_id', 'program_id', 'year', 'curriculum_status', 'curriculum_status_year', 'curriculum_standard', 'pdf_docs')
    for assessments in assessmentss:
        writer.writerow(assessments)

    return response

    
def export_committee_csv(request):
    response = HttpResponse(content_type='text/xlsx')
    response['Content-Disposition'] = 'attachment; filename="committee.csv"'
    response.write(u'\ufeff'.encode('utf8'))

    writer = csv.writer(response)
    writer.writerow(['professor_id', 'year', 'assessment_level', 'profession', 'assessment_programs'])
    
    committees = Committee.objects.all().values_list('professor_id', 'year', 'assessment_level', 'profession', 'assessment_programs')
    for committee in committees:
        writer.writerow(committee)

    return response





#--------------------------------------------- Inbox System ------------------------------------------------#

def inbox(request):
    if(request.user.is_authenticated):
        user = request.user.username
    
    if(user == 'admin'): ### AUTHENTICATION ###
        user = 'admin'
    
    iss = Issue.objects.all()

    issue_list = []

    for item in iss:
        issue_list.append(item)
    
    ########################################################################
    page = request.GET.get('page')
    paginator = Paginator(issue_list, 10)

    try:
        issue_list = paginator.page(page)
    except PageNotAnInteger:
        issue_list = paginator.page(1)
    except EmptyPage:
        issue_list = paginator.page(paginator.num_pages)
    ########################################################################

    context = {'issue_list':issue_list, 'user':user }
    return render(request, 'inbox/inbox_main_page.html', context)


def issue_detail(request, issue_id):
    if(request.user.is_authenticated):
        user = request.user.username

    detail = get_object_or_404(Issue, pk=issue_id)

    comment_list = []
    #print(detail.id)
    for comment in Comment.objects.all():
        if(comment.comment_for == str(detail.id)):
            comment_list.append(comment)

    context = {'detail':detail, 'comments':comment_list, 'issue_id':issue_id, 'user':user}
    return render(request, 'inbox/issue_detail.html',context)

def create_issue(request):
    if(request.user.is_authenticated):
        user = request.user.username

    form = IssueForm(request.POST or None, files = request.FILES or None)
    if form.is_valid():
        form.save()
        form = IssueForm()
        return redirect('inbox')
    
    form = IssueForm(initial={'sender':user, 'receiver':'admin'})
    context = { 'form': form }
    return render(request, "inbox/create_issue.html", context)


def create_comment(request, issue_id):
    if(request.user.is_authenticated):
        user = request.user.username

    form = CommentForm(request.POST or None, files = request.FILES or None)
    if form.is_valid():
        form.save()
        form = CommentForm()
        return redirect('issue_detail', issue_id=issue_id)
    
    issue = get_object_or_404(Issue, pk=issue_id)
    form = CommentForm(initial={'comment_for':str(issue.id), 'sender':user})

    context = {'form': form, 'issue':issue}
    return render(request, "inbox/create_comment.html", context)


def edit_issue(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    #print(issue)
    if request.method == "POST":
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('inbox')

    else:
        form = IssueForm(instance=issue)

    context = {
        'form':form
    }
    return render(request, 'inbox/edit_issue.html', context)


def edit_comment(request, issue_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    #print(issue)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('issue_detail', issue_id=issue_id)

    else:
        form = CommentForm(instance=comment)

    context = {'form':form}
    return render(request, 'inbox/edit_comment.html', context)

#-------------------------------------------------------------------------------------------------------------#

