import xlrd
from study_program.models import StudyProgram

workbook = xlrd.open_workbook('C:/Users/WIN10/Desktop/ToAjKo/IQAData.xlsx')
worksheet = workbook.sheet_by_name('Program (ข้อมูลหลักสูตร)')


#shell()
#exec(open('C:/iqa_website_test/IQA-Website-for-KMITL-master/myvenv/Scripts/iqa_web/study_program/importDataScript/createStudyProgramScript.py',encoding="utf8").read())

for i in range(2, worksheet.nrows):
#    print(worksheet.row(i))
    code = worksheet.row(i)[0].value

    if(worksheet.row(i)[6].value == 1):
        program_status = 'ACTIVE'
    elif(worksheet.row(i)[6].value == 2):
        program_status = 'GOING TO CLOSE'
    else:
        program_status = 'NOT ACTIVE'

    degree_and_major = worksheet.row(i)[3].value

    if(worksheet.row(i)[4].value == 1):
        collaboration_with_other_institues = 'Program issued specifically by KMITL'
    elif(worksheet.row(i)[4].value == 2):
        collaboration_with_other_institues = 'Program supported by other institutes'
    else:
        collaboration_with_other_institues = 'Collaborated program with other institutes'

    name = worksheet.row(i)[2].value
    pdf_docs = 'study_program_details/computer-science-resume-example-computer-science-resume-sample-0-u_l994DYD.jpg'


    st = StudyProgram.objects.create(code = code, program_status = program_status, name = name, collaboration_with_other_institues = collaboration_with_other_institues, degree_and_major = degree_and_major, pdf_docs = pdf_docs)
    print("aee ok")



