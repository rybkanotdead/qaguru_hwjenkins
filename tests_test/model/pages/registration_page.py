import time

import allure, os
from selene import browser, be, have
from selenium.webdriver.common.by import By


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.element('#gender-radio-1 + .custom-control-label')
        self.user_number = browser.element('#userNumber')

        self.date_of_birth_input = browser.element('#dateOfBirthInput')
        self.year = browser.element('.react-datepicker__year-select')
        self.month = browser.element('.react-datepicker__month-select')

        self.subjects_input = browser.element('#subjectsInput')
        self.hobbies = browser.all("#hobbiesWrapper .custom-control-label")
        self.upload_picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')

        self.state = browser.element('#state')
        self.city = browser.element('#city')

    @allure.step("Открыть страницу с формой регистрации пользователя")
    def open(self):
        browser.open('/automation-practice-form')
        return self

    @allure.step("Закрыть баннер (если есть)")
    def remove_banner(self):
        browser.element('footer').execute_script('element.remove()')
        return self

    @allure.step("Ввод имени")
    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    @allure.step("Ввод фамилии")
    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    @allure.step("Ввод почты")
    def fill_email(self, value):
        self.email.type(value)
        return self

    @allure.step("Выбор пола")
    def select_gender(self, value):
        browser.element(f'[value={value}]').element('..').click()
        return self

    @allure.step("Ввод телефона")
    def fill_mobile_number(self, value):
        self.user_number.type(value)
        return self

    @allure.step("Выбор даты рождения")
    def fill_date_of_birth(self, year, month, day):
        self.date_of_birth_input.click()
        self.year.click().element(f'[value="{year}"]').click()
        self.month.click().element(f'[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    @allure.step("Выбор предмета")
    def fill_subject(self, value):
        self.subjects_input.type(value).press_enter()
        return self

    @allure.step("Выбор хобби")
    def select_hobby(self, value):
        hobby_element = self.hobbies.element_by(have.text(value))
        hobby_element.perform(lambda e: browser.execute_script("arguments[0].scrollIntoView();", e))
        hobby_element.click()
        return self

    @allure.step("Загрузка картинки")
    def set_upload_picture(self, value):
        #self.upload_picture.type(os.path.abspath(value))
        self.upload_picture.type(os.path.abspath(os.path.join(os.path.dirname(__file__), f"../image/{value}")))
        return self

    @allure.step("Ввод адреса проживания")
    def fill_current_address(self, value):
        self.current_address.type(value)
        return self

    @allure.step("Выбор штата")
    def fill_state(self, value):
        self.state.click().all("#state div").element_by(have.exact_text(value)).click()
        return self

    @allure.step("Выбор города")
    def fill_city(self, value):
        self.city.click().all("#city div").element_by(have.exact_text(value)).click()
        return self

    @allure.step("Клик по кнопке Подтвердить")
    def click_submit_button(self):
        browser.element('#submit').should(be.visible).click()
        return self

    @allure.step("Проверка отображения данных о пользователе после регистрации")
    def should_have_registered(self, first_name, last_name, email, gender, phone_number, date_of_birth, subject,
                               hobbie, picture, address, state, city):
        browser.element('.table').all('td:nth-child(2)').should(have.texts(
            f'{first_name} {last_name}', email, gender, phone_number, date_of_birth,
            subject, hobbie, picture, address, f'{state} {city}'.strip()))
        return self

    @allure.step("Клик по кнопке Закрыть")
    def click_close_button(self):
        browser.element('#closeLargeModal').should(be.visible).click()
        return self