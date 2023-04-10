from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given('launch chrome browser')
def launchBrowser(context):
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    context.driver = webdriver.Chrome(executable_path="../../webdrivers/chromedriver_win32/chromedriver.exe", chrome_options=options)


@when('open orangehrm homepage')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then('verify that logo present on that home page')
def verifyLogo(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt='company-branding']")))
    status = context.driver.find_element(By.XPATH, "//img[@alt='company-branding']").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()


@when('then enter username {user} and password {pwd}')
def data_entry(context, user, pwd):
    wait = WebDriverWait(context.driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt='company-branding']")))
    context.driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(user)
    context.driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(pwd)


@when('click on login button')
def click_login(context):
    context.driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()


@then('user must login into the dashboard page')
def check_dashboard(context):
    try:
        wait = WebDriverWait(context.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//h6[contains(.,'Dashboard')]")))
        text = context.driver.find_element(By.XPATH, "//h6[contains(.,'Dashboard')]").text
    except:
        context.driver.close()
        assert False, "Test Failed"

    if text == 'Dashboard':
        context.driver.close()
        assert True, "Test Passed"

@when('then enter valid username and password')
def valid_entry(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt='company-branding']")))
    context.driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("Admin")
    context.driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("admin123")


@when('navigate to search page')
def navigate_to_search(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//h6[contains(.,'Dashboard')]")))
    status = context.driver.find_element(By.XPATH, "//input[@placeholder='Search']").is_displayed()
    assert status is True


@then('search page should display')
def search_results(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("a")
    search_elements = context.driver.find_elements(By.XPATH, "//ul[@class='oxd-main-menu']//li")
    for result in search_elements:
        text = result.find_element(By.XPATH, "//a//span").text
        assert "a" in text.lower(), "Test Passed"
