from uuid import UUID

from django.db import models


class Question(models.Model):
    text: str = models.TextField()
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text[:50]


class Answer(models.Model):
    question: Question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    user_id: UUID = models.UUIDField()
    text: str = models.TextField()
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Answer {self.id}"
