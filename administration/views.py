from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import LoginForm


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'administration/login.html'

    def get(self, request):
        login_form = self.form_class(None)
        return render(request, self.template_name, {'login_form': login_form})

    def post(self, request):
        login_form = self.form_class(request.POST)

        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']

            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('contacts:index'))
            else:
                error_msg = 'Invalid User'
                return render(request, self.template_name, {'login_form': login_form, 'error_msg': error_msg})
        else:
            error_msg = 'Invalid User'
            return render(request, self.template_name, {'login_form': login_form, 'error_msg': error_msg})

