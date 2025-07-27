from django.urls import path
from . import views

app_name = 'comingsoon'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('comitee/', views.comitee_view, name='comitee'),
    path('call-for-paper/', views.call_for_paper_view, name='call_for_paper'),
    # path('registration/', views.registration_view, name='registration'),
    # path('submission/', views.submission_view, name='submission'),
    path('program/', views.program_view, name='program'),
]


