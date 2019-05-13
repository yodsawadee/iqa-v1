from study_program.models import AssessmentResult, Professor, StudyProgram, AUN
import xlrd

workbook = xlrd.open_workbook('C:/iqa_website_test/IQA-Website-for-KMITL-master/myvenv/Scripts/iqa_web/study_program/importDataScript/data/Revisedv2 Database_ [Assessors Matching & Assesment Scheduling_ An Application for IQA System].xlsx')
worksheet = workbook.sheet_by_name('AUN')

#shell()
#exec(open('C:/iqa_website_test/IQA-Website-for-KMITL-master/myvenv/Scripts/iqa_web/study_program/importDataScript/createAUNResult.py',encoding="utf8").read())

already_create = []
for i in range(2, worksheet.nrows):
#    print(worksheet.row(i))

    criteria1 = worksheet.row(i)[2].value
    criteria2 = worksheet.row(i)[3].value
    criteria3 = worksheet.row(i)[4].value
    criteria4 = worksheet.row(i)[5].value
    criteria5 = worksheet.row(i)[6].value
    criteria6 = worksheet.row(i)[7].value
    criteria7 = worksheet.row(i)[8].value
    criteria8 = worksheet.row(i)[9].value
    criteria9= worksheet.row(i)[10].value
    criteria10 = worksheet.row(i)[11].value
    criteria11 = worksheet.row(i)[12].value
    total_score = worksheet.row(i)[13].value


    
    code = worksheet.row(i)[1].value
    code = code[3:len(code)]
    #print(code)
    a = AssessmentResult.objects.get(code=code)
    assessment_id_id = a.id

    
    #print("AssessmentResult ID: ",a.id)
  
    if assessment_id_id not in already_create:
        aun = AUN.objects.create(
            criteria1 = criteria1,
            criteria2 = criteria2,
            criteria3 = criteria3,
            criteria4 = criteria4,
            criteria5 = criteria5,
            criteria6 = criteria6,
            criteria7 = criteria7,
            criteria8 = criteria8,
            criteria9 = criteria9,
            criteria10 = criteria10,
            criteria11 = criteria11,
            total_score = total_score,
            assessment_id_id = assessment_id_id
        )
        already_create.append(assessment_id_id)
        print("aee ok")
