from rest_framework import generics
from rest_framework.exceptions import NotFound

from .models import Answer, Question
from .serializers import AnswerSerializer, QuestionSerializer


class QuestionListCreateView(generics.ListCreateAPIView):
    queryset: Question = Question.objects.all().order_by("-created_at")
    serializer_class = QuestionSerializer


class QuestionRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset: Question = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerCreateForQuestionView(generics.CreateAPIView):
    serializer_class = AnswerSerializer

    def perform_create(self, serializer: AnswerSerializer) -> None:
        question_id: int = self.kwargs.get("question_id")
        try:
            question: Question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise NotFound("Question does not exist")
        serializer.save(question=question)


class AnswerRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset: Answer = Answer.objects.all()
    serializer_class = AnswerSerializer
