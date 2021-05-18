from django.db import models

# Create your models here.


class Question(models.Model):
    LEVELS = (
        ('easy', 'EASY'),
        ('medium', 'MEDIUM'),
        ('hard', 'HARD')
    )

    text = models.TextField()
    score = models.IntegerField()
    level = models.CharField(choices=LEVELS, max_length=10)

    def __str__(self):
        return f"{self.id} - {self.text} - {self.level}"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=100)
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.id} - {self.text}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question', 'text'], name='unique_answers_for_question'),
        ]
