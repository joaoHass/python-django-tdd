import pytest
from selenium import webdriver

@pytest.fixture
def setup_data():
    print('Test started')
    browser = webdriver.Firefox()
    
    yield browser
    
    browser.quit()
    print('Test ended')

def test_can_start_a_todo_list(setup_data):
    browser = setup_data
    
    browser.get('http://localhost:8000')
    
    assert 'To-Do' in browser.title