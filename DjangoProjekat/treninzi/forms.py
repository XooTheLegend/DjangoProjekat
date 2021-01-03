from django.forms import ModelForm
from .models import Practice, Comment

class PracticeForm(ModelForm):
    class Meta:
        model = Practice
        fields = ['type', 'location', 'content', 'rate', 'hours', 'minutes']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']