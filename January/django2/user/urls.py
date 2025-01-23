from django.urls import path
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import SignUpView, UserUpdateView, MyPageView, UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('mypage/', MyPageView.as_view(), name='mypage'),
    path('mypage/edit/', UserUpdateView.as_view(), name='edit_profile'),
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-update-destroy'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('login/', LoginView.as_view(), name='login'),
]