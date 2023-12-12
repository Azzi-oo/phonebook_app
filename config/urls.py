from django.contrib import admin
from django.urls import path
from phonebook import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('add/', views.AddPhoneFormView.as_view()),
]
