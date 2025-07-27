from django.shortcuts import render
from .forms import SubmitForm
from django.core.mail import send_mail
from django.conf import settings

def submission_view(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save()

            # Gửi email xác nhận
            send_mail(
                subject='Cảm ơn bạn đã gửi bài tham dự!',
                message=f"Xin chào {submission.fullname},\n\nCảm ơn bạn đã gửi bài tham dự hội nghị.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[submission.email],
                fail_silently=False,
            )

            return render(request, 'submit/success.html', {'fullname': submission.fullname})
        else:
            print("Form errors:", form.errors)
    else:
        form = SubmitForm()

    return render(request, 'submit/submit_form.html', {'form': form})
