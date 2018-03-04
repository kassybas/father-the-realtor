from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('props/', views.PropertyListView.as_view(), name='props'),
    path('props/<int:pk>', views.PropertyDetailView.as_view(), name='prop-detail'),
]
