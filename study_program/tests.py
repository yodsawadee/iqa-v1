from django.test import TestCase
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# class LoginTestCase(unittest.TestCase):

#     def setUp(self):
#         chromedriver = "./chromedriver"
#         self.browser = webdriver.Chrome(chromedriver)
#         self.browser.get('http://localhost:8000/')
#         # self.browser.get('http://iqa-v2.herokuapp.com/')

#     def test_login(self):
#         username = self.browser.find_element_by_name('username')
#         password = self.browser.find_element_by_name('password')
#         # login_submit = self.browser.find_element_by_css_selector('input.btn.btn-outline-success.col-md-4.mr-2')
#         username.send_keys('yod')
#         password.send_keys('1234')        
#         login_submit.click()
#         time.sleep(3)

#     def tearDown(self):
#         self.browser.close()


# if __name__ == "__main__":
#     unittest.main()
    

#     # def test_something_that_will_pass(self):
#     #     time.sleep(1)
#     #     username = self.browser.find_element_by_name('username')
#     #     username.send_keys('yod')
#     #     time.sleep(1)
#     #     password = self.browser.find_element_by_name('password')
#     #     password.send_keys('1234')
#     #     time.sleep(1)
#     #     elem_guests = self.browser.find_element_by_id('Login-btn')
#     #     elem_guests.click()
#     #     time.sleep(5)
#     #     # self.assertFalse(False)

#     # def test_something_that_will_fail(self):
#     #     time.sleep(1)
#     #     username = self.browser.find_element_by_name('username')
#     #     username.send_keys('jan')
#     #     time.sleep(1)
#     #     password = self.browser.find_element_by_name('password')
#     #     password.send_keys('1234')
#     #     time.sleep(1)
#     #     elem_guests = self.browser.find_element_by_id('Login-btn')
#     #     elem_guests.click()
#     #     time.sleep(5)
#     #     # self.assertTrue(False)


#=========================================================================================================
# class StudyProgramTestCase(unittest.TestCase):
    
#     def setUp(self):
#         chromedriver = "./chromedriver"
#         self.browser = webdriver.Chrome(chromedriver)
#         self.browser.get('http://localhost:8000/')

#         ##----Login----
#         username = self.browser.find_element_by_name('username')
#         password = self.browser.find_element_by_name('password')
#         elem_guests = self.browser.find_element_by_css_selector('input.btn.btn-outline-success.col-md-4.mr-2')

#         username.send_keys('thisisadmin')
#         password.send_keys('thisispassword')
#         elem_guests.click()
#         time.sleep(1)

#     def tearDown(self):
#         self.browser.close()
    
#     def test_study_program(self):
#         browser = self.browser
#         ##----view all study program-------------------------------------------------------------------------------------
#         elem_guests = browser.find_element_by_id('StudyProgram-btn')
#         elem_guests.click()
#         time.sleep(1)

#         # elem_guests = browser.find_element_by_id('Home-nav-btn')
#         # elem_guests.click()
#         # time.sleep(1)

#         # elem_guests = browser.find_element_by_id('StudyProgram-btn')
#         # elem_guests.click()
#         # time.sleep(1)


#         # elem_guests = browser.find_element_by_link_text('1')
#         # elem_guests.click()
#         # time.sleep(1)

#         # ##----create study program-------------------------------------------------------------------------------------
#         # elem_guests = browser.find_element_by_id('Add-btn')
#         # elem_guests.click()
#         # time.sleep(1)
#         # ## find the form element
#         # code = browser.find_element_by_id('id_code')
#         # name = browser.find_element_by_id('id_name')
#         # program_status_ACTIVE = browser.find_element_by_xpath("//select[@id='id_program_status']/option[@value='ACTIVE']")
#         # degree_and_major = browser.find_element_by_id('id_degree_and_major')
#         # program_issued_specifically_by_KMITL = browser.find_element_by_xpath("//select[@id='id_collaboration_with_other_institues']/option[@value='Program issued specifically by KMITL']")

#         # pdf_docs = browser.find_element_by_id('id_pdf_docs')

#         # responsible_professor_1 = browser.find_element_by_xpath("//select[@id='id_responsible_professors']/option[@value='4']")
#         # responsible_professor_2 = browser.find_element_by_xpath("//select[@id='id_responsible_professors']/option[@value='13']")
#         # responsible_professor_3 = browser.find_element_by_xpath("//select[@id='id_responsible_professors']/option[@value='10']")
#         # save_btn = browser.find_element_by_css_selector('input.btn.btn-success.col-2')

#         # ## fill the form with data
#         # code.send_keys('sp1')
#         # name.send_keys('หลักสูตรสมมุติขึ้นมาเองเพื่อการเทส')
#         # program_status_ACTIVE.click()
#         # degree_and_major.send_keys('การเทสบัณฑิต (การเทส)')
#         # program_issued_specifically_by_KMITL.click()

#         # # pdf_docs.send_keys('./pdf-file.png')
#         # # time.sleep(5)

#         # responsible_professor_1.click()
#         # responsible_professor_2.click()
#         # responsible_professor_3.click()

#         # save_btn.click()
#         # time.sleep(2)

#         ##----view study program detail-----------------------------------------------------------------------------------------
#         # program = browser.find_element_by_xpath("//a[@id='text-list'][2]")
#         # time.sleep(2)
#         # program.click()

#         last_page_no = browser.find_element_by_css_selector('i.fa.fa-angle-double-right')
#         time.sleep(2)
#         last_page_no.click()
#         time.sleep(2)
#         program = browser.find_element_by_xpath("//a[@id='text-list'][6]")
#         time.sleep(2)
#         program.click()
#         time.sleep(5)

#         ##----edit study program-------------------------------------------------------------------------------------
#         # elem_guests = browser.find_element_by_css_selector('button.btn.btn-outline-success')#can't find!
#         elem_guests = browser.find_element_by_id('EditProfile-btn')
#         elem_guests.click()
#         time.sleep(1)
#         ## find the form element
#         program_status_ACTIVE = browser.find_element_by_xpath("//select[@id='id_program_status']/option[@value='ACTIVE']")
#         program_status_NOT_ACTIVE = browser.find_element_by_xpath("//select[@id='id_program_status']/option[@value='NOT ACTIVE']")
#         save_btn = browser.find_element_by_css_selector('input.btn.btn-success.col-2')
#         ## fill the form with data
#         # program_status_ACTIVE.click()
#         program_status_NOT_ACTIVE.click()
#         save_btn.click()
#         time.sleep(5)


#=========================================================================================================
# class ProfessorTestCase(unittest.TestCase):
    
#     def setUp(self):
#         chromedriver = "./chromedriver"
#         self.browser = webdriver.Chrome(chromedriver)
#         self.browser.get('http://localhost:8000/')

#         ##----Login----
#         username = self.browser.find_element_by_name('username')
#         password = self.browser.find_element_by_name('password')
#         elem_guests = self.browser.find_element_by_css_selector('input.btn.btn-outline-success.col-md-4.mr-2')

#         username.send_keys('thisisadmin')
#         password.send_keys('thisispassword')
#         elem_guests.click()
#         time.sleep(1)

#     def tearDown(self):
#         self.browser.close()
    
#     def test_professor(self):
#         browser = self.browser
#         #----view all professor-------------------------------------------------------------------------------------
#         elem_guests = browser.find_element_by_id('Professors-btn')
#         elem_guests.click()
#         time.sleep(1)

#         # ##----create professor-------------------------------------------------------------------------------------
#         # elem_guests = browser.find_element_by_id('Add-btn')
#         # elem_guests.click()
#         # time.sleep(1)
#         # ## find the form element
#         # professor_id = browser.find_element_by_id('id_professor_id')
#         # academic_title = browser.find_element_by_id('id_academic_title')
#         # name_surname = browser.find_element_by_id('id_name_surname')
#         # date_of_birth = browser.find_element_by_id('id_date_of_birth')
#         # bsc	= browser.find_element_by_id('id_bsc')
#         # bsc_grad_institute = browser.find_element_by_id('id_bsc_grad_institute')

#         # bsc_year_1989 = browser.find_element_by_xpath("//select[@id='id_bsc_year']/option[@value='1989']")

#         # msc = browser.find_element_by_id('id_msc')
#         # msc_grad_institute = browser.find_element_by_id('id_msc_grad_institute')

#         # msc_year_1999 = browser.find_element_by_xpath("//select[@id='id_msc_year']/option[@value='1999']")

#         # phd = browser.find_element_by_id('id_phd')
#         # phd_grad_institute = browser.find_element_by_id('id_phd_grad_institute')

#         # phd_year_2004 = browser.find_element_by_xpath("//select[@id='id_phd_year']/option[@value='2004']")

#         # phone = browser.find_element_by_id('id_phone')
#         # email = browser.find_element_by_id('id_email')
#         # university = browser.find_element_by_id('id_university')
#         # additional_degree = browser.find_element_by_id('id_additional_degree')

#         # responsible_program_186 = browser.find_element_by_xpath("//select[@id='id_responsible_program']/option[@value='4']")

#         # save_btn = browser.find_element_by_css_selector('input.btn.btn-success.col-2')

#         # ## fill the form with data
#         # professor_id.send_keys('CHIVTM') #CHIVTE already exist
#         # academic_title.send_keys('Asst.Prof.Dr.')
#         # name_surname.send_keys('Chivalai Temiyasathit')
#         # date_of_birth.send_keys('1848-9-3')
#         # bsc.send_keys('B.Eng. Industrial Engineering')
#         # bsc_grad_institute.send_keys('Chulalongkorn University')

#         # bsc_year_1989.click()

#         # msc.send_keys('M.S. Industrial Engineering')
#         # msc_grad_institute.send_keys('University of Texas Arlington, USA')

#         # msc_year_1999.click()

#         # phd.send_keys('Ph.D. Industrial Engineering')
#         # phd_grad_institute.send_keys('University of Texas Arlington, USA')

#         # phd_year_2004.click()

#         # phone.send_keys('099-999-9999')
#         # email.send_keys('ktchival@kmitl.ac.th')
#         # university.send_keys('KMITL')

#         # responsible_program_186.click()
#         # time.sleep(5)
#         # save_btn.click()
#         # time.sleep(2)

#         ##----view study professor detail-----------------------------------------------------------------------------------------
#         # elem_guests = browser.find_element_by_class_name('list-group-item list-group-item-light bg-light')
#         # elem_guests.click()

#         # elem_guests = browser.find_element_by_id('text-list')
#         # elem_guests.click()
#         professor = browser.find_element_by_xpath("//a[@id='text-list'][4]")
#         professor.click()


#         ##----edit study program-------------------------------------------------------------------------------------
#         # elem_guests = browser.find_element_by_css_selector('button.btn.btn-outline-success')#can't find!
#         elem_guests = browser.find_element_by_id('EditProfile-btn')
#         elem_guests.click()

#         date_of_birth = browser.find_element_by_id('id_date_of_birth')
#         time.sleep(2)
#         date_of_birth.clear()
#         time.sleep(2)
#         date_of_birth.send_keys('1999-11-11')

#         bsc	= browser.find_element_by_id('id_bsc')
#         bsc_grad_institute = browser.find_element_by_id('id_bsc_grad_institute')
#         bsc_year_1989 = browser.find_element_by_xpath("//select[@id='id_bsc_year']/option[@value='1989']")
#         msc = browser.find_element_by_id('id_msc')
#         msc_grad_institute = browser.find_element_by_id('id_msc_grad_institute')
#         msc_year_1999 = browser.find_element_by_xpath("//select[@id='id_msc_year']/option[@value='1999']")
#         phd = browser.find_element_by_id('id_phd')
#         phd_grad_institute = browser.find_element_by_id('id_phd_grad_institute')
#         phd_year_2004 = browser.find_element_by_xpath("//select[@id='id_phd_year']/option[@value='2004']")
#         phone = browser.find_element_by_id('id_phone')
#         email = browser.find_element_by_id('id_email')
#         university = browser.find_element_by_id('id_university')
#         additional_degree = browser.find_element_by_id('id_additional_degree')

#         save_btn = browser.find_element_by_css_selector('input.btn.btn-success.col-2')

#         ## fill the form with data
#         bsc.send_keys('-')
#         bsc_grad_institute.send_keys('-')
#         bsc_year_1989.click()
#         msc.send_keys('-')
#         msc_grad_institute.send_keys('-')
#         msc_year_1999.click()
#         phd.send_keys('-')
#         phd_grad_institute.send_keys('-')
#         phd_year_2004.click()
#         phone.send_keys('_')
#         email.send_keys('-')
#         university.send_keys('-')

#         time.sleep(5)
#         save_btn.click()

#=========================================================================================================
# class CommitteeTestCase(unittest.TestCase):
    
#     def setUp(self):
#         chromedriver = "./chromedriver"
#         self.browser = webdriver.Chrome(chromedriver)
#         self.browser.get('http://localhost:8000/')

#         ##----Login----
#         username = self.browser.find_element_by_name('username')
#         password = self.browser.find_element_by_name('password')
#         elem_guests = self.browser.find_element_by_css_selector('input.btn.btn-outline-success.col-md-4.mr-2')

#         username.send_keys('thisisadmin')
#         password.send_keys('thisispassword')
#         elem_guests.click()
#         time.sleep(1)

#     def tearDown(self):
#         self.browser.close()
    
#     def test_committee(self):
#         browser = self.browser
#         # ----view all committee-------------------------------------------------------------------------------------
#         elem_guests = browser.find_element_by_id('Assessment-btn')
#         time.sleep(1)
#         elem_guests.click()

#         elem_guests = browser.find_element_by_id('CommitteeList-btn')
#         time.sleep(1)
#         elem_guests.click()

#         # ##----create committee-------------------------------------------------------------------------------------
#         # elem_guests = browser.find_element_by_id('Add-btn')
#         # elem_guests.click()
#         # time.sleep(1)
#         # ## find the form element
#         # code = browser.find_element_by_id('id_code')
#         # professor_id_2 = browser.find_element_by_xpath("//select[@id='id_professor_id']/option[@value='2']")#วสุ อุดมเพทายกุล
#         # year_1989 = browser.find_element_by_xpath("//select[@id='id_year']/option[@value='1989']")
#         # assessment_level_Senior = browser.find_element_by_xpath("//select[@id='id_assessment_level']/option[@value='Senior']")
#         # profession = browser.find_element_by_id('id_profession')
#         # save_btn = browser.find_element_by_css_selector('input.btn.btn-success.col-2')

#         # ## fill the form with data
#         # code.send_keys('sp1')
#         # professor_id_2.click()
#         # year_1989.click()
#         # assessment_level_Senior.click()
#         # profession.send_keys('-')
#         # time.sleep(5)
#         # save_btn.click()
#         # time.sleep(2)

#         ##----view committee detail-----------------------------------------------------------------------------------------
#         professor = browser.find_element_by_xpath("//a[@id='text-list'][1]")
#         professor.click()


#         ##----edit committee-------------------------------------------------------------------------------------
#         elem_guests = browser.find_element_by_id('EditProfile-btn')
#         elem_guests.click()

#         ## find the form element
#         code = browser.find_element_by_id('id_code')
#         professor_id_2 = browser.find_element_by_xpath("//select[@id='id_professor_id']/option[@value='2']")#วสุ อุดมเพทายกุล
#         year_1989 = browser.find_element_by_xpath("//select[@id='id_year']/option[@value='1989']")
#         assessment_level_Senior = browser.find_element_by_xpath("//select[@id='id_assessment_level']/option[@value='Senior']")
#         profession = browser.find_element_by_id('id_profession')
#         save_btn = browser.find_element_by_css_selector('input.btn.btn-success.col-2')

#         ## fill the form with data
#         code.clear()
#         code.send_keys('sp1')
#         professor_id_2.click()
#         year_1989.click()
#         assessment_level_Senior.click()
#         profession.clear()
#         profession.send_keys('somethings')
#         time.sleep(5)
#         save_btn.click()
#         time.sleep(2)

#=========================================================================================================
# class AssessmentTestCase(unittest.TestCase):
    
#     def setUp(self):
#         chromedriver = "./chromedriver"
#         self.browser = webdriver.Chrome(chromedriver)
#         self.browser.get('http://localhost:8000/')

#         ##----Login----
#         username = self.browser.find_element_by_name('username')
#         password = self.browser.find_element_by_name('password')
#         elem_guests = self.browser.find_element_by_css_selector('input.btn.btn-outline-success.col-md-4.mr-2')

#         username.send_keys('thisisadmin')
#         password.send_keys('thisispassword')
#         elem_guests.click()
#         time.sleep(1)

#     def tearDown(self):
#         self.browser.close()
    
#     def test_assessment(self):
#         browser = self.browser
#         # ----view all assessment-------------------------------------------------------------------------------------
#         elem_guests = browser.find_element_by_id('Assessment-btn')
#         time.sleep(1)
#         elem_guests.click()

#         elem_guests = browser.find_element_by_id('AssessmentResults-btn')
#         time.sleep(1)
#         elem_guests.click()

#         # ##----create assessment-------------------------------------------------------------------------------------
#         elem_guests = browser.find_element_by_id('Add-btn')
#         elem_guests.click()
#         time.sleep(1)
#         ## find the form element
#         code = browser.find_element_by_id('id_code')
#         committee_id_1 = browser.find_element_by_xpath("//select[@id='id_committee_id']/option[@value='1']")
#         program_id_2 = browser.find_element_by_xpath("//select[@id='id_program_id']/option[@value='2']")
#         year_1989 = browser.find_element_by_xpath("//select[@id='id_year']/option[@value='1989']")
#         curriculum_status_Modify = browser.find_element_by_xpath("//select[@id='id_curriculum_status']/option[@value='Modify']")
#         curriculum_status_year_1989 = browser.find_element_by_xpath("//select[@id='id_curriculum_status_year']/option[@value='1989']")
#         curriculum_standard_1989 = browser.find_element_by_xpath("//select[@id='id_curriculum_standard']/option[@value='1989']")
#         pdf_docs = browser.find_element_by_id('id_pdf_docs')

#         save_btn = browser.find_element_by_css_selector('input.btn.btn-success.col-2')

#         ## fill the form with data
#         code.send_keys('ar1')
#         committee_id_1.click()
#         program_id_2.click()
#         year_1989.click()
#         curriculum_status_Modify.click()
#         curriculum_status_year_1989.click()
#         curriculum_standard_1989.click()

#         pdf_docs.send_keys('./pdf-file.png')

#         time.sleep(5)
#         save_btn.click()
#         time.sleep(2)




# if __name__ == "__main__":
#     # LoginTestCase()
#     # StudyProgramTestCase()
#     # ProfessorTestCase()
#     unittest.main()

#---------------------------------------------------------------------------------------------------------

chromedriver = "./chromedriver"
browser = webdriver.Chrome(chromedriver)
browser.get('http://localhost:8000/')
# browser.get('http://iqa-v2.herokuapp.com/')

##----Login----
username = browser.find_element_by_name('username')
password = browser.find_element_by_name('password')
# elem_guests = browser.find_element_by_id('Login-btn')
elem_guests = browser.find_element_by_css_selector('input.btn.btn-outline-success.col-md-4.mr-2')

username.send_keys('thisisadmin')
password.send_keys('thisispassword')
# time.sleep(5)
elem_guests.click()
# time.sleep(1)

# ----view assessment calendar-------------------------------------------------------------------------------------
elem_guests = browser.find_element_by_id('IQA-btn')
time.sleep(1)
elem_guests.click()

elem_guests = browser.find_element_by_id('Calendar-btn')
time.sleep(1)
elem_guests.click()





# browser.close()