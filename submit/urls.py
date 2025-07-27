from django.urls import path
from .views import submission_view
app_name = 'submit'

urlpatterns = [
    path('submission/', submission_view, name='submission'),
]
