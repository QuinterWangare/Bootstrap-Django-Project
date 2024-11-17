from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create_testimonial, name='create_testimonial'),
    path('update/<int:pk>/', views.update_testimonial, name='update_testimonial'),
    path('delete/<int:pk>/', views.delete_testimonial, name='delete_testimonial'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)