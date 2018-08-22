from django.urls import path


from . import views

app_name = 'students'
urlpatterns = [
    path('', views.students_list, name='list'),
    path('<int:student_id>/', views.student_view, name='detail'),
    path('edit/<int:student_id>/', views.student_edit, name='student_edit'),
    path('add/', views.student_add, name='student_add'),
    path('delete/<int:student_id>/', views.student_delete, name='student_delete'),
    #path('heroes/', views.heroes, name='heroes_l'),
    #path('heroes/<str:nick>', views.hero, name='personal-room'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]