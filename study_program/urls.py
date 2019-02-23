from django.urls import path, include
from django.shortcuts import redirect

from . import views




urlpatterns = [
    #path('', views.main_menu, name = 'main_menu'),

    path('main_menu', views.main_menu, name = 'main_menu'),
    path('assessment_menu', views.assessment_menu, name = 'assessment_menu'),

    path('study_program/', views.all_programs, name = 'all_program'),
    path('study_program/<int:page_number>/', views.all_programs, name = 'all_program'),
    path('study_program/?page=<int:page_number>/', views.all_programs, name = 'all_program'),
    
    path('program_detail/<int:program_id>/', views.program_detail, name='program_detail'),
    
    path('professors/', views.all_professors, name = 'all_professor'),
    path('professors/<int: page_number>', views.all_professors, name = 'all_professor'),
    path('professors_profile/<int:professor_id>/', views.professor_detail, name='professor_profile'),

    path('assessment/', views.all_assessments, name = 'all_assessment'),
    path('assessment/<int:page_number>/', views.all_assessments, name = 'all_assessment'),
    path('assessment_result/<int:assessment_id>/', views.assessment_result, name = 'assessment_result'),

    path('committee/', views.all_committees, name = 'all_committee'),
    path('committee/<int:page_number>/', views.all_committees, name = 'all_committee'),
    path('committee_profile/<int:committee_id>/', views.committee_profile, name = 'committee_profile'),
    
    
    #https://django.cowhite.com/blog/adding-and-editing-model-objects-using-django-class-based-views-and-forms/
    
    # edit form
    path('study_program/edit/<int:program_id>', views.edit_study_program, name = "edit_study_program"),
    path('professors/edit/<int:professor_id>', views.edit_professor_profile, name = "edit_professor_profile"),
    path('assessment/edit/<int:assessment_id>', views.edit_assessment_result, name = "edit_assessment_result"),
    path('committee/edit/<int:committee_id>', views.edit_committee_profile, name = "edit_committee_profile"),

    # create form
    path('study_program/create', views.create_study_program, name = "create_study_program"),

    path('professor/create', views.create_professor, name = "create_professor"),
    path('professor/study_program/create/<int:program_id>', views.create_professor_fromStudyProgram, name = "create_professor_fromStudyProgram"),

    path('committee/create', views.create_committee, name = "create_committee"),
    path('assessment_result/create', views.create_assessment_result, name = "create_assessment_result"),
    path('aun/create', views.create_aun_result, name = 'create_aun'),

    #path('edit/study_program/<int:id>', views.my_view, name="index")
    #path('', lambda _: redirect('/admin/study_program/studyprogram/'), name="index")
    #path('', lambda _: redirect('admin:index'), name="index")
]  


