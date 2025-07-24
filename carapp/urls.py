from django.urls import path
from . import views

urlpatterns = [
    path('bookdrive/', views.book_drive, name='book_drive'),
    path('', views.home, name='home'),
    path('bookdrive/', views.book_drive, name='book_drive'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.user_login, name='login'),
]


