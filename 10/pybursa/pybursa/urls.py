from django.views.generic import TemplateView

from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # url(r'^blog/', include('blog.urls')),
    path('coaches/', include('coaches.urls')),
    path('courses/', include('courses.urls')),
    path('students/', include('students.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('products/', TemplateView.as_view(template_name='index.html'), name='products'),
    path('product/', TemplateView.as_view(template_name='index.html'), name='product'),
    path('admin/', admin.site.urls),
]
admin.site.site_header = 'PyBursa administration'