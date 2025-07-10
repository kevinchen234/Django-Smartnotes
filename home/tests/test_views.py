import pytest
from django.contrib.auth.models import User


def test_home_endpoint_returns_welcome_page(client):
    """
    Test the home view to ensure it returns a 200 status code.
    """
    response = client.get(path="/home/")
    assert response.status_code == 200
    assert "Welcome to SmartNotes" in str(response.content)


def test_signup_endpoint_returns_form_for_unauthenticated_user(client):
    """
    Test the signup view to ensure it returns a 200 status code.
    """
    response = client.get(path="/signup/")
    assert 200 == response.status_code
    assert "home/register.html" in response.template_name


@pytest.mark.django_db
def test_signup_endpoint_redirects_authenticated_user(client):
    """
    When a user is authenticated and try to access the sign up page
    they are redirected to the notes list page.
    """
    user = User.objects.create_user(username="testuser", password="testpass")
    client.force_login(user=user)
    response = client.get(path="/signup/", follow=False)
    assert 302 == response.status_code
    assert response.url == "/smart/notes/"
