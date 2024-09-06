from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth_year: str
    date_of_birth_month: str
    date_of_birth_day: str
    subject: str
    hobby: str
    file: str
    address: str
    state: str
    city: str


user_data = User(
    first_name='Sosha',
    last_name='Hex',
    email='sinterma@gmail.com',
    gender='Other',
    phone_number='4817859887',
    date_of_birth_year='1991',
    date_of_birth_month='January',
    date_of_birth_day='03',
    subject='English',
    hobby='Music',
    file='picture.png',
    address='Germany',
    state='NCR',
    city='Delhi'
)