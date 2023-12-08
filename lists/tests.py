from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

def test_home_page_returns_correct_html():
    request = HttpRequest()
    
    response = home_page(request)
    html = response.content.decode('utf8')
    
    assert '<title>To-Do Lists</title>' in html
    assert html.startswith('<html>')
    assert html.endswith('</html>')
    
# utilizes the django.test.Client fixture from pytest-django
# see: https://pytest-django.readthedocs.io/en/latest/helpers.html#client-django-test-client
def test_home_page_returns_correct_html2(client):
    assert '<title>To-Do Lists</title>' in client.get('/').content.decode('utf8')
    
