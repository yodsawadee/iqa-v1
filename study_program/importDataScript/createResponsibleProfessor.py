#import psycopg2
import xlrd
from study_program.models import Professor
from study_program.models import StudyProgram


workbook = xlrd.open_workbook('C:/Users/WIN10/Dropbox/IQA_Data_Excel/study_program.xlsx')
worksheet = workbook.sheet_by_name('StudyProgram-Professor')

#shell()
#exec(open('C:/iqa_website_test/IQA-Website-for-KMITL-master/myvenv/Scripts/iqa_web/study_program/importDataScript/createResponsibleProfessor.py',encoding="utf8").read())

for i in range(1, worksheet.nrows):
    id_kub = worksheet.row(i)[0].value
    study_program_id = int(worksheet.row(i)[1].value)
    professor_id = int(worksheet.row(i)[2].value)
    
    a = Professor.objects.get(pk=professor_id)
    b = StudyProgram.objects.get(pk = study_program_id)
    a.responsible_program.add(b)



    print("aee ok")
    


