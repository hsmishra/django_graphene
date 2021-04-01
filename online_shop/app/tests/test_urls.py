from django.urls import reverse, resolve
from django.contrib.auth import get_user_model

import pytest

from app.views import home


class TestUrls:

    def test_home_url(self):
        path = reverse('home')
        assert resolve(path).view_name == "home"

    # @pytest.mark.parametrize('param', [('home'),])
    # def test_render_views(client, param):
    #     temp_url = reverse(home)
    #     resp = client.get(temp_url)
    #     assert resp.status_code == 200