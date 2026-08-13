from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def get_item_count(self):
        return len(self.find_all(self.CART_ITEMS))

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
