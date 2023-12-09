from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page
from pytest_django.asserts import assertTemplateUsed, assertContains


# utilizes the django.test.Client fixture from pytest-django
# see: https://pytest-django.readthedocs.io/en/latest/helpers.html#client-django-test-client
def test_home_page_returns_correct_html(client):
    response = client.get('/')
    response_html = response.content.decode('utf8').strip()
    
    assert '<title>To-Do Lists</title>' in response_html
    assert response_html.startswith('<html>') or response_html.startswith('<!DOCTYPE html>')
    assert response_html.endswith('</html>')
    assertTemplateUsed(response, 'home.html')
    
    
def test_can_save_a_POST_request(client):
    response = client.post('/', data={'new-item-input': 'A new list item'})

    assertContains(response, 'A new list item')
    assertTemplateUsed(response, 'home.html')

