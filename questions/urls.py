from django.urls import path

from .views import (AnswerCreateForQuestionView, AnswerRetrieveDestroyView,
                    QuestionListCreateView, QuestionRetrieveDestroyView)

urlpatterns = [
    path("questions/", QuestionListCreateView.as_view()),
    path("questions/<int:pk>/", QuestionRetrieveDestroyView.as_view()),
    path("questions/<int:question_id>/answers/", AnswerCreateForQuestionView.as_view()),
    path("answers/<int:pk>/", AnswerRetrieveDestroyView.as_view()),
]
