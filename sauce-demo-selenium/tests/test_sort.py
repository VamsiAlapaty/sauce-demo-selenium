import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from conftest import STANDARD_USER, PASSWORD


def _login(driver):
    LoginPage(driver).load().login(STANDARD_USER, PASSWORD)
    return InventoryPage(driver)


@pytest.mark.parametrize(
    "sort_value,expected_order_desc",
    [
        ("az", "name ascending"),
        ("za", "name descending"),
        ("lohi", "price ascending"),
        ("hilo", "price descending"),
    ],
)
def test_sort_options_change_order(driver, sort_value, expected_order_desc):
    inventory_page = _login(driver)

    inventory_page.sort_by(sort_value)

    if sort_value == "az":
        names = inventory_page.get_item_names()
        assert names == sorted(names)
    elif sort_value == "za":
        names = inventory_page.get_item_names()
        assert names == sorted(names, reverse=True)
    elif sort_value == "lohi":
        prices = inventory_page.get_item_prices()
        assert prices == sorted(prices)
    elif sort_value == "hilo":
        prices = inventory_page.get_item_prices()
        assert prices == sorted(prices, reverse=True)
