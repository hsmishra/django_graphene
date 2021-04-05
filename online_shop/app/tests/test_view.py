from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer

from app.views import home


class TestView:

    def test_home_page_view(self):
        path = reverse('home')
        request = RequestFactory().get(path)
        
        response = home(request)
        assert response.status_code == 200