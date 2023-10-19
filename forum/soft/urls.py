from django.urls import path
from . import views

app_name = 'soft'

urlpatterns = [
    path('', views.soft_home, name='soft_home'),
    path('create_soft', views.create_soft, name='create_soft'),
    path('<int:pk>', views.SoftDetailView.as_view(), name='soft-detail'),
    path('<int:pk>/update', views.SoftUpdateView.as_view(), name='soft-update'),
    path('<int:pk>/delete', views.SoftDeleteView.as_view(), name='soft-delete'),
]