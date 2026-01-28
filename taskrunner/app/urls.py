from django.urls import path
from .views.auth import custom_logout
from .views.filesets import (
    filesets,
    fileset,
    upload_fileset,
    rename_fileset,
    delete_fileset,
    delete_all_filesets,
    download_fileset,
)


urlpatterns = [
    path('', filesets),
    path('filesets/', filesets),
    path('filesets/upload', upload_fileset),
    path('filesets/delete', delete_all_filesets),
    path('filesets/<str:fileset_id>', fileset),
    path('filesets/<str:fileset_id>/rename', rename_fileset),
    path('filesets/<str:fileset_id>/delete', delete_fileset),
    path('filesets/<str:fileset_id>/download', download_fileset),
    path('accounts/logout/', custom_logout),
]