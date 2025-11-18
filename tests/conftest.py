import logging
import uuid

import pytest
from rest_framework.test import APIClient

from questions.models import Answer, Question

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


@pytest.fixture
def create_question() -> Question:
    question: Question = Question.objects.create(text="Test question")
    logger.info(f"Created question: {question.id} - {question.text}")
    return question


@pytest.fixture
def create_answer(create_question) -> Answer:
    answer: Answer = Answer.objects.create(
        question=create_question, user_id=uuid.uuid4(), text="Test answer"
    )
    logger.info(f"Created answer: {answer.id} for question {create_question.id}")
    return answer


@pytest.fixture
def api_client() -> APIClient:

    client: APIClient = APIClient()
    logger.info("API client initialized")
    return client
