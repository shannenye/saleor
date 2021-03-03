from urllib.parse import urlencode

import pytest
from django.core.exceptions import ValidationError

from ..utils.url import APPURLValidator, prepare_url


def test_prepare_url():
    redirect_url = "https://www.example.com"
    params = urlencode({"param1": "abc", "param2": "xyz"})
    result = prepare_url(params, redirect_url)
    assert result == f"{redirect_url}?param1=abc&param2=xyz"


def test_validate_url():
    url_validator = APPURLValidator()
    url = "http://otherapp:3000"
    assert url_validator(url) is None


def test_validate_invalid_url():
    url_validator = APPURLValidator()
    url = "otherapp:3000"
    with pytest.raises(ValidationError):
        url_validator(url)
