from django import forms
from django.utils import timezone
import datetime


class ReminderForm(forms.Form):
    mail = forms.EmailField(max_length=100)
    text = forms.CharField(max_length=500)
    date_time = forms.DateTimeField(initial=timezone.now())

    def clean_date_time(self):
        data = self.cleaned_data['date_time']
        if data > (timezone.now() + datetime.timedelta(days=2)) or data < timezone.now():
            raise forms.ValidationError('Incorrect Date/Time for reminder')
        return data
