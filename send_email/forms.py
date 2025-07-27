from django import forms
from .models import Subscriber

class NotifyForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data['email']
        return email

    def validate_unique(self):
        # Bỏ qua validation unique mặc định để cho phép trùng email
        pass
