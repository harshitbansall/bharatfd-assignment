from unittest.mock import patch

import pytest
from rest_framework.test import APIRequestFactory

from home.models import FAQ
from home.views import FAQView


@pytest.mark.django_db
@patch('django.core.cache.cache.get')
@patch('django.core.cache.cache.set')
def test_get_faq_list(mock_cache_set, mock_cache_get):
    mock_cache_get.return_value = None
    mock_cache_set.return_value = True

    factory = APIRequestFactory()

    FAQ.objects.create(question="Who can open a Fixed Deposit?",
                       answer="Any Indian citizen who is 18 years old or older and has valid identification documents like a PAN card and Aadhaar can open a Fixed Deposit.")
    FAQ.objects.create(question="Can I renew my Fixed Deposit upon maturity?",
                       answer="Yes, most banks offer options to automatically renew your FD for the same tenure upon maturity, unless you choose otherwise.")

    request = factory.get('/faqs')
    view = FAQView.as_view()
    response = view(request)

    assert response.status_code == 200
    assert len(response.data['data']) == 2

    mock_cache_set.assert_called()
    mock_cache_get.assert_called()
