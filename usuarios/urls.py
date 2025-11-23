from django.urls import path
from usuarios.views import my_login, my_signup, about
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', my_login, name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', my_signup, name='signup'),
    path('about/', about, name='about')
]