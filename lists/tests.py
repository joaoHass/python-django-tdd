from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

# utilizes the django.test.Client fixture from pytest-django
# see: https://pytest-django.readthedocs.io/en/latest/helpers.html#client-django-test-client
def test_home_page_returns_correct_html(client):
    response_html = client.get('/').content.decode('utf8')
    
    assert '<title>To-Do Lists</title>' in response_html
    assert response_html.startswith('<html>')
    assert response_html.endswith('</html>')
    
