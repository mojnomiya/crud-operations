from django.urls import path
from .views import UserGetPostView, UserDetailDeleteView

urlpatterns = [
    path('', UserGetPostView.as_view(), name='users'),
    path('<int:pk>/', UserDetailDeleteView.as_view(), name='users_details'),
]