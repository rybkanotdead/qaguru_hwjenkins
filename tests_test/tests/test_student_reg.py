import allure
from tests_test.model.pages.registration_page import RegistrationPage


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
     .fill_mobile_number('8999123456')
     .fill_date_of_birth(2013, 5, 21)
     .fill_subject('Hindi')
     .fill_subject('Maths')
     .select_hobby('Sports')
     .set_upload_picture(os.path.abspath('tests_test/image/images.png'))
     .fill_current_address('my_curr_address')
     .fill_state('NCR')
     .fill_city('Delhi')
     .click_submit_button()
     .should_have_registered('my_firstName', 'my_secondName', 'my_email@mail.com', 'Male', '8999123456', '21 June,2013',
                             'Hindi, Maths', 'Sports', 'images.png', 'my_curr_address', 'NCR', 'Delhi'))