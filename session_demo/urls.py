from django.urls import path

from session_demo.views import donat_session, delete_donat_session, tambah_donat, delete_all_sessions

urlpatterns = [
    path('', donat_session, name='main'),
    path('tambah-donat/', tambah_donat, name='tambah-donat'),
    path('delete-donat-session/', delete_donat_session, name='delete-donat'),
    path('delete-all-sessions/', delete_all_sessions, name='delete-all-sessions'),
]
