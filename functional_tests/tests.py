from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import pytest
import time

@pytest.fixture
def setup_data():
    print('Test started')
    browser = webdriver.Firefox()
    
    yield browser
    
    browser.quit()
    print('Test ended')

def test_can_start_a_todo_list(setup_data, live_server):
    browser = setup_data
    
    # Edith has heard about a cool new online to-do app.
    # She goes to check out its homepage
    browser.get(str(live_server.url))
    
    # She notices the page title and header mention to-do lists
    assert 'To-Do' in browser.title
    h1_text = browser.find_element(By.TAG_NAME, 'h1').text
    assert 'To-Do' in h1_text
    
    # She is invited to enter a to-do item straight away
    inputbox = browser.find_element(By.ID, 'idNewItem')
    assert inputbox.get_attribute('placeholder') == 'Enter a To-Do item'
    
    # She types "Buy peacock feathers" into a text box
    # (Edith's hobby is tying fly-fishing lures)
    inputbox.send_keys('Buy peacock feathers')
    
    # When she hits enter, the page updates, and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list table\
    inputbox.send_keys(Keys.ENTER)
    
    wait_for_row_in_table_list(browser, '1: Buy peacock feathers')
    
    # There is still a text box inviting her to add another item.
    # She enters "Use peacock feathers to make a fly"
    # (Edith is very methodical)
    inputbox = browser.find_element(By.ID, "idNewItem")
    inputbox.send_keys("Use peacock feathers to make a fly")
    inputbox.send_keys(Keys.ENTER)
    
    # The page updates again, and now shows both items on her list
    wait_for_row_in_table_list("1: Buy peacock feathers")
    wait_for_row_in_table_list("2: Use peacock feathers to make a fly")
    
def wait_for_row_in_table_list(browser, row_text):
    MAX_WAIT = 5
    start_time = time.time()
    
    while True:
        try:
            table = browser.find_element(By.ID, 'idListTable')
            rows = table.find_elements(By.TAG_NAME, 'tr')

            assert row_text in [row.text for row in rows]
            return
        except (AssertionError, WebDriverException):
            if time.time() - start_time > MAX_WAIT:
                raise
            time.sleep(0.5)