import pytest

from django.contrib.auth.models import User
from notes.models import Notes
from .factories import UserFactory, NoteFactory


@pytest.fixture
def logged_user(client):
    user = UserFactory()
    client.force_login(user=user)
    return user


@pytest.mark.django_db
def test_list_endpoint_return_user_notes(client, logged_user):
    note = NoteFactory(user=logged_user)
    note2 = NoteFactory(user=logged_user)

    response = client.get(path="/smart/notes/")
    assert 200 == response.status_code
    content = str(response.content)
    assert note.title in content
    assert note2.title in content
    assert 2 == content.count("<h3>")


@pytest.mark.django_db
def test_list_endpoint_only_list_notes_from_authenticated_user(client, logged_user):
    john = UserFactory(username="john")
    john_note = NoteFactory(user=john)
    note = NoteFactory(user=logged_user)
    note2 = NoteFactory(user=logged_user)

    response = client.get(path="/smart/notes/")
    assert 200 == response.status_code
    content = str(response.content)
    assert note.title in content
    assert note2.title in content
    assert john_note.title not in content
    assert 2 == content.count("<h3>")


@pytest.mark.django_db
def test_create_endpoint_receives_form_data(client, logged_user):
    form_data = {
        "title": "Django Test Note",
        "text": "This is a test note.",
    }
    response = client.post(path="/smart/notes/new/", data=form_data, follow=True)
    assert 200 == response.status_code
    assert "notes/notes_list.html" in response.template_name
    assert 1 == logged_user.notes.count()
    assert "Django Test Note" in logged_user.notes.first().title
