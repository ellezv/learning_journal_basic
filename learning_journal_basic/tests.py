"""Test for views."""
import pytest
from pyramid import testing


@pytest.fixture
def req():
    the_request = testing.DummyRequest()
    return the_request


def test_home_page_has_right_dict(req):
    """My home page view returns some data."""
    from .views import home_list
    response = home_list(req)
    assert "bag_list" in response


def test_home_page_has_iter(req):
    from .views import home_list
    response = home_list(req)
    assert hasattr(response["bag_list"], "__iter__")

@pytest.fixture
def testapp():
    from webtest import TestApp
    from learning_journal_basic import main
    app = main({})
    return TestApp(app)


# def test_home_page_has_list(testapp):
#     response = testapp.get("/", status=200)
#     inner_html = response.inner_html()
#     assert "<li>" in inner_html
