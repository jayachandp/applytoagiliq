from django.shortcuts import render, render_to_response
from django.template import RequestContext
from uploadresume.forms import ResumeForm
import os
import json
import requests

# Create your views here.

def index(request):
    CLIENT_ID = os.environ['CLIENT_ID']
    REDIRECT_URI = os.environ['REDIRECT_URI']
    oauth_url = "http://join.agiliq.com/oauth/authorize/" \
                "?client_id=%s&redirect_uri=%s" % (CLIENT_ID, REDIRECT_URI)
    data = {"oauth_url": oauth_url}
    return render_to_response("index.html", data,
                              context_instance=RequestContext(request))

def upload_resume(request):
    # Get the access token with the CLIENT_SECRET
    CLIENT_ID = os.environ['CLIENT_ID']
    REDIRECT_URI = os.environ['REDIRECT_URI']
    CLIENT_SECRET = os.environ['CLIENT_SECRET']
    code = request.GET['code']
    access_token_url = "http://join.agiliq.com/oauth/access_token/"
    payload = {
        "client_id":CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": code,
        }
    response_raw = requests.post(access_token_url, data=payload)
    response = json.loads(response_raw.text)
    form_action_url = "http://join.agiliq.com/api/resume/upload/" \
                 "?access_token=%s" % (response['access_token'])
    # Form for uploading the Resume
    form = ResumeForm()
    data = {
        'form': form,
        'action': form_action_url
        }
    return render_to_response("upload_form.html", data,
                              context_instance=RequestContext(request))


