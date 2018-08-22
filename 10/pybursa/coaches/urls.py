from django.urls import path


from . import views

app_name = 'coaches'
urlpatterns = [
    path('', views.CoachesList.as_view(), name='list'),
    #path('', views.coaches_list, name='list'),
    path('<int:pk>/', views.CoacheDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.CoacheEdit.as_view(), name='coache_edit'),
    #path('add/', views.CoacheCreate.as_view(), name='coache_add'),
    path('add/', views.coache_add, name='coache_add'),
    path('delete/<int:pk>/', views.CoacheDelete.as_view(), name='coache_delete'),
    #path('<int:coache_id>/', views.coache_view, name='detail'),
    #path('heroes/', views.heroes, name='heroes_l'),
    #path('heroes/<str:nick>', views.hero, name='personal-room'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]