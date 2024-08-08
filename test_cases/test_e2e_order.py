import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Objectrepo.product_page_obj import prod_page_obj
from utilities.Baseclass import Baseclass
from selenium.webdriver.support.ui import Select


class Test_cart(Baseclass):

    @pytest.mark.sanity
    def test_place_order_successfully(self):
        logs = Baseclass.logger()
        logs.info("**********Place_order_Testcase_execution_started**********")
        prod = prod_page_obj(self.driver)
        wait = WebDriverWait(self.driver, 40)
        wait.until(EC.presence_of_element_located(prod.nav_bar))
        wait.until(EC.element_to_be_clickable(prod.nav_bar))
        prod.nav().click()
        prod.side_nav().click()
        prod.gender_cat().click()
        wait.until(EC.element_to_be_clickable(prod.side_bar_cat))
        prod.gender().click()
        all_prod = prod.product_list()
        ind = 0
        for product in all_prod:
            if product.text == ' Summit Watch ':
                break
            else:
                ind = ind + 1

        add_button = prod.add_to_bag(ind)
        box = prod.price_box(ind)
        action = ActionChains(self.driver)
        action.move_to_element(box).perform()
        action.move_to_element(add_button).perform()
        wait.until(EC.element_to_be_clickable(add_button))
        add_button.click()
        wait.until(EC.visibility_of_element_located(prod.cart_icon))
        logs.info("**********Item_added_to_Cart**********")
        prod.cart().click()

        def wait_for_page_load(driver):
            WebDriverWait(driver, 20).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )

        #Cart operations
        cart_page_obj = prod.cart_view()
        actual_title = cart_page_obj.get_title().text
        exp_title = "Shopping Cart"
        assert actual_title == exp_title
        wait_for_page_load(driver=self.driver)
        wait.until(EC.visibility_of_element_located(cart_page_obj.subtotal))
        subtotal = cart_page_obj.get_subtotal().text
        total = cart_page_obj.get_total().text
        assert subtotal == total
        cart_page_obj.disc_link().click()
        cart_page_obj.entry_field().send_keys("20poff")
        cart_page_obj.disc_apply_cta().click()
        actual_msg = cart_page_obj.suc_banner().text
        exp_msg = 'You used coupon code "20poff".'
        assert actual_msg == exp_msg
        logs.info("**********Discount_applied**********")
        before_updating_qty_discount_amt = cart_page_obj.discount().text
        cart_page_obj.quantity_filed().send_keys(Keys.DELETE)
        cart_page_obj.quantity_filed().send_keys('4')
        cart_page_obj.update_cart().click()
        wait.until(EC.visibility_of_element_located(cart_page_obj.disc_value))
        after_updating_qty_discount_amt = cart_page_obj.discount().text
        assert before_updating_qty_discount_amt == after_updating_qty_discount_amt
        time.sleep(2)
        cart_page_obj.tax_form().click()
        wait.until(EC.element_to_be_clickable(cart_page_obj.country_dropdown))
        country_selc = Select(cart_page_obj.select_country())
        country_selc.select_by_visible_text('France')
        state = Select(cart_page_obj.select_state())
        state.select_by_visible_text('Finistère')
        cart_page_obj.postal_entry().send_keys('30323')

        #checkout page operations
        checkout = cart_page_obj.go_checkout()
        wait_for_page_load(driver=self.driver)
        wait.until(EC.visibility_of_element_located(checkout.email))
        e = checkout.email_address()
        if e:
            e.send_keys('xyz@d.com')
        else:
            pass

        f = checkout.firstname().get_attribute('value')
        if f:
            pass
        else:
            checkout.firstname().send_keys('test')

        l = checkout.lastname().get_attribute('value')
        if l:
            pass
        else:
            checkout.lastname().send_keys('user')

        checkout.street_address().send_keys('123 Near store')
        checkout.city_t().send_keys('ABCD')
        s = checkout.state().get_attribute('value')
        if s:
            pass
        else:
            state_entry = Select(checkout.state())
            state_entry.select_by_visible_text('Ohio')

        p = checkout.postal_code().get_attribute('value')
        if p:
            pass
        else:
            checkout.postal_code().send_keys('22032')

        checkout.telephone().send_keys('4034359384')
        wait.until(EC.element_to_be_clickable(checkout.next_cta))
        checkout.next_button().click()
        wait_for_page_load(driver=self.driver)
        wait.until(EC.invisibility_of_element_located(checkout.main_loader))
        wait.until(EC.invisibility_of_element_located(checkout.sec_loader))
        wait.until(EC.element_to_be_clickable(checkout.place_o))
        element = checkout.place_order()
        self.driver.execute_script("arguments[0].click();", element)
        wait_for_page_load(driver=self.driver)
        wait.until(EC.presence_of_element_located(checkout.msg))
        order_success_msg = checkout.success_msg().text
        assert order_success_msg == 'Thank you for your purchase!'
        logs.info("**********Order_placed_successfully**********")
