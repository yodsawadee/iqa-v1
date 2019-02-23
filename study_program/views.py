from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import StudyProgram, Professor, AssessmentResult, Committee, AUN
from .forms import StudyProgramForm, ProfessorForm, AssessmentResultForm, CommitteeForm, AunForm
from django.http import HttpResponseRedirect

import math

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required(login_url="/login")
def main_menu(request):
    return render(request, 'main_page/main_menu_page.html')

@login_required(login_url="/login")
def assessment_menu(request):
    return render(request, 'main_page/assessment_menu_page.html')

@login_required(login_url='login')
def all_programs(request, page_number = 1):
    #Filters: 
    # 1 - faculties
    # 2 - degree
    # 3 - status
    # 4 - inter/thai
    # 5 - modify/new
    
    faculties_list = {'Engineering':'Engineering', 'Agriculture':'Agriculture', 'Science':'Science'}    
    faculties = ["Science", "Engineering","Medicine"]

    degree_list = {'b':'Bachelor', 'm':'Master', 'd':'Doctor'}

    # status_list = {}

    from_item = (page_number * 10) - 10
    to_item = page_number * 10

    page_number_list = [1,1,2,3,4] ##########

    sp = StudyProgram.objects # get object
    programs = sp.all() # get all objects
    total_program = sp.count() # get length of object

    program_list = []

    ########################################################################
    studyProgram_list = StudyProgram.objects.all()
    page = request.GET.get('page')
    #print(page)
    paginator = Paginator(studyProgram_list, 10)

    try:
        studyPrograms = paginator.page(page)
        print(type(studyPrograms))
    except PageNotAnInteger:
        print("KAO NOTiNT")
        studyPrograms = paginator.page(1)
    except EmptyPage:
        print("KAO EMPTY PAGE")
        studyPrograms = paginator.page(paginator.num_pages)

    # return render(request, 'study_program/all_program.html', { 'studyPrograms': studyPrograms })
    # return render(request, 'study_program/all_program.html', {
    #     'studyPrograms': studyPrograms,
    #     'faculties':faculties_list,
    #     'degrees': degree_list,
    #     'programs': program_list})
    ########################################################################


    # check searching program
    found = False
    faculty_search = request.GET.get('faculty_name')
    if(faculty_search != None):
        #print(faculty_search)
        for item in programs:
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
            'degrees': degree_list,
            'programs': program_list, 
            'current_page': current_page, 
            'prev_page': prev_page, 
            'next_page': next_page,
            'prev_two_page': prev_two_page, ##########
            'next_two_page': next_two_page, ##########
            'page_number': page_number_list}) ##########

    else:
        for item in programs:
            program_list.append(item)
        
        # get 10 items/ page
        program_list = program_list[from_item:to_item]

        # adjust page button
        prev_two_page = page_number - 2 ##########
        next_two_page = page_number + 2 ##########

        prev_page = page_number - 1
        if(page_number - 1 < 1):
            prev_page = 1 
            prev_two_page = 1 ##########

        current_page = page_number

        next_page = page_number + 1
        
        if(next_page > math.ceil(total_program/10)):
            next_page = current_page

        return render(request, 'study_program/all_program.html', {
            'studyPrograms': studyPrograms,
            'faculties':faculties_list,
            'degrees': degree_list,
            'programs': program_list, 
            'current_page': current_page, 
            'prev_page': prev_page, 
            'next_page': next_page,
            'prev_two_page': prev_two_page, ##########
            'next_two_page': next_two_page, ##########
            'page_number': page_number_list}) ##########


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


@login_required(login_url="login")
def all_professors(request, page_number=1):

    from_item = (page_number * 10) - 10
    to_item = page_number * 10

    p = Professor.objects # get object
    assessments = p.all() # get all objects
    total_assessment = p.count() # get length of object

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

   
    return render(request, 'professor/all_professor.html', {'professors': assessment_list, 'current_page': current_page, 'prev_page': prev_page, 'next_page':next_page})


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
   

    return render(request, 'professor/professor_profile.html', {'professor_profile': profile, 'responsible_program':responsible_program, 'committee_list':committee_list, 'professor_id':professor_id})


@login_required(login_url="login")
def all_assessments(request, page_number=1):
        
    from_item = (page_number * 10) - 10
    to_item = page_number * 10

    ar = AssessmentResult.objects # get object
    assessments = ar.all() # get all objects
    total_assessment = ar.count() # get length of object

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

   
    return render(request, 'assessment/all_assessment.html', {'assessments': assessment_list, 'current_page': current_page, 'prev_page': prev_page, 'next_page':next_page})


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


@login_required(login_url="login")
def all_committees(request, page_number=1):
        
    from_item = (page_number * 10) - 10
    to_item = page_number * 10

    c = Committee.objects # get object
    committees = c.all() # get all objects
    total_committee = c.count() # get length of object

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

   
    return render(request, 'committee/all_committee.html', {'committee_list': committee_list, 'current_page': current_page, 'prev_page': prev_page, 'next_page':next_page})
  

@login_required(login_url="login")
def committee_profile(request, committee_id):
    detail = get_object_or_404(Committee, pk=committee_id)

    assessment_list = []
    for assessment in detail.assessment_programs.all():
        assessment_list.append(assessment)
    
    id_kub = detail.professor_id.id
    print(id_kub)
    return render(request, 'committee/committee_detail.html', {'committee_detail': detail, 'professor_profile':id_kub, 'assessment_list': assessment_list, 'committee_id':committee_id})



#################### CREATE ####################


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
##############################################

#################### EDIT ####################

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