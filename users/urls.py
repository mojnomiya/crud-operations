from django.urls import path
from .views import UsersGetPostView, UserDetaiDeletelView

urlpatterns = [
    path('', UsersGetPostView.as_view(), name='users'),
    path('<int:pk>/', UserDetaiDeletelView.as_view(), name='users_details'),
]