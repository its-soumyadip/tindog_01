from django.urls import path
# from home import views
from .views import Index,LoginView,LogoutView,RegisterView
urlpatterns = [
    path('',Index.as_view()),
    path('login',LoginView.as_view()),
    path('logout',LogoutView.as_view()),
    path('register',RegisterView.as_view()),
]
