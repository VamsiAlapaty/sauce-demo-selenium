from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from conftest import STANDARD_USER, PASSWORD


def _login(driver):
    LoginPage(driver).load().login(STANDARD_USER, PASSWORD)
    return InventoryPage(driver)


def test_add_single_item_updates_cart_badge(driver):
    inventory_page = _login(driver)

    inventory_page.add_item_to_cart_by_name("Sauce Labs Backpack")

    assert inventory_page.get_cart_count() == 1


def test_add_multiple_items_updates_cart_badge(driver):
    inventory_page = _login(driver)

    inventory_page.add_item_to_cart_by_name("Sauce Labs Backpack")
    inventory_page.add_item_to_cart_by_name("Sauce Labs Bike Light")
    inventory_page.add_item_to_cart_by_name("Sauce Labs Bolt T-Shirt")

    assert inventory_page.get_cart_count() == 3


def test_cart_page_shows_added_items(driver):
    inventory_page = _login(driver)
    inventory_page.add_item_to_cart_by_name("Sauce Labs Backpack")
    inventory_page.add_item_to_cart_by_name("Sauce Labs Bike Light")

    inventory_page.go_to_cart()
    cart_page = CartPage(driver)

    assert cart_page.get_item_count() == 2
