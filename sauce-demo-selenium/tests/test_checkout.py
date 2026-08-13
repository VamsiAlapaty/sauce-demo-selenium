from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from conftest import STANDARD_USER, PASSWORD


def test_complete_checkout_flow_end_to_end(driver):
    # 1. Log in
    LoginPage(driver).load().login(STANDARD_USER, PASSWORD)
    inventory_page = InventoryPage(driver)

    # 2. Add an item and go to cart
    inventory_page.add_item_to_cart_by_name("Sauce Labs Backpack")
    inventory_page.go_to_cart()

    # 3. Proceed to checkout
    cart_page = CartPage(driver)
    cart_page.checkout()

    # 4. Fill shipping info
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_info("Vamsi", "K", "98201")

    # 5. Confirm total is shown, then finish
    assert "Total" in checkout_page.get_total_text()
    checkout_page.finish()

    # 6. Confirm order completion
    assert "Thank you" in checkout_page.get_confirmation_message()
