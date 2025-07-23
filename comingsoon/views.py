from django.shortcuts import render


def home(request):
    context = {}
    template = 'pages/home.html'
    return render(request, template, context)


def about_view(request):
    return render(request, 'pages/about.html', {'about_text': "HUET Conference là diễn đàn nghiên cứu đa ngành."})

def comitee_view(request):
    comitee = [
        {'name': 'TS. Nguyễn Văn A', 'position': 'Chủ tịch hội nghị'},
        {'name': 'PGS. Trần Thị B', 'position': 'Thư ký'},
    ]
    return render(request, 'pages/comitee.html', {'comitee_members': comitee})

def call_for_paper_view(request):
    topics = ["AI và ML", "Khoa học dữ liệu", "Công nghệ môi trường"]
    return render(request, 'pages/call_for_paper.html', {
        'call_text': "Chúng tôi trân trọng mời bạn gửi bài báo khoa học.",
        'topics': topics
    })

def registration_view(request):
    return render(request, 'pages/registration.html', {
        'registration_info': "Hội nghị miễn phí cho sinh viên và giảng viên HUET.",
        'registration_link': 'https://docs.google.com/forms/...'
    })

def submission_view(request):
    return render(request, 'pages/submission.html', {
        'submission_guide': "Bài báo cần nộp theo mẫu IEEE, định dạng PDF.",
        'submission_portal': 'https://easychair.org/conferences/?conf=huet2025'
    })

def program_view(request):
    program = [
        {'date': 'Ngày 1 - 20/09', 'sessions': [
            {'time': '08:00', 'title': 'Khai mạc', 'speaker': 'TS. Nguyễn A'},
            {'time': '10:00', 'title': 'Báo cáo chủ đề AI', 'speaker': 'PGS. Trần B'}
        ]},
        {'date': 'Ngày 2 - 21/09', 'sessions': [
            {'time': '09:00', 'title': 'Workshop IoT', 'speaker': 'TS. Lê C'}
        ]}
    ]
    return render(request, 'pages/program.html', {'program': program})