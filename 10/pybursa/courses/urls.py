from django.urls import path


from . import views

app_name = 'courses'
urlpatterns = [
    #path('', views.courses_list, name='list'),
    path('', views.CoursesList.as_view(), name = 'list'),
    #path('<int:course_id>/', views.course_view, name='detail'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='detail'),
    #path('edit/<int:course_id>/', views.course_edit, name='course_edit'),
    path('edit/<int:pk>/', views.CourseEdit.as_view(), name='course_edit'),
    #path('add/', views.course_add, name='course_add'),
    path('add/', views.CourseCreate.as_view(), name='course_add'),
    path('delete/<int:pk>/', views.CourseDelete.as_view(), name='course_delete'),
    #path('heroes/', views.heroes, name='heroes_l'),
    #path('heroes/<str:nick>', views.hero, name='personal-room'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]