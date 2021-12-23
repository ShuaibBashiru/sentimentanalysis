from django.urls import path
from . import content, itemcontent

urlpatterns = [

    path('upload/users_preview/', content.file_upload_preview, name="file_upload_preview"),
    path('upload/file_upload/', content.file_upload, name="file_upload"),
    path('upload/items_upload/', itemcontent.file_upload, name="item_content_upload"),

]
