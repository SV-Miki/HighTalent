import logging
import uuid

import pytest
from rest_framework.response import Response
from rest_framework.test import APIClient

from questions.models import Answer, Question

logger = logging.getLogger(__name__)


@pytest.mark.django_db
def test_create_answer(api_client: APIClient, create_question: Question) -> None:
    # Arrange
    url: str = f"/questions/{create_question.id}/answers/"
    payload: dict = {"user_id": str(uuid.uuid4()), "text": "Answer via API"}

    # Act
    response: Response = api_client.post(url, payload, format="json")
    logger.info(f"POST {url} -> {response.status_code}")

    # Assert
    assert response.status_code == 201
    assert Answer.objects.count() == 1


@pytest.mark.django_db
def test_get_answer(api_client: APIClient, create_answer: Answer) -> None:
    # Arrange
    url: str = f"/answers/{create_answer.id}/"

    # Act
    response: Response = api_client.get(url)
    logger.info(f"GET {url} -> {response.status_code}, text={response.data['text']}")

    # Assert
    assert response.status_code == 200
    assert response.data["text"] == "Test answer"


@pytest.mark.django_db
def test_delete_answer(api_client: APIClient, create_answer: Answer) -> None:
    # Arrange
    url: str = f"/answers/{create_answer.id}/"

    # Act
    response: Response = api_client.delete(url)
    logger.info(f"DELETE {url} -> {response.status_code}")

    # Assert
    assert response.status_code in (204, 200)
    assert Answer.objects.count() == 0
