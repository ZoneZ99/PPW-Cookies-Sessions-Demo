from django.http import HttpResponse
from django.shortcuts import render


def cookies_view(request):
    response = render(request, 'cookies_page.html')
    if request.COOKIES.get('donat'):
        donat = int(request.COOKIES.get('donat'))
        response.set_cookie('donat', donat + 1)
    else:
        response.set_cookie('donat', 1)
    return response


def delete_cookie(request):
    if request.COOKIES.get('donat'):
        response = HttpResponse("<h1>DONAT DIHAPUS</h1>")
        response.delete_cookie('donat')
    else:
        response = HttpResponse("<h1>BELUM ADA DONAT :(</h1>")
    return response
