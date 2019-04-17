from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about', views.about_page,name='about_page'),
    path('service', views.service_page,name='service_page'),
    path('contact', views.contact_page, name='contact_page'),
    path('blog', views.blog_page, name='blog_page'),
    
]