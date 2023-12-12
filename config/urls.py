from django.contrib import admin
from django.urls import path, include
from phonebook import views, api_views
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'persone/', api_views.PersoneModelViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('add/', views.AddPhoneFormView.as_view()),
    path('delete/<int:pk>', views.DeletePhoneView.as_view(), name='delete'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/persone/', api_views.persone_list),
    path('api/persone-cbv/', api_views.PersoneListAPIView.as_view(), name='persone-cbv'),
    path('api/persone-cbv-detail/<int:pk>', api_views.PersonDetailAPIView.as_view(), name='persone-cbv-detail'),
    path('api/persone-cbv-update/<int:pk>', api_views.PersoneUpdateAPIView.as_view(), name='persone-cbv-update'),
    path('api/persone-cbv-delete/<int:pk>', api_views.PersoneDeleteAPIView.as_view(), name='persone-cbv-delete'),
]
