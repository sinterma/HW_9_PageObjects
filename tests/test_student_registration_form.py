from model.student_registration_form import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name('Sosha')
    registration_page.fill_last_name('Hex')
    registration_page.fill_email('sinterma@gmail.com')
    registration_page.select_gender('Other')
    registration_page.fill_number('0987890690')
    registration_page.fill_date_of_birth('03', 'January', '1991')
    registration_page.scroll_page_to_the_end()
    registration_page.fill_subject('English')
    registration_page.select_hobby()
    registration_page.upload_photo()
    registration_page.fill_address('Germany', 'NCR', 'Delhi')

    registration_page.shoud_registered_user_with('Sosha Hex', 'sinterma@gmail.com', 'Other', '0987890690',
                                                 '03 January,1991',
                                                 'English', 'Music', 'picture.png', 'Germany',
                                                 'NCR Delhi')
