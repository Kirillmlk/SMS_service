from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.ClientListView.as_view(), name='client-list'),
    path('clients/<int:pk>/', views.ClientDetailView.as_view(), name='client-detail'),
    path('mailings/', views.MailingListView.as_view(), name='mailing-list'),
    path('mailings/<int:pk>/', views.MailingDetailView.as_view(), name='mailing-detail'),
    path('mailings/<int:pk>/messages/', views.MailingMessageListView.as_view(), name='mailing-message-list'),
]