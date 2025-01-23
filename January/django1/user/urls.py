from django.urls import path
from .views import SignUpView, UserUpdateView, MyPageView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('mypage/', MyPageView.as_view(), name='mypage'),
    path('mypage/edit/', UserUpdateView.as_view(), name='edit_profile'),
]