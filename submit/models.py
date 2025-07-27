from django.db import models


class Submission(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    paper_name = models.CharField(max_length=255)  # ➕ Thêm trường này
    message = models.TextField(blank=True)
    paper_file = models.FileField(upload_to='papers/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} - {self.paper_name}"
