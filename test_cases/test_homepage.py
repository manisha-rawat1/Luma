from selenium.webdriver import Keys
from Objectrepo.homepage_obj import home_obj
from utilities.Baseclass import Baseclass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Test_hotseller_items_selection(Baseclass):

    def test_add_hotseller_item(self):
        homepage = home_obj(self.driver)
        self.driver.execute_script("window.scrollBy(0, 1600)", " ")
        actual_title = homepage.title_hotseller().text
        expected_title = 'Hot Sellers'
        assert actual_title == expected_title
        hotseller_items = homepage.hotseller_items()
        index = 1
        expected_item = 'Breathe-Easy Tank'
        for item in hotseller_items:
            if item.text == expected_item:
                return index
            else:
                index = index + 1

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_all_elements_located(homepage.all_size))
        sizes = homepage.sizes()
        for size in sizes:
            if size.text == "M":
                size.click()

        homepage.one_color().click()
        homepage.add_to_bag_cta(index).click()

    def test_verify_item_added_to_cart(self):
        homepage = home_obj(self.driver)
        expected_item = 'Breathe-Easy Tank'
        exp_success_msg = 'You added ' + expected_item + ' to your shopping cart.'
        actual_msg = homepage.successmsg().text
        assert actual_msg == exp_success_msg
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(homepage.cart))
        action = ActionChains(self.driver)
        action.move_to_element(homepage.cart_icon()).click().perform()
        prod_added_cart = homepage.item_added().text
        assert prod_added_cart == expected_item

    def test_update_prod_pgo_checkout(self):
        homepage = home_obj(self.driver)
        homepage.qty_field().send_keys(Keys.BACKSPACE)
        homepage.qty_field().send_keys('4')
        homepage.update_qty().click()
        homepage.check_out_cta().click()
