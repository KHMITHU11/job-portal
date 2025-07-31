from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, UserProfileForm
from .models import UserProfile


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        if hasattr(self.request.user, 'profile'):
            return reverse_lazy(self.request.user.profile.get_dashboard_url())
        return reverse_lazy('home')


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Account created successfully! Please log in.')
        return response
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


@login_required
def profile_view(request):
    """View and edit user profile"""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.profile)
    
    context = {
        'form': form,
        'user': request.user,
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def dashboard_redirect(request):
    """Redirect user to appropriate dashboard based on user type"""
    if hasattr(request.user, 'profile'):
        return redirect(request.user.profile.get_dashboard_url())
    else:
        # If no profile exists, create one with default type
        UserProfile.objects.create(user=request.user, user_type='applicant')
        return redirect('applicant_dashboard')


@login_required
def change_user_type(request):
    """Allow users to change their user type"""
    if request.method == 'POST':
        new_type = request.POST.get('user_type')
        if new_type in ['employer', 'applicant']:
            request.user.profile.user_type = new_type
            request.user.profile.save()
            messages.success(request, f'Account type changed to {new_type.title()}.')
            return redirect('dashboard_redirect')
    
    return render(request, 'accounts/change_user_type.html') 