from django.shortcuts import render
from .models import User
from .forms import SellerSignUpForm,  BuyerSignUpForm
from django.views.generic import (
    TemplateView,
    CreateView,
    View
)

# Create your views here.
class SignUpView(TemplateView):
    template_name = ".html"

class BuyerSignUpView(CreateView):
    model = User
    form_class = BuyerSignUpForm
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'buyer'
        return super().get_context_data(**kwargs)

class SellerSignUpView(CreateView):
    model = User
    form_class = SellerSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'seller'
        return super().get_context_data(**kwargs)


class LoginView(View):
    pass

