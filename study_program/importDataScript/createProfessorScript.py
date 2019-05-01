#import psycopg2
import xlrd
from study_program.models import Professor


workbook = xlrd.open_workbook('C:/Users/WIN10/Dropbox/IQA_Data_Excel/study_program.xlsx')
worksheet = workbook.sheet_by_name('professor')

#shell()
#exec(open('C:/iqa_website_test/IQA-Website-for-KMITL-master/myvenv/Scripts/iqa_web/study_program/importDataScript/createProfessorScript.py',encoding="utf8").read())

for i in range(1, worksheet.nrows):
    id_kub = worksheet.row(i)[0].value
    professor_id = worksheet.row(i)[1].value
    academic_title = worksheet.row(i)[2].value
    name_surname = worksheet.row(i)[3].value
    if(worksheet.row(i)[4].value == ''):
        date_of_birth = "1999-11-11"
    else:
        date_of_bith = worksheet.row(i)[4].value
   
    bsc = worksheet.row(i)[5].value
    bsc_grad_institute = worksheet.row(i)[6].value
    if(worksheet.row(i)[7].value == ''):
        bsc_year = 0
    else:
        bsc_year = int(worksheet.row(i)[7].value)
    msc = worksheet.row(i)[8].value
    msc_grad_institute = worksheet.row(i)[9].value
    if(worksheet.row(i)[10].value == ''):
        msc_year = 0
    else:
        msc_year = int(worksheet.row(i)[10].value)
    phd = worksheet.row(i)[11].value
    phd_grad_institute = worksheet.row(i)[12].value
    if(worksheet.row(i)[13].value == ''):
        phd_year = 0
    else:
        phd_year = int(worksheet.row(i)[13].value)
    phone = worksheet.row(i)[14].value
    email = worksheet.row(i)[15].value
    university = worksheet.row(i)[16].value
    additional_degree = worksheet.row(i)[17].value

    #print(int(id_kub),str(professor_id),str(name_surname),str(date_of_birth),str(bsc),str(bsc_grad_institute),str(bsc_year),str(msc),str(msc_grad_institute),str(msc_year),str(phd),str(phd_grad_institute),str(phd_year),str(phone),str(email),str(university),str(additional_degree))
    
    #conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=kraikrai")
    #cur = conn.cursor()

    #insert_query = "insert into public.study_program_professor values ({}, '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}',{}, '{}', '{}',{}, '{}', '{}','{}','{}')".format(int(id_kub),professor_id,academic_title,name_surname,date_of_birth,bsc,bsc_grad_institute,bsc_year,msc,msc_grad_institute,msc_year,phd,phd_grad_institute,phd_year,phone,email,university,additional_degree)
    #print(insert_query)
    #insert_query = "insert into public.study_program_studyprogram values (2, 'ENGAGROINDBMT', 'ACTIVE', 'วิศวกรรมศาสตรบัณฑิต (วิศวกรรมระบบอุตสาหกรรมการเกษตร)', 'Program issued specifically by KMITL', 'หลักสูตรวิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมระบบอุตสาหกรรมการเกษตร (ต่อเนื่อง)', 'study_program_details/computer-science-resume-example-computer-science-resume-sample-0-u_l994DYD.jpg')"
    #cur.execute(insert_query)
    #conn.commit()
    p = Professor.objects.create(professor_id = professor_id, academic_title=academic_title, name_surname=name_surname, date_of_birth=date_of_birth, bsc=bsc,bsc_grad_institute=bsc_grad_institute, bsc_year=bsc_year, msc=msc, msc_grad_institute=msc_grad_institute,msc_year=msc_year,phd=phd,phd_grad_institute=phd_grad_institute,phd_year=phd_year, phone=phone, email=email, university=university, additional_degree=additional_degree )

    print("aee ok")
    


