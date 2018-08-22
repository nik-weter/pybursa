from django.urls import path, re_path


from . import views

app_name = 'nine'
urlpatterns = [
    path('square', views.quad_equation, name='index'),
    path('heroes/', views.heroes, name='heroes_l'),
    path('heroes/<str:nick>', views.hero, name='personal-room'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]