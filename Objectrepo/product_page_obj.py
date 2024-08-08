from selenium.webdriver.common.by import By

from Objectrepo.cart_obj import cart_object


class prod_page_obj:
    search_box = (By.XPATH, "//input[@id='search']")
    pcp_select_prod = (By.XPATH, "//a[@class='product-item-link']")
    add_to_cmp = (By.XPATH, "//div[@class='product-addto-links']//a[@class='action tocompare']")
    success_banner = (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")
    other_prods = (By.XPATH, "//a[@class='product-item-link']")
    cmp_list = (By.XPATH, "//a[text()='comparison list']")
    close_icon = (By.XPATH, "(//a[@class='action delete'])[2]")
    ok_cta = (By.XPATH, "//button[@class='action-primary action-accept']")
    fav = (By.XPATH, "//a[@class='action towishlist']")
    nav_bar = (By.XPATH, "//a[@class='level-top ui-corner-all']")
    submenu = (By.XPATH, "//li[@class='level1 nav-2-2 category-item last parent ui-menu-item']")
    submenu_prod = (By.XPATH, "//a[@id='ui-id-15']")
    women_pcp = (By.XPATH, "//a[@class='product-item-link']")
    size_select = (By.XPATH, "//div[@id='option-label-size-143-item-171']")
    color_select = (By.XPATH, "//div[@id='option-label-color-93-item-50']")
    qty = (By.XPATH, "//input[@id='qty']")
    add_to_cart = (By.XPATH, "//button[@id='product-addtocart-button']")

    gear_cat_nav = (By.XPATH, "//a[@id='ui-id-6']")
    watches_filter = (By.XPATH, "//a[contains(text(),'Watches')]")
    gender_select = (By.XPATH, "//div[normalize-space()='Gender']")
    side_bar_cat = (By.XPATH, "//a[contains(text(),'Women')]")
    watches_items = (By.XPATH, "//a[@class='product-item-link']")
    cart_icon = (By.XPATH, "//div[@class='minicart-wrapper']//span[@class='counter qty']")
    view_cart_link = (By.XPATH, "//a[@class='action viewcart']")

    @staticmethod
    def sec_prod(index):
        xpath = f"(//a[@title='Add to Compare'])[{index}]"
        return xpath

    def __init__(self, driver):
        self.driver = driver

    def search_item_field(self):
        return self.driver.find_element(*prod_page_obj.search_box)

    def select_product(self):
        return self.driver.find_element(*prod_page_obj.pcp_select_prod)

    def main_prod(self):
        return self.driver.find_element(*prod_page_obj.add_to_cmp)

    def success_msg(self):
        return self.driver.find_element(*prod_page_obj.success_banner)

    def prod_list(self):
        return self.driver.find_elements(*prod_page_obj.other_prods)

    def prod_two(self, index):
        xpath = self.sec_prod(index)
        ele_xpath = (By.XPATH, xpath)
        return self.driver.find_element(*ele_xpath)

    def list_cmp(self):
        return self.driver.find_element(*prod_page_obj.cmp_list)

    def remove(self):
        return self.driver.find_element(*prod_page_obj.close_icon)

    def conf_popup(self):
        return self.driver.find_element(*prod_page_obj.ok_cta)

    def wishlist(self):
        return self.driver.find_element(*prod_page_obj.fav)

    def nav_bar_selection(self):
        return self.driver.find_elements(*prod_page_obj.nav_bar)

    def sub_menu(self):
        return self.driver.find_element(*prod_page_obj.submenu)

    def sub_menu_item(self):
        return self.driver.find_element(*prod_page_obj.submenu_prod)

    def women_pcp_items(self):
        return self.driver.find_elements(*prod_page_obj.women_pcp)

    def size_selection(self):
        return self.driver.find_element(*prod_page_obj.size_select)

    def color_selection(self):
        return self.driver.find_element(*prod_page_obj.color_select)

    def qty_select(self):
        return self.driver.find_element(*prod_page_obj.qty)

    def add_tocart(self):
        return self.driver.find_element(*prod_page_obj.add_to_cart)

    @staticmethod
    def add_cta(ind):
        xpath = f"(//span[contains(text(),'Add to Cart')])[{ind}]"
        return xpath

    @staticmethod
    def item_cont(ind):
        xpath = f"(//div[@class='price-box price-final_price'])[{ind}]"
        return xpath

    def nav(self):
        return self.driver.find_element(*prod_page_obj.gear_cat_nav)

    def side_nav(self):
        return self.driver.find_element(*prod_page_obj.watches_filter)

    def gender_cat(self):
        return self.driver.find_element(*prod_page_obj.gender_select)

    def gender(self):
        return self.driver.find_element(*prod_page_obj.side_bar_cat)

    def product_list(self):
        return self.driver.find_elements(*prod_page_obj.watches_items)

    def price_box(self, ind):
        xpath = self.item_cont(ind)
        ele = (By.XPATH, xpath)
        return self.driver.find_element(*ele)

    def add_to_bag(self, ind):
        xpath = self.add_cta(ind)
        ele = (By.XPATH, xpath)
        return self.driver.find_element(*ele)

    def cart(self):
        return self.driver.find_element(*prod_page_obj.cart_icon)

    def cart_view(self):
        self.driver.find_element(*prod_page_obj.view_cart_link).click()
        cart = cart_object(self.driver)
        return cart
