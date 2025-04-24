from django.urls import path
from .views import RegisterView, LoginView, CurrentUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', CurrentUserView.as_view(), name='current_user'),
    path('predict/', CurrentUserView.as_view(), name='PredictView'),
    
]