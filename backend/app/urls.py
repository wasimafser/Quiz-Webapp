from django.urls import path
from .views import QuizView, IndexRedirect, GenerateQuestionsView

urlpatterns = [
    path('', IndexRedirect.as_view(), name='index'),
    path('quiz/', QuizView.as_view(), name='quiz_view'),
    path('generate_questions/', GenerateQuestionsView.as_view(), name='generate_questions')
]
