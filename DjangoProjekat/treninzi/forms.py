from django.forms import ModelForm
from .models import Practice, Comment

class PracticeForm(ModelForm):
    class Meta:
        model = Practice
        fields = ['content']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']