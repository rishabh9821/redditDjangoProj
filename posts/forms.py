from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):

    class Meta():
        fields = ('title', 'content')
        model = Post
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title',"class": 'postTitleInput'}),
            'content': forms.Textarea(attrs={'class': 'postContentInput'})
        }