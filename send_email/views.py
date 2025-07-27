from django.shortcuts import render
from .forms import NotifyForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Subscriber

def notify_view(request):
    if request.method == 'POST':
        form = NotifyForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            if created:
                print(f"Đã tạo subscriber mới: {subscriber.email}")
            else:
                print(f"Subscriber đã tồn tại: {subscriber.email}")

            send_mail(
                subject='Cảm ơn bạn đã đăng ký!',
                message='Bạn đã đăng ký nhận thông tin hội nghị thành công. Chúng tôi sẽ liên hệ sớm.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[subscriber.email],
                fail_silently=False,
            )

            return render(request, 'notify/success.html', {'email': subscriber.email})
        else:
            print("Form errors:", form.errors)
    else:
        form = NotifyForm()
    return render(request, 'notify/notify.html', {'form': form})
