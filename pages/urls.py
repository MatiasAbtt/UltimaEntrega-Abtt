from django.urls import path
from . import views
from .views import (
    PageListView,
    PageDetailView,
    PageCreateView,
    PageUpdateView,
    PageDeleteView,
    about_view, 
)

urlpatterns = [
    path('<int:pk>/', PageDetailView.as_view(), name='page-detail'),
    path('create/', PageCreateView.as_view(), name='page-create'),
    path('<int:pk>/update/', PageUpdateView.as_view(), name='page-update'),
    path('<int:pk>/delete/', PageDeleteView.as_view(), name='page-delete'),
    path('about/', about_view, name='about'),
]