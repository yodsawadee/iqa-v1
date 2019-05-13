from study_program.models import AssessmentResult, Professor, StudyProgram
import xlrd

workbook = xlrd.open_workbook('C:/iqa_website_test/IQA-Website-for-KMITL-master/myvenv/Scripts/iqa_web/study_program/importDataScript/data/Revisedv2 Database_ [Assessors Matching & Assesment Scheduling_ An Application for IQA System].xlsx')
worksheet = workbook.sheet_by_name('AssessmentResult (ผลการประเมิน)')

#shell()
#exec(open('C:/iqa_website_test/IQA-Website-for-KMITL-master/myvenv/Scripts/iqa_web/study_program/importDataScript/createAssessmentResult.py',encoding="utf8").read())

for i in range(2, worksheet.nrows):
#    print(worksheet.row(i))

    code = worksheet.row(i)[0].value
    year = int(worksheet.row(i)[2].value)
    if(worksheet.row(i)[4].value == 1):
        curriculum_status = "New"
    else:
        curriculum_status = "Modify"
    

    curriculum_status_year = int(worksheet.row(i)[5].value)
    
    # if 1 == 2548, 2 == 2558
    curriculum_standard = int(worksheet.row(i)[6].value)
    pdf_docs = 'study_program_details/computer-science-resume-example-computer-science-resume-sample-0-u_l994DYD.jpg'
    
    try:
        a = StudyProgram.objects.get(code=worksheet.row(i)[3].value)
    
        program_id_id = a.id
    except:
        program_id_id = None




    ar = AssessmentResult.objects.create(code = code, year = year, curriculum_status = curriculum_status, curriculum_status_year = curriculum_status_year, curriculum_standard = curriculum_standard, pdf_docs = pdf_docs, program_id_id = program_id_id)
    print("aee ok")
