from dj_rest_auth.registration.views import VerifyEmailView
from django.conf import settings
from django.test import Client
from django.http import HttpResponseRedirect


def email_confirm_redirect(request, key):
    post_url = "/api/auth/account-confirm-email/"
    client = Client()
    post_data = {'key': key}
    response = client.post(post_url, post_data)
    return response


