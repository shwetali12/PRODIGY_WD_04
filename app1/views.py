from django.shortcuts import render,redirect
from django.core.mail import send_mail 
from django.conf import settings
from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def resume(request):
    return render(request,'resume.html')

def work(request):
    return render(request,'work.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send the email
            subject = 'Contact Form Submission'
            message = f'Name: {name}\nEmail: {email}\nMessage: {message}'
            from_email = settings.EMAIL_HOST_USER  # Use the same email as configured in settings.py
            recipient_list = ['jagdaleshwetali1820@gmail.com','shwetalipoman@gmail.com']  # The recipient's email address

            send_mail(subject, message, from_email, recipient_list)

            # Redirect or display a success message
            return redirect('success') 
            # Process the form data, e.g., send an email or save to a database
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success(request):
    return render(request,'success.html')