from selenium.webdriver.common.by import By


class sign_in:

    sign_in_link = (By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]")
    email_field = (By.XPATH, "//input[@id='email']")
    password_field = (By.XPATH, "//input[@name='login[password]']")
    sign_in_cta = (By.XPATH, "//button[@class='action login primary']")
    forgot_password_link = (By.XPATH, "//a[@class='action remind']")
    errors_empty_field = (By.XPATH, "//div[@class='mage-error']")
    error_signin = (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")

    def __init__(self, driver):
        self.driver = driver

    def signin(self):
        return self.driver.find_element(*sign_in.sign_in_link)

    def email_address(self):
        return self.driver.find_element(*sign_in.email_field)

    def password(self):
        return self.driver.find_element(*sign_in.password_field)

    def signin_cta(self):
        return self.driver.find_element(*sign_in.sign_in_cta)

    def forgot_password(self):
        return self.driver.find_element(*sign_in.forgot_password_link)

    def empty_filed_error(self):
        return self.driver.find_elements(*sign_in.errors_empty_field)

    def incorrect_input_error(self):
        return self.driver.find_element(*sign_in.error_signin)
