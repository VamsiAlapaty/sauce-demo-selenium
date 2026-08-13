# Sauce Demo — Selenium + pytest Automation Suite

![Tests](https://github.com/YOUR_USERNAME/sauce-demo-selenium/actions/workflows/tests.yml/badge.svg)

End-to-end UI test automation for [saucedemo.com](https://www.saucedemo.com/), built with
Selenium WebDriver, pytest, and the Page Object Model. First pass of a two-pass portfolio
project (Selenium now, Playwright rebuild next).

## Stack
- Python 3.11
- Selenium 4
- pytest
- webdriver-manager (auto-installs the matching ChromeDriver — no manual driver downloads)
- GitHub Actions for CI

## Project structure
```
pages/              # Page Object Model — one class per page, no assertions here
  base_page.py       # shared wait/click/type helpers
  login_page.py
  inventory_page.py
  cart_page.py
  checkout_page.py
tests/              # test files — assertions live here, not in page objects
  test_login.py
  test_cart.py
  test_checkout.py
  test_sort.py
conftest.py         # driver fixture (setup/teardown) + shared test data
.github/workflows/  # CI pipeline definition
```

## Running locally
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

pytest                          # runs with a visible browser
HEADLESS=true pytest            # runs headless, same as CI
pytest -v                       # verbose output
pytest tests/test_login.py      # run a single file
```

## Design notes
- **Page Object Model**: tests never call Selenium directly — they call methods on page
  objects (`login_page.login(...)`, `inventory_page.add_item_to_cart_by_name(...)`). If
  Sauce Demo changes a locator, exactly one file changes, not every test.
- **Explicit waits only**: `BasePage` wraps `WebDriverWait` + `expected_conditions`.
  No `time.sleep()` anywhere in this repo — sleep-based waits are the #1 cause of flaky
  suites and the fastest way to lose credibility in an interview.
- **Data-driven tests**: `@pytest.mark.parametrize` covers all Sauce Demo user types and
  sort options from single test functions instead of copy-pasted near-duplicates.
- **Fixture-managed browser lifecycle**: `driver` fixture in `conftest.py` guarantees
  `driver.quit()` runs even when a test fails, so failures don't leak Chrome processes in CI.

## Build log / milestones
- [x] Environment + first passing login test
- [x] Page Object Model structure
- [x] Core flows: login (valid/invalid/locked-out), cart, checkout, sort
- [x] pytest fixtures + parametrized data-driven tests
- [x] GitHub Actions CI on every push
- [ ] Playwright rebuild (pass two)

## Next: Playwright pass
Same test scenarios, rebuilt in Playwright's sync API, to demonstrate framework range —
Selenium is still the enterprise standard, Playwright is where new hiring demand is
concentrated.
