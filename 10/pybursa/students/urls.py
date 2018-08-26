from django.urls import path, include
from django.views.generic import TemplateView

from . import views

app_name = 'students'
urlpatterns = [
    path('', views.students_list, name='list'),
    path('<int:student_id>/', views.student_view, name='detail'),
    path('edit/<int:student_id>/', views.student_edit, name='student_edit'),
    path('add/', views.student_add, name='student_add'),
    path('delete/<int:student_id>/', views.student_delete, name='student_delete'),
    path('email/', views.MailView.as_view(), name = 'student_email'),
    path('send/', TemplateView.as_view(template_name="students/send.html"), name = 'mail_send'),
    #path('heroes/', views.heroes, name='heroes_l'),
    #path('heroes/<str:nick>', views.hero, name='personal-room'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]

