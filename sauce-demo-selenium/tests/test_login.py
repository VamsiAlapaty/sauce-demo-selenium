import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from conftest import STANDARD_USER, LOCKED_OUT_USER, PROBLEM_USER, PERFORMANCE_GLITCH_USER, PASSWORD


def test_login_with_standard_user(driver):
    login_page = LoginPage(driver).load()
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()
    assert inventory_page.get_page_title() == "Products"


def test_login_with_invalid_password(driver):
    login_page = LoginPage(driver).load()
    login_page.login(STANDARD_USER, "wrong_password")

    assert "do not match" in login_page.get_error_message().lower()


def test_login_with_locked_out_user(driver):
    login_page = LoginPage(driver).load()
    login_page.login(LOCKED_OUT_USER, PASSWORD)

    assert "locked out" in login_page.get_error_message().lower()


@pytest.mark.parametrize(
    "username",
    [STANDARD_USER, PROBLEM_USER, PERFORMANCE_GLITCH_USER],
    ids=["standard_user", "problem_user", "performance_glitch_user"],
)
def test_login_succeeds_for_valid_user_types(driver, username):
    """Data-driven: adding a new valid user type later means adding one
    line to the list above, not writing a new test function."""
    login_page = LoginPage(driver).load()
    login_page.login(username, PASSWORD)

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()
