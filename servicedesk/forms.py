from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def send_mail(self):
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        sender = self.cleaned_data['sender']
        cc_myself = self.cleaned_data['cc_myself']
        recipients = ['dedhio@gmail.com']
        if cc_myself:
            recipients.append(sender)
        send_mail(subject,message,sender,recipients)