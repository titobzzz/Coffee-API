from django.urls import path, include
from . import views 

from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'profiles', views.ProfileViewSet, basename="profile")

urlpatterns=[
    # path('',include(router.urls)),
    path('profiles/', views.ProfileViewSet.as_view({"get":"list","post":"perform_create"}), name="profile_list"),
     path('profiles/<str:id>/', views.ProfileViewSet.as_view({"get":"retrieve","patch":"update"}), name="profile_retrieve"),
]