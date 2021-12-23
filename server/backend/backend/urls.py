from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('posts/', include('forms.urls')),
    path('upload/', include('upload.urls')),
    path('download/', include('file_generator.urls')),
    path('api/', include('api.urls')),
    path('mailer/', include('api.urls')),
    # path('user_api/', include('user_api.urls')),
    # path('post_user/', include('user_forms.urls')),
    path('web/', include('web_app.urls')),
]
