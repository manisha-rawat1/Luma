from selenium.webdriver.common.by import By


class Signup_obj:

    home_link = (By.XPATH, "//div[@class='panel header']//a[text() = 'Create an Account']")
    first_name = (By.XPATH, "//input[@id='firstname']")
    last_name = (By.XPATH, "//input[@id='lastname']")
    email = (By.XPATH, "//input[@id='email_address']")
    password = (By.XPATH, "//input[@id='password']")
    conf_password = (By.XPATH, "//input[@id='password-confirmation']")
    signup_btn = (By.XPATH, "//button[@class='action submit primary']")
    error = (By.XPATH, "//div[@id='firstname-error']")
    s_msg = (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")

    def __init__(self, driver):
        self.driver = driver

    def homelink(self):
        return self.driver.find_element(*Signup_obj.home_link)

    def firstname(self):
        return self.driver.find_element(*Signup_obj.first_name)

    def lastname(self):
        return self.driver.find_element(*Signup_obj.last_name)

    def email_add(self):
        return self.driver.find_element(*Signup_obj.email)

    def pass_word(self):
        return self.driver.find_element(*Signup_obj.password)

    def conf_pass_word(self):
        return self.driver.find_element(*Signup_obj.conf_password)

    def sign_up_cta(self):
        return self.driver.find_element(*Signup_obj.signup_btn)

    def error_msg(self):
        return self.driver.find_element(*Signup_obj.error)

    def success_msg(self):
        return self.driver.find_element(*Signup_obj.s_msg)
