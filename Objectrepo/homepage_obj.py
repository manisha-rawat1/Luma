from selenium.webdriver.common.by import By


class home_obj:
    sign_up_link = (By.XPATH, "//div[@class='panel header']//a[text() = 'Create an Account']")
    sign_in_link = (By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]")
    hotseller_title = (By.XPATH, "//h2[@class='title']")
    all_hotseller_items = (By.XPATH, "//div[@class='block widget block-products-list grid']")
    all_size = (By.XPATH, "//div[@class='swatch-opt-1812']//div[@class='swatch-option text']")
    color = (By.XPATH, "//div[@class='swatch-opt-1812']//div[@id='option-label-color-93-item-57']")
    success_msg = (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")
    cart = (By.XPATH, "//a[@class='action showcart']//span[@class='counter qty']")
    added_prod = (By.XPATH, "//a[@data-bind='attr: {href: product_url}, html: product_name']")
    prod_quant = (By.XPATH, "//input[@class='item-qty cart-item-qty']")
    update_cta = (By.XPATH, "//button[@class='update-cart-item']")
    checkout_cta = (By.XPATH, "//button[@id='top-cart-btn-checkout']")

    def __init__(self, driver):
        self.driver = driver

    def get_index(self, index):
        xpath = f"(//button[@class='action tocart primary'])[{index}]"
        return xpath

    def title_hotseller(self):
        return self.driver.find_element(*home_obj.hotseller_title)

    def hotseller_items(self):
        return self.driver.find_elements(*home_obj.all_hotseller_items)

    def sizes(self):
        return self.driver.find_elements(*home_obj.all_size)

    def one_color(self):
        return self.driver.find_element(*home_obj.color)

    def add_to_bag_cta(self, index):
        xpath = self.get_index(index)
        ele = (By.XPATH, xpath)
        return self.driver.find_element(*ele)

    def successmsg(self):
        return self.driver.find_element(*home_obj.success_msg)

    def cart_icon(self):
        return self.driver.find_element(*home_obj.cart)

    def item_added(self):
        return self.driver.find_element(*home_obj.added_prod)

    def qty_field(self):
        return self.driver.find_element(*home_obj.prod_quant)

    def update_qty(self):
        return self.driver.find_element(*home_obj.update_cta)

    def check_out_cta(self):
        return self.driver.find_element(*home_obj.checkout_cta)
