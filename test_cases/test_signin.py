import pytest

from utilities.Baseclass import Baseclass
from Objectrepo.signin_obj import sign_in
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_signin(Baseclass):

    @pytest.mark.regression
    def test_verify_sign_in_page(self):
        login = sign_in(self.driver)
        login.signin().click()
        expected_title = 'Customer Login'
        actual_title = self.driver.title
        assert actual_title == expected_title

    @pytest.mark.regression
    def test_sign_in_with_empty_field(self):
        login = sign_in(self.driver)
        login.signin().click()
        login.signin_cta().click()
        expected_error = 'This is a required field.'
        actual_errors = login.empty_filed_error()
        for error in actual_errors:
            if error.text == expected_error:
                print('Error message displayed! Successfully.')
                break

        login.password().send_keys('Newpassword@123')
        login.signin_cta().click()
        for error in actual_errors:
            if error.text == expected_error:
                print('Error message displayed! Successfully.')
                break

    @pytest.mark.regression
    def test_sign_in_incorrect_credentials(self):
        login = sign_in(self.driver)
        login.signin().click()
        login.email_address().send_keys('xyz@qay.com')
        login.password().send_keys('Newpassword@123')
        login.signin_cta().click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(login.error_signin))
        expected_error = 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
        actual_error = login.incorrect_input_error().text
        assert actual_error == expected_error
        login.forgot_password().click()
        self.driver.back()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_sign_in_correct_credentials(self):
        login = sign_in(self.driver)
        login.signin().click()
        login.email_address().send_keys('qw@qa.com')
        login.password().send_keys('poppop@123')
        login.signin_cta().click()
        actual_page_title = self.driver.title
        expected_page_title = 'Home Page'
        assert actual_page_title == expected_page_title







        
