from django.shortcuts import render, render_to_response
from django.template import Context, loader, RequestContext
from uploadresume.forms import ResumeForm
import os

# Create your views here.

def index(request):
    CLIENT_ID = os.environ['CLIENT_ID']
    REDIRECT_URI = os.environ['REDIRECT_URI']
    oauth_url = "http://join.agiliq.com/oauth/authorize/?client_id=%s&redirect_uri=%s" % (CLIENT_ID, REDIRECT_URI)
    data = { "oauth_url": oauth_url }
    return render_to_response("index.html", data,
                              context_instance=RequestContext(request))

def upload_resume(request):
    form = ResumeForm()
    data = {'form': form}
    return render_to_response("upload_form.html", data,
                              context_instance=RequestContext(request))

