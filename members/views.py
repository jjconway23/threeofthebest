from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from theblog.models import Profile
from .forms import EditProfileForm, SignUpForm, PasswordChangingForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView

#Profile Views
class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'facebook_url', 'twitter_url', 'instagram_url', 'tiktok_url', 'snapchat_url', 'youtube_url']
    success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

#Sign Up Views

class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    """
        View that allows users to change pasword
    """
    form_class = PasswordChangingForm
    success_url = reverse_lazy('home')

