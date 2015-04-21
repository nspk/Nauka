from django import forms
from .models import Message

class MessageForm(forms.ModelForm): #dziedziczy z ModelForm co znaczy ze pracuje od razu na modelu
    class Meta:
        model = Message
        fields = ('uzytkownik', 'email', 'tresc')


class ContactForm(forms.Form): #bezwykorzystania Modelform
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())

    def clean_name(self):
        data = self.cleaned_data['name']
        if "D" not in data:
            raise forms.ValidationError("Musisz mieć imię zawierajace 'D'")
        return data