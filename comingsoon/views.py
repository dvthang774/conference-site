from django.shortcuts import render


def home(request):
    context = {}
    template = 'pages/home.html'
    return render(request, template, context)



def about_view(request):
    about_text = """
Hội thảo khoa học quốc gia với chủ đề **“Trí tuệ nhân tạo, công nghệ xanh và phát triển bền vững”** được tổ chức nhằm:

1. **Đánh giá và chia sẻ kết quả nghiên cứu** mới nhất trong các lĩnh vực trí tuệ nhân tạo (AI), công nghệ xanh và các giải pháp phát triển bền vững; đồng thời cập nhật xu hướng khoa học và công nghệ trong và ngoài nước.

2. **Tạo diễn đàn kết nối** giữa các nhà khoa học, giảng viên, người học, doanh nghiệp và cơ quan quản lý; hình thành các mạng lưới hợp tác đa ngành, thúc đẩy chuyển giao công nghệ và thương mại hoá sản phẩm nghiên cứu.

3. **Định hướng nghiên cứu ứng dụng AI** vào công nghệ, kỹ thuật điều khiển, tự động hoá, năng lượng xanh, tối ưu hoá quy trình sản xuất, tiết kiệm năng lượng, giảm phát thải và thích ứng biến đổi khí hậu; phù hợp với chiến lược phát triển bền vững quốc gia.

4. **Góp phần nâng cao năng lực nghiên cứu** và khẳng định vị thế học thuật, thúc đẩy công bố quốc tế và xây dựng thương hiệu khoa học uy tín trong lĩnh vực AI, công nghệ xanh và phát triển bền vững.

5. **Khuyến khích đổi mới sáng tạo** thông qua các phiên thảo luận chuyên đề, trình diễn công nghệ và trưng bày sản phẩm nghiên cứu của giảng viên, sinh viên và doanh nghiệp.
"""


    return render(request, 'pages/about.html', {
        'about_text': about_text,
    })


def comitee_view(request):
    comitee = [
        {'name': 'TS. Nguyễn Văn A', 'position': 'Chủ tịch hội nghị'},
        {'name': 'PGS. Trần Thị B', 'position': 'Thư ký'},
    ]
    return render(request, 'pages/comitee.html', {'comitee_members': comitee})

def call_for_paper_view(request):
    call_text = """
AIGTSD 2025, Hội nghị Khoa học Quốc gia về Trí tuệ Nhân tạo, Công nghệ Xanh và Phát triển Bền vững lần thứ 1, sẽ diễn ra từ ngày 20-21/09/2025 tại Khoa Kĩ thuật và Công nghệ - Đại học Huế. Hội nghị nhằm kết nối các nhà khoa học, giảng viên, sinh viên và doanh nghiệp trong lĩnh vực AI, công nghệ xanh và phát triển bền vững.
    """  # phần mô tả dài như trên, bạn có thể để trong biến hoặc file txt

    topics = [
        "Kỹ thuật Xây dựng Dân dụng, Giao thông, Hạ tầng",
        "Kiến trúc, Quy hoạch đô thị",
        "Năng lượng Tái tạo, Tiết kiệm năng lượng",
        "Kỹ thuật Ô tô, xe điện",
        "Kỹ thuật Cơ khí và Sản xuất, Cơ học Ứng dụng",
        "Công nghệ Thông tin, Chuyển đổi số",
        "Tự động hóa, Thiết kế IC, Bán dẫn",
        "Vật liệu, Công nghệ Sinh học và Công nghệ Môi trường",
        "Các lĩnh vực khác",
    ]

    submission_guidelines = """
- Các bài gửi có thể viết bằng tiếng Anh hoặc tiếng Việt (cho Kỷ yếu Hội nghị có ISBN). Bài báo toàn văn yêu cầu dài 4-6 trang sử dụng mẫu của Hội nghị (đang cập nhật).
    """

    important_dates = [
        "Hạn cuối gửi bài: 20/03/2025 - 15/04/2025",
        "Thông báo chấp nhận: 15/05/2025 - 30/05/2025",
        "Hạn cuối đăng ký: 30/06/2025",
    ]

    return render(request, 'pages/callforpaper.html', {
        'call_text': call_text,
        'topics': topics,
        'submission_guidelines': submission_guidelines,
        'important_dates': important_dates,
    })


# def registration_view(request):
#     return render(request, 'pages/registration.html', {
#         'registration_info': "Hội nghị miễn phí cho sinh viên và giảng viên HUET.",
#         'registration_link': 'https://docs.google.com/forms/...'
#     })

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