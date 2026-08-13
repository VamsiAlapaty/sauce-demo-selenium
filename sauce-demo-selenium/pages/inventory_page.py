from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def is_loaded(self):
        return "inventory.html" in self.driver.current_url

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def add_item_to_cart_by_name(self, item_name):
        # Sauce Demo builds add-to-cart button ids from the product name,
        # e.g. "Sauce Labs Backpack" -> add-to-cart-sauce-labs-backpack
        slug = item_name.lower().replace(" ", "-")
        locator = (By.ID, f"add-to-cart-{slug}")
        self.click(locator)

    def get_cart_count(self):
        if not self.is_visible(self.CART_BADGE):
            return 0
        return int(self.get_text(self.CART_BADGE))

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def sort_by(self, option_value):
        from selenium.webdriver.support.ui import Select
        dropdown = self.find(self.SORT_DROPDOWN)
        Select(dropdown).select_by_value(option_value)

    def get_item_names(self):
        elements = self.find_all(self.ITEM_NAME)
        return [el.text for el in elements]

    def get_item_prices(self):
        elements = self.find_all(self.ITEM_PRICE)
        return [float(el.text.replace("$", "")) for el in elements]
