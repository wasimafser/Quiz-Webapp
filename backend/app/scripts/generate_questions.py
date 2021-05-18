import requests

from django.db import transaction

from app.models import Question, Answer

API_URL = "https://opentdb.com/api.php?amount=30&type=multiple"

def get_score(level):
    if level == 'easy':
        return 10
    elif level == 'medium':
        return 20
    else:
        return 30

def generate_questions():
    response = requests.get(API_URL)
    results = response.json()['results']
    questions = []
    answers = []
    with transaction.atomic():
        for result in results:
            question = Question.objects.create(
                text=result['question'],
                score=get_score(result['difficulty']),
                level=result['difficulty']
            )
            questions.append(question)
            for choice in result['incorrect_answers']:
                answer = Answer(
                    question=question,
                    text=choice,
                    is_answer=False
                )
                answers.append(answer)
            # APPEND CORRECT ANSWER
            answer = Answer(
                question=question,
                text=result['correct_answer'],
                is_answer=True
            )
            answers.append(answer)

    Answer.objects.bulk_create(answers)