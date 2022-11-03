from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = "SoundRecorderApp"

urlpatterns = [
    # path("", views.signup, name="signup"),
    path("main/", views.index, name="index"),
    path("record/", views.record, name="record"),
    path("record/detail/<int:id>/", views.record_detail, name="record_detail"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    # path('logout', views.custom_logout, name='logout'),
]
