from django.shortcuts import render_to_response, render
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['dedhio@gmail.com']
            if cc_myself:
                recipients.append(sender)
            send_mail(subject,message,sender,recipients)
            return HttpResponseRedirect('/servicedesks/thanks')
    else:
        form = ContactForm()
    return render_to_response('contact.html', {'form': form}, RequestContext(request))
    

def thanks(request):
    return render(request, 'thanks.html', {"frota": 300})


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('thanks')

    def form_valid(self, form):

        form.send_mail()
        return super().form_valid(form)







