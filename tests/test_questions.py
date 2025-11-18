import logging
import uuid

import pytest
from rest_framework.response import Response
from rest_framework.test import APIClient

from questions.models import Answer, Question

logger = logging.getLogger(__name__)


@pytest.mark.django_db
def test_create_question(api_client: APIClient) -> None:
    # Arrange
    url: str = "/questions/"
    payload: dict = {"text": "Hello?"}

    # Act
    response: Response = api_client.post(url, payload, format="json")
    logger.info(f"POST {url} -> {response.status_code}")

    # Assert
    assert response.status_code == 201
    assert Question.objects.count() == 1


@pytest.mark.django_db
def test_question_detail_returns_answers(
    api_client: APIClient, create_question: Question
) -> None:
    # Arrange
    answer: Answer = Answer.objects.create(
        question=create_question, user_id=uuid.uuid4(), text="Answer 1"
    )
    url: str = f"/questions/{create_question.id}/"
    logger.info(f"Created answer for question {create_question.id}")

    # Act
    response: Response = api_client.get(url)
    logger.info(
        f"GET {url} -> {response.status_code}, answers={len(response.data['answers'])}"
    )

    # Assert
    assert response.status_code == 200
    assert len(response.data["answers"]) == 1


@pytest.mark.django_db
def test_cascade_delete(api_client: APIClient, create_question: Question) -> None:
    # Arrange
    answer: Answer = Answer.objects.create(
        question=create_question, user_id=uuid.uuid4(), text="A1"
    )
    url: str = f"/questions/{create_question.id}/"
    logger.info(
        f"Before delete: Question count={Question.objects.count()}, Answer count={Answer.objects.count()}"
    )

    # Act
    response: Response = api_client.delete(url)
    logger.info(f"Deleted question {create_question.id}")

    # Assert
    assert Question.objects.count() == 0
    assert Answer.objects.count() == 0
    logger.info("Cascade delete verified")
