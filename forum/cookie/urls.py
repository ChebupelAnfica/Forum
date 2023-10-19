from django.urls import path
from . import views

app_name = 'cookie'

urlpatterns = [
    path('', views.cookie_home, name='cookie_home'),
    path('create_cookie', views.create_cookie, name='create_cookie'),
    path('<int:pk>', views.CookieDetailView.as_view(), name='cookie-detail'),
    path('<int:pk>/update', views.CookieUpdateView.as_view(), name='cookie-update'),
    path('<int:pk>/delete', views.CookieDeleteView.as_view(), name='cookie-delete'),
]