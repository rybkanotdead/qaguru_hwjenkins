import allure

from tests_test.model.pages.registration_page import RegistrationPage
import os

@allure.tag("allure test #1")
@allure.label("owner", "IK")
@allure.feature('Регистрация пользователя')
@allure.story('Регистрация пользователя с заполнением всех полей')
@allure.link("https://github.com", name='Testing')
def test_registers_user():
    registration_page = RegistrationPage()
    (registration_page.open()
     .fill_first_name('my_firstName')
     .fill_last_name('my_secondName')
     .fill_email('my_email@mail.com')
     .select_gender('Male')
     .remove_banner()
     .fill_mobile_number('8800555353')
     .fill_date_of_birth(1999, 8, 26)
     .fill_subject('Maths')
     .select_hobby('Sport')
     .set_upload_picture('image/images.jpg')
     .fill_current_address('Abaya26')
     .fill_state('NCR')
     .fill_city('Delhi')
     .click_submit_button()
     .should_have_registered('my_firstName', 'my_secondName', 'my_email@mail.com', 'Male', '8800555353', '26 September, 1999',
                             'Maths', 'Sports', 'images.jpg', 'Abaya26', 'NCR', 'Delhi'))