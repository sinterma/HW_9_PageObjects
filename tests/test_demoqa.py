from demoqa_tests.data import user_info
from demoqa_tests.pages.registration_page import RegistrationFormPage


def test_fill_registration_form():
    sosha = user_info.user_data
    register_page = RegistrationFormPage()

    register_page.open()
    register_page.register(sosha)
    register_page.should_register_user_with(sosha)