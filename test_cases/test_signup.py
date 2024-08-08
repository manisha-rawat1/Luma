import pytest
from Objectrepo.signup_obj import Signup_obj
from utilities.Baseclass import Baseclass


class Test_signup(Baseclass):

    def test_signup_all_field_empty(self):
        sign_up = Signup_obj(self.driver)
        sign_up.homelink().click()
        sign_up.sign_up_cta().click()
        expected_error = 'This is a required field.'
        actual_error = sign_up.error_msg().text
        assert actual_error == expected_error

    def test_signup_all_field_filled(self):
        sign_up = Signup_obj(self.driver)
        sign_up.homelink().click()
        sign_up.firstname().send_keys('Good')
        sign_up.lastname().send_keys('User')
        sign_up.email_add().send_keys('new@user.com')
        sign_up.pass_word().send_keys('newuser@123')
        sign_up.conf_pass_word().send_keys('newuser@123')
        sign_up.sign_up_cta().click()
        actual_success_message = sign_up.success_msg().text
        expected_msg = 'Thank you for registering with Main Website Store.'
        assert actual_success_message == expected_msg




