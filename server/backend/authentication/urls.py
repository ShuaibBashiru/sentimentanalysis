from django.urls import path
from . import views, auth, auth_user, upload


urlpatterns = [
    path('', views.index, name="home"),
    path('sign_in/', auth.authenticate, name="sign_to_portal"),
    path('sign_in_user/', auth_user.authenticate, name="sign_user"),
    path('tokenize/', auth.token_nizer, name="tokenize_csrf"),
    path('auth_check/', auth.auth_check_session, name="check_session"),
    path('logout/', auth.logout_session, name="auth_logout_session"),
]
