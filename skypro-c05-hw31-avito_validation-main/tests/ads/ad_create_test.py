import pytest


@pytest.mark.django_db
def test_ad_create(client, user, category):

    expected_response = {
        "id": user.id,
        "image": None,
        "name": "Test 10 characters minimum",
        "price": 2500,
        "author": user.username,
        "category": category.name,
        "is_published": False,
        "description": "Test description"
    }

    data = {
        "author_id": user.id,
        "name": "Test 10 characters minimum",
        "price": 2500,
        "description": "Test description",
        "is_published": False,
        "category_id": category.id
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_ad_create_price_less_than_zero(client, user, category):

    expected_response = {
        "price": [
            "Ensure this value is greater than or equal to 0."
        ]
    }

    data = {
        "author_id": user.id,
        "name": "Test 10 characters minimum",
        "price": -1,
        "description": "Test description",
        "is_published": False,
        "category_id": category.id
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.data == expected_response


@pytest.mark.django_db
def test_ad_create_is_published_true(client, user, category):

    expected_response = {
        "is_published": [
            "This field may not be True"
        ]
    }

    data = {
        "author_id": user.id,
        "name": "Test 10 characters minimum",
        "price": 2500,
        "description": "Test description",
        "is_published": True,
        "category_id": category.id
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.data == expected_response


@pytest.mark.django_db
def test_ad_create_name_less_10_chars(client, user, category):

    expected_response = {
        "name": [
            "Ensure this field has at least 10 characters."
        ]
    }

    data = {
        "author_id": user.id,
        "name": "Test",
        "price": 2500,
        "description": "Test description",
        "is_published": False,
        "category_id": category.id
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.data == expected_response
