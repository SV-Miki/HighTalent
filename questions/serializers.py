from uuid import UUID

from rest_framework import serializers

from .models import Answer, Question
from .validators import validate_non_empty_text, validate_uuid


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "question", "user_id", "text", "created_at"]
        read_only_fields = ["id", "created_at", "question"]

    def validate_text(self, value: str) -> str:
        return validate_non_empty_text(value, "Answer text")

    def validate_user_id(self, value: str | UUID) -> UUID:
        return validate_uuid(value, "User ID")


class QuestionSerializer(serializers.ModelSerializer):
    answers: list[AnswerSerializer] = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "text", "created_at", "answers"]

    def validate_text(self, value: str) -> str:
        return validate_non_empty_text(value, "Question text")
