from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from .forms import ContactForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'carapp/hm.html')

def book_drive(request):
    return render(request, 'carapp/bookdrive.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            email_to_you = EmailMessage(
                subject=f"New Contact Form Submission from {name}",
                body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email='tanviranade4@gmail.com',
                to=['tanviranade4@gmail.com'],
                headers={'Reply-To': email}
            )
            email_to_you.send()

            send_mail(
                subject="Thank you for contacting Car Hive!",
                message="We have received your message and will get back to you soon.\n\nRegards,\nCar Hive Team",
                from_email='tanviranade4@gmail.com',
                recipient_list=[email],
            )

            return render(request, 'carapp/contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'carapp/contact.html', {'form': form})

# ✅ Moved outside — this is correct
def signup_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered.")
        else:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
            user.save()
            return redirect('login')

    return render(request, 'carapp/signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # redirect to home or dashboard
        else:
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'carapp/login.html')
