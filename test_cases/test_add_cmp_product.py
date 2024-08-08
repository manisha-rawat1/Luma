import time

import pytest
from selenium.webdriver import Keys
from Objectrepo.product_page_obj import prod_page_obj
from utilities.Baseclass import Baseclass
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_add_cmp_prod(Baseclass):
    logs = Baseclass.logger()

    @pytest.mark.regression
    def test_search_cmp_products(self):
        self.logs.info("**********Search_cmp_Testcase_execution_started**********")
        prod = prod_page_obj(self.driver)
        prod.search_item_field().send_keys('Jackets')
        prod.search_item_field().send_keys(Keys.ENTER)
        prod.select_product().click()
        prod.main_prod().click()
        self.logs.info("**********Fist_Product_added_to_Cmp_list**********")
        actual_msg = prod.success_msg().text
        expected_msg = 'You added product Jade Yoga Jacket to the comparison list.'
        assert actual_msg == expected_msg

        elements = prod.prod_list()
        index = 1
        for element in elements:
            if element.text == 'Phoebe Zipper Sweatshirt':
                break
            else:
                index = index + 1

        prod.prod_two(index).click()
        self.logs.info("**********Second_prod_added_to_cmp_list**********")
        actual_msg = prod.success_msg().text
        expected_msg = 'You added product Phoebe Zipper Sweatshirt to the comparison list.'
        assert actual_msg == expected_msg
        prod.list_cmp().click()
        prod.remove().click()

        #for getting current window handle
        main_window = self.driver.current_window_handle

        #for switching window handle to current window
        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(prod.ok_cta))

        prod.conf_popup().click()

        #for switching back to main window
        self.driver.switch_to.window(main_window)
        self.logs.info("**********Cmp_done**********")
        #prod.wishlist().click()

    def test_select_category_nav_bar(self):
        prod = prod_page_obj(self.driver)
        self.logs.info("**********Nav_bar_execution_started**********")
        all_category = prod.nav_bar_selection()

        action = ActionChains(self.driver)

        for category in all_category:
            if category.text == 'Women':
                action.move_to_element(category)
                action.move_to_element(prod.sub_menu())
                action.move_to_element(prod.sub_menu_item()).click()
                action.perform()
                break

        all_women_items = prod.women_pcp_items()

        for item in all_women_items:
            if item.text == 'Cora Parachute Pant':
                item.click()
                break

        prod.size_selection().click()
        prod.color_selection().click()
        prod.qty_select().clear()
        prod.qty_select().send_keys('2')
        prod.add_tocart().click()
        time.sleep(4)
        actual_msg = prod.success_msg().text
        expected_msg = 'You added Cora Parachute Pant to your shopping cart.'
        assert actual_msg == expected_msg
        self.logs.info("**********Nav_execution_success**********")
