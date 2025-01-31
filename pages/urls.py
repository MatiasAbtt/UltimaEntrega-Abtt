from django.urls import path
from .views import (
    PageListView,
    PageDetailView,
    PageCreateView,
    PageUpdateView,
    PageDeleteView,
    about_view
)

urlpatterns = [
    path('', PageListView.as_view(), name='page-list'),             # http://127.0.0.1:8000/
    path('pages/<int:pk>/', PageDetailView.as_view(), name='page-detail'),
    path('pages/create/', PageCreateView.as_view(), name='page-create'),
    path('pages/<int:pk>/update/', PageUpdateView.as_view(), name='page-update'),
    path('pages/<int:pk>/delete/', PageDeleteView.as_view(), name='page-delete'),
    path('about/', about_view, name='about'),
]