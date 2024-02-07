"""locators, links"""

#authorization
authorization_link_login = "https://stellarburgers.nomoreparties.site/login"
authorization_link_main = "https://stellarburgers.nomoreparties.site/"
authorization_email = "/html/body/div/div/main/div/form/fieldset[1]/div/div/input"
authorization_password = "/html/body/div/div/main/div/form/fieldset[2]/div/div/input"
authorization_login_button = "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa"
authorization_main_button = "/html/body/div/div/main/section[2]/div/button"
authorization_cabinet_button = "/html/body/div/div/header/nav/a/p"
authorization_login_forgot_password_button = "/html/body/div/div/main/div/div/p[2]/a"
authorization_login_remember_password_button = "/html/body/div/div/main/div/div/p/a"

#registration
registration_link = "https://stellarburgers.nomoreparties.site/register"
registration_name = "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input"
registration_email = "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input"
registration_password = "//input[@type='password']"
registration_button = "//button[text()='Зарегистрироваться']"
registration_already_exist_label = "/html/body/div/div/main/div/p"
registration_wrong_password_label = "//*[@id='root']/div/main/div/form/fieldset[3]/div/p"

#transition
cabinet_logo = "/html/body/div/div/header/nav/div/a"
cabinet_constructor = "/html/body/div/div/header/nav/ul/li[1]/a/p"

#constructor
constructor_bread_xpath = "//span[text()='Булки']"
constructor_sause_xpath = "//span[text()='Соусы']"
constructor_filling_xpath = "//span[text()='Начинки']"
constructor_current_class =  "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"

#exit
main_cabinet_button = "/html/body/div/div/header/nav/a/p"
cabinet_exit_button = "/html/body/div/div/main/div/nav/ul/li[3]/button"