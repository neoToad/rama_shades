from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from .models import User
from django import forms


class SignUpForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        helper = FormHelper()
        helper.form_show_labels = False


        self.helper = helper

    class Meta:
        model = User
        fields = ("email", "password1", "password2")