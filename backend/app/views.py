from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.core import serializers

from .models import Question, Answer
from .forms import QuestionForm

# Create your views here.


class IndexRedirect(View):
    def get(self, request):
        return redirect('quiz_view')


class QuizView(View):
    template_name = 'app/quiz.html'

    def get(self, request, *args, **kwargs):
        questions = []
        for question in Question.objects.all().order_by('level'):
            questions.append({
                'id': question.id,
                'question': question.text,
                'answer_choices': list(question.answers.all().values('id', 'text', 'is_answer')),
                'score': question.score,
                'level': question.level,
                'form': QuestionForm(initial=question).as_p()
            })
        context = {
            'questions': questions,
        }
        return render(request, self.template_name, context=context)


class GenerateQuestionsView(View):

    def get(self, request):
        from .scripts import generate_questions
        generate_questions.generate_questions()
        return HttpResponse("Done")