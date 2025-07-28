# contact/views.py

from django.shortcuts import render
from django.core.mail import send_mail

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"New Contact Form Submission:\n\nName: {name}\nEmail: {email}\nMessage:\n{message}"

        send_mail(
            subject="📩 New Message from Portfolio",
            message=full_message,
            from_email=email,
            recipient_list=['suryadevsharma11@gmail.com'],  # ✅ Your Gmail here
        )

        return render(request, 'index.html', {'success': True})

    return render(request, 'index.html')
