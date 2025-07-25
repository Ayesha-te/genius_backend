from django.urls import path
from users.views.auth_views import register_user, login_user, logout_user
from users.views.account_views import change_password, forgot_password

urlpatterns = [
    path('register/', register_user),
    path('login/', login_user),
    path('logout/', logout_user),
    path('change-password/', change_password),
    path('forgot-password/', forgot_password),
]
