from django.urls import path, include
from django.shortcuts import redirect

from . import views




urlpatterns = [
    #path('', views.main_menu, name = 'main_menu'),

    path('main_menu', views.main_menu, name = 'main_menu'),
    path('assessment_menu', views.assessment_menu, name = 'assessment_menu'),
    path('iqa_menu', views.iqa_menu, name = 'iqa_menu'),
    path('faculty_menu', views.faculty_menu, name = 'faculty_menu'),

    path('study_program/', views.all_programs, name = 'all_program'),
    path('study_program/<str:faculty>', views.all_programs, name = 'all_program'),
    path('study_program/<int:page_number>/', views.all_programs, name = 'all_program'),
    path('study_program/?page=<int:page_number>/', views.all_programs, name = 'all_program'),

    path('study_program/export/csv', views.export_studyprogram_csv, name = 'export_studyprogram_csv'),
    
    path('program_detail/<int:program_id>/', views.program_detail, name='program_detail'),
    
    path('professors/', views.all_professors, name = 'all_professor'),
    path('professors/<int:page_number>', views.all_professors, name = 'all_professor'),
    path('professors/?page=<int:page_number>/', views.all_professors, name = 'all_professor'),
    path('professors_profile/<int:professor_id>/', views.professor_detail, name='professor_profile'),

    path('professors/export/csv', views.export_professor_csv, name = 'export_professor_csv'),

    path('assessment/', views.all_assessments, name = 'all_assessment'),
    path('assessment/<int:page_number>/', views.all_assessments, name = 'all_assessment'),
    path('assessment/?page=<int:page_number>/', views.all_assessments, name = 'all_assessment'),
    path('assessment_result/<int:assessment_id>/', views.assessment_result, name = 'assessment_result'),

    path('assessment/export/csv', views.export_assessment_csv, name = 'export_assessment_csv'),

    path('committee/', views.all_committees, name = 'all_committee'),
    path('committee/<int:page_number>/', views.all_committees, name = 'all_committee'),
    path('committee/?page=<int:page_number>/', views.all_committees, name = 'all_committee'),
    path('committee_profile/<int:committee_id>/', views.committee_profile, name = 'committee_profile'),

    path('committee/export/csv', views.export_committee_csv, name = 'export_committee_csv'),
    
    # committee menu
    path('committee_menu/', views.committee_menu, name = 'committee_menu'),

    #https://django.cowhite.com/blog/adding-and-editing-model-objects-using-django-class-based-views-and-forms/
    
    # edit form
    path('study_program/edit/<int:program_id>', views.edit_study_program, name = "edit_study_program"),
    path('professors/edit/<int:professor_id>', views.edit_professor_profile, name = "edit_professor_profile"),
    path('assessment/edit/<int:assessment_id>', views.edit_assessment_result, name = "edit_assessment_result"),
    path('committee/edit/<int:committee_id>', views.edit_committee_profile, name = "edit_committee_profile"),
    path('faculty/committee_appointment/edit_date_time/<int:available_time_id>', views.edit_committee_appointment, name = 'edit_committee_appointment'),
      

    # create form
    path('study_program/create', views.create_study_program, name = "create_study_program"),

    path('professor/create', views.create_professor, name = "create_professor"),
    path('professor/study_program/create/<int:program_id>', views.create_professor_fromStudyProgram, name = "create_professor_fromStudyProgram"),

    path('committee/create', views.create_committee, name = "create_committee"),
    path('assessment_result/create', views.create_assessment_result, name = "create_assessment_result"),
    path('aun/create', views.create_aun_result, name = 'create_aun'),

    path('faculty_menu/committee_appointment/create/', views.create_committee_appointment, name = 'create_committee_appointment'),

    # IQA Menu
    path('iqa_menu/notice', views.all_notification, name = 'all_notificaiton'),
    path('iqa_menu/committee_recommendation', views.committee_recommendation, name = 'committee_recommendation'),

    # Assessment Calendar
    path('assessment_calendar/', views.assessment_calendar, name = 'assessment_calendar'),
    path('assessment_calendar/<int:month>/<int:year>', views.assessment_calendar, name = 'assessment_calendar'),
    path('assessment_calendar/detail/', views.assessment_calendar_detail, name = 'assessment_calendar_detail'),
    path('assessment_calendar/detail/<int:day>/<int:month>/<int:year>', views.assessment_calendar_detail, name = 'assessment_calendar_detail'),
    path('assessment_calendar/view_conflict_detail/', views.view_conflict_detail, name = 'view_conflict_detail'),

    # Faculty Menu
    path('faculty_menu/all_faculty_program', views.all_faculty_program, name = 'all_faculty_program'),
    path('faculty_menu/faculty_program_detail/<int:program_id>', views.faculty_program_detail, name = 'faculty_program_detail'),
    path('faculty_menu/committee_appointment', views.committee_appointment, name = 'committee_appointment'),


    # Inbox System
    path('inbox', views.inbox, name = 'inbox'),
    path('inbox/?page=<int:page_number>/', views.inbox, name = 'inbox'),

    path('issue_detail/<int:issue_id>', views.issue_detail, name='issue_detail'),
    path('issue/create', views.create_issue, name = 'create_issue'),
    path('comment/create/<int:issue_id>', views.create_comment, name = 'create_comment'),

    path('edit/<int:issue_id>', views.edit_issue, name = 'edit_issue'),
    path('comment/edit/<int:issue_id>/<int:comment_id>', views.edit_comment, name='edit_comment'),

    
]  


