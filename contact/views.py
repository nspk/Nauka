from django.views.generic import DetailView, FormView
from .models import Message
from .forms import MessageForm, ContactForm

class MessageAddView(FormView): #dziedziczy z ModelForm co znaczy ze pracuje od razu na modelu
    form_class = ContactForm #MessageForm
    template_name = 'contact/message_form.html'
    success_url = "/"

    #uruchamiany kiedy jest poprawny
    def form_valid(self, form):
        form.save() #bo model form jest instancja ModelForm i ma metode save dla MessageForm
        return super(MessageAddView, self).form_valid(form)