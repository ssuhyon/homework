from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django import forms

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class MyPageView(LoginRequiredMixin, TemplateView):
    template_name = 'user/mypage.html'

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user_update.html'
    success_url = reverse_lazy('mypage')

    def get_object(self):
        return self.request.user
class MyPageView(TemplateView):
    template_name = 'user/mypage.html'
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('login')
