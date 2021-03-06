from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	path('',views.index, name = 'index'),
	path('business', views.business, name = 'business'),
	path('register/', user_views.register, name = 'register'),
	path('login/', LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
	path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
	path('profile/', user_views.profile , name = 'profile'),
]