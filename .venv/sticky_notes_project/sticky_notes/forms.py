from django import forms
from .models import StickyNote

class StickyNoteForm(forms.ModelForm):
    """
    Provides a form with fields 'title', 'content', and 'color'
    to create or edit a StickyNote.

    Methods:
        __init__: Initializes the form with color choices for the 'color' field.
    """

    class Meta:
        model = StickyNote
        fields = ['title', 'content', 'color']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        color_choices = StickyNote._meta.get_field('color').choices
        self.fields['color'].widget = forms.Select(choices=color_choices)

