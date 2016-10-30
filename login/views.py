from django.shortcuts import render_to_response, HttpResponseRedirect, render
import logging
from django.contrib import auth
logger = logging.getLogger(__name__)


# *************************************************** #
#                   LOGIN                             #
# *************************************************** #
def login(request):
    render(request, "login.html", {})


def auth_view(request):
    def authenticate(username, password):
        pass
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    logger.info(username)
    logger.info(password)
    user = authenticate(username=username, password=password)
    user = ''
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('')
    else:
        return HttpResponseRedirect('/accounts/invalid/')


def loggedin(request):
    return render_to_response('loggedin.html', {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('invalid.html')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')