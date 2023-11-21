from django.forms import ModelForm
from .models import Role, Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
            'dia',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
            'dia': 'Data',
        }
