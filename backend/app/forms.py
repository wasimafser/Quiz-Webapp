from django import forms


class QuestionForm(forms.Form):
    answer = forms.ChoiceField(widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__()
        question = kwargs['initial']
        self.fields['answer'].label = question.text
        self.fields['answer'].choices = list(question.answers.all().values_list('id', 'text'))
