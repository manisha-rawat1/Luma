from selenium.webdriver.common.by import By

from Objectrepo.checkout_obj import checkout_obj


class cart_object:
    title = (By.XPATH, "//span[@class='base']")
    subtotal = (By.XPATH, "//tr[@class='totals sub']//td[@class='amount']//span")
    total = (By.XPATH, "//tr[@class='grand totals']//td[@class='amount']")
    discount_link = (By.XPATH, "//div[@id='block-discount']")
    discount_entry_field = (By.XPATH, "//input[@id='coupon_code']")
    apply_cta = (By.XPATH, "//button[@class='action apply primary']")
    success_banner = (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")
    disc_value = (By.XPATH, "//tr[@class='totals']//span[@class='price']")
    qty_field = (By.XPATH, "//input[@class='input-text qty']")
    update_cta = (By.XPATH, "//button[@class='action update']")
    tax_link = (By.XPATH, "//strong[@id='block-shipping-heading']")
    country_dropdown = (By.XPATH, "(//select[@class='select'])[1]")
    state_dropdown = (By.XPATH, "(//select[@class='select'])[2]")
    postal_code_filed = (By.XPATH, "//input[@name='postcode']")
    best_way = (By.XPATH, "//input[@name='ko_unique_1']")
    flat_rate = (By.XPATH, "//input[@name='ko_unique_2']")
    checkout_cta = (By.XPATH, "//button[@data-role = 'proceed-to-checkout']")

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(*cart_object.title)

    def get_subtotal(self):
        return self.driver.find_element(*cart_object.subtotal)

    def get_total(self):
        return self.driver.find_element(*cart_object.total)

    def disc_link(self):
        return self.driver.find_element(*cart_object.discount_link)

    def entry_field(self):
        return self.driver.find_element(*cart_object.discount_entry_field)

    def disc_apply_cta(self):
        return self.driver.find_element(*cart_object.apply_cta)

    def suc_banner(self):
        return self.driver.find_element(*cart_object.success_banner)

    def discount(self):
        return self.driver.find_element(*cart_object.disc_value)

    def quantity_filed(self):
        return self.driver.find_element(*cart_object.qty_field)

    def update_cart(self):
        return self.driver.find_element(*cart_object.update_cta)

    def tax_form(self):
        return self.driver.find_element(*cart_object.tax_link)

    def select_country(self):
        return self.driver.find_element(*cart_object.country_dropdown)

    def select_state(self):
        return self.driver.find_element(*cart_object.state_dropdown)

    def postal_entry(self):
        return self.driver.find_element(*cart_object.postal_code_filed)

    def go_checkout(self):
        self.driver.find_element(*cart_object.checkout_cta).click()
        checkout = checkout_obj(self.driver)
        return checkout

