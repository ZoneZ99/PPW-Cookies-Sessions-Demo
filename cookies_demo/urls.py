from django.urls import path

from cookies_demo.views import cookies_view, delete_cookie

urlpatterns = [
    path('', cookies_view),
    path('delete/', delete_cookie),
]
