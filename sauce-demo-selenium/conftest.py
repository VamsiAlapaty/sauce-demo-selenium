import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """One browser instance per test, always torn down even if the test fails.
    Runs headless automatically when CI=true (GitHub Actions sets this),
    or when you set HEADLESS=true locally."""
    options = webdriver.ChromeOptions()

    if os.getenv("CI") or os.getenv("HEADLESS"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.implicitly_wait(0)  # we use explicit waits in BasePage instead

    yield drv

    drv.quit()


# Standard Sauce Demo test users - reused across multiple test files
STANDARD_USER = "standard_user"
LOCKED_OUT_USER = "locked_out_user"
PROBLEM_USER = "problem_user"
PERFORMANCE_GLITCH_USER = "performance_glitch_user"
PASSWORD = "secret_sauce"
