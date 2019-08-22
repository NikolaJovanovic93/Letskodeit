import pytest
from base.webdriverfactory import WebDriverFactory


@pytest.yield_fixture()
def setup():
    print("This will run before each method")
    yield
    print("This will run after each method")


@pytest.yield_fixture(scope="class")
def onetimesetup(request, browser):
    print("This will run once at the start of test")
    wdf = WebDriverFactory(browser)
    driver = wdf.getwebdriverinstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("This will run once at the end of test")


def pytest_addoption(parser):
    parser.addoption("--browser", help="Chose browser type on witch you want to run test")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")




























