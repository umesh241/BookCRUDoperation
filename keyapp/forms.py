from django.forms import ModelForm
from keyapp.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['Title', 'Author']
