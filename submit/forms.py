from django import forms
from .models import Submission

class SubmitForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['fullname', 'email', 'phone', 'paper_name', 'message', 'paper_file']

    def __init__(self, *args, **kwargs):
        super(SubmitForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Textarea, forms.FileInput)):
                field.widget.attrs['class'] = 'form-control'
            if isinstance(field.widget, forms.FileInput):
                field.widget.attrs['class'] = 'form-control-file'
