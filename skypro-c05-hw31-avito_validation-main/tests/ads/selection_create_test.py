import pytest


@pytest.mark.django_db
def test_selection_create(client, user_token, user, ad):

    data = {
        "owner": user.id,
        "name": "Test selection",
        "items": [ad.id]
    }

    expected_response = {
        "id": 1,
        "owner": user.id,
        "name": "Test selection",
        "items": [ad.id]
    }

    response = client.post(
        "/selection/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION='Bearer ' + user_token
    )

    assert response.status_code == 201
    assert response.data == expected_response
