from django.urls import  path
from . import views

urlpatterns = [
    path('',views.SignUpView.as_view(), name="register"),
    path('register-buyer/',views.BuyerSignUpView.as_view(), name="buyer_signup"),
    path('register-seller/',views.SellerSignUpView.as_view(), name="seller_signup")

]