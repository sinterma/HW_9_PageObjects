import os
from selene import browser, have, command, be
import tests


class RegistrationPage():

    def open(self):
        browser.open('/')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.visible)

    def fill_last_name(self, value):
        browser.element('#lastName').type('Hex')

    def fill_email(self, value):
        browser.element('#userEmail').type('sinterma@gmail.com')

    def select_gender(self, value):
        browser.element('[for="gender-radio-3"]').click()

    def fill_number(self, value):
        browser.element('#userNumber').type('0987890690')

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def scroll_page_to_the_end(self):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    def fill_subject(self, value):
        browser.element('#subjectsInput').type('English').press_enter()

    def select_hobby(self):
        browser.element('[for="hobbies-checkbox-3"]').click()

    def upload_photo(self):
        browser.element('#uploadPicture').send_keys(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), 'resources/picture.png')
            )
        )

    def fill_address(self, address, state, city):
        browser.element('#currentAddress').type(address)
        browser.element("#react-select-3-input").type(state).press_enter()
        browser.element('#react-select-4-input').type(city).press_enter()
        browser.element('#submit').click()

    def shoud_registered_user_with(self, full_name, mail, gender, number, date_of_birth, subject, hobby, file, address,
                                   state_and_city):
        browser.element('.modal-content').element('table').all('tr').all('td').even.should(have.exact_texts(
            full_name, mail, gender, number, date_of_birth, subject,
            hobby, file, address, state_and_city))
