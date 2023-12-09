from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page
from lists.models import Item
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


def test_saving_and_retrieving_items(db):
    first_item = Item()
    first_item.text = 'The first list item'
    first_item.save()
    
    second_item = Item()
    second_item.text = 'Item, the second'
    second_item.save()
    
    saved_items = Item.objects.all()
    assert saved_items.count() == 2
    
    first_saved_item = saved_items[0]
    second_saved_item = saved_items[1]
    
    assert first_saved_item.text == 'The first list item'
    assert second_saved_item.text == 'Item, the second'