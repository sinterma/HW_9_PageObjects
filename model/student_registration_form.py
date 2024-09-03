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
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element(
            '..').click()

    def fill_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def scroll_page_to_the_end(self):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    def choose_subject_and_hobby(self, subject, hobby):
        browser.element('#subjectsInput').type(subject).press_enter()
        browser.all('.custom-checkbox').element_by(
            have.exact_text(hobby)).perform(
            command.js.scroll_into_view).click()

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
