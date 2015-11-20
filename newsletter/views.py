from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail

from .forms import SignUpForm
from .forms import ContactForm
from .models import SignUp
# Create your views here.


def home(request):

    title = 'Welcome'
    if request.user.is_authenticated():
        title = title + str(request.user)

    form = SignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.full_name:
            instance.full_name = request.user or "Lukasz"

        instance.save()

    context = {
        'title': title,
        'form': form,
    }

    if request.user.is_staff and request.user.is_authenticated():
        context = {
            'queryset': SignUp.objects.all()
        }

    return render(request, 'home.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    title = "Contact Us"
    text_align_center = True
    context = {
        'form': form,
        'title': title,
        'text_align_center': text_align_center,
    }

    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_full_name = form.cleaned_data.get('full_name')
        form_message = form.cleaned_data.get('full_message')

        subject = 'this is the subject'
        message = 'this is the message'
        from_ = settings.EMAIL_HOST_USER
        to_ = [from_, 'lukasz.mistura@gmail.com']

        send_mail(subject,
                  message,
                  settings.EMAIL_HOST_USER,
                  to_,
                  fail_silently=False)
        # for key, value in form.cleaned_data.iteritems():
        #     print key, value

    return render(request, 'forms.html', context)
