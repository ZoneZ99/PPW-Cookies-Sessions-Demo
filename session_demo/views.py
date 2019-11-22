from django.shortcuts import render, redirect


def donat_session(request):
    if request.session.get('donat'):
        request.session['ada_donat'] = True
    return render(request, 'donat-session.html')


def tambah_donat(request):
    if request.session.get('donat'):
        donat = request.session['donat']
        request.session['donat'] = donat + 1
    else:
        request.session['donat'] = 1
    return redirect(donat_session)


def delete_donat_session(request):
    if request.session.get('donat'):
        del request.session['donat']
    return redirect(donat_session)


def delete_all_sessions(request):
    request.session.flush()
    return redirect(donat_session)