from django import forms
from .models import EmergencyRequest

class EmergencyRequestForm(forms.ModelForm):
    class Meta:
        model = EmergencyRequest
        fields = ['emergency_type', 'document']
        widgets = {
            'emergency_type': forms.Select(choices=[
                ('Medical', 'Medical Emergency'),
                ('Urgent Business', 'Urgent Official/Business Duty'),
                ('Disability', 'Disability/Senior Citizen Assistance'),
                ('Other', 'Other Urgent Situation')
            ], attrs={'required': True}),
            'document': forms.FileInput(attrs={'accept': '.pdf,.jpg,.jpeg,.png'})
        }
        help_texts = {
            'document': 'Please upload supporting documents (PDF, JPG, PNG) to prove urgency.'
        }
