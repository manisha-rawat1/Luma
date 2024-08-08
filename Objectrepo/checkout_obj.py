from selenium.webdriver.common.by import By


class checkout_obj:

    first_name = (By.XPATH, "//input[@name ='firstname']")
    last_name = (By.XPATH, "//input[@name ='lastname']")
    email = (By.XPATH, "//div[@class='control _with-tooltip']//input[@type='email']")
    address = (By.XPATH, "//input[@name ='street[0]']")
    city = (By.XPATH, "//input[@name ='city']")
    state_dropdown = (By.XPATH, "(//select[@class='select'])[1]")
    postal_code_filed = (By.XPATH, "//input[@name='postcode']")
    country_dropdown = (By.XPATH, "(//select[@class='select'])[2]")
    phone = (By.XPATH, "//input[@name='telephone']")
    shipping_method = (By.XPATH, "//input[@class='radio']")
    next_cta = (By.XPATH, "//button[@class='button action continue primary']")
    place_o = (By.XPATH, "//span[normalize-space()='Place Order']")
    msg = (By.XPATH, "//span[@class='base']")
    main_loader = (By.XPATH, "//div[@id='checkout-loader']//div[@class='loader']")
    sec_loader = (By.XPATH, "//div[@class='loading-mask']//p")

    def __init__(self, driver):
        self.driver = driver

    def firstname(self):
        return self.driver.find_element(*checkout_obj.first_name)

    def lastname(self):
        return self.driver.find_element(*checkout_obj.last_name)

    def street_address(self):
        return self.driver.find_element(*checkout_obj.address)

    def city_t(self):
        return self.driver.find_element(*checkout_obj.city)

    def state(self):
        return self.driver.find_element(*checkout_obj.state_dropdown)

    def postal_code(self):
        return self.driver.find_element(*checkout_obj.postal_code_filed)

    def country(self):
        return self.driver.find_element(*checkout_obj.country_dropdown)

    def telephone(self):
        return self.driver.find_element(*checkout_obj.phone)

    def next_button(self):
        return self.driver.find_element(*checkout_obj.next_cta)

    def email_address(self):
        return self.driver.find_element(*checkout_obj.email)

    def shipping(self):
        return self.driver.find_elements(*checkout_obj.shipping_method)

    def place_order(self):
        return self.driver.find_element(*checkout_obj.place_o)

    def success_msg(self):
        return self.driver.find_element(*checkout_obj.msg)
