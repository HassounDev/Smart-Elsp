from django.shortcuts import render
from django.http import Http404
from merchandise_app.models import Merchandise, Orderer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

def dashboard(request):
    try:
        merchandises = Merchandise.objects.all()
    except Merchandise.DoesNotExist:
        raise Http404("Merchandise doesn't exist!")
    return render(request, 'dashboard/index.html', {'merchandises':merchandises})

class UserFormView(View):

    form_class = UserForm
    template_name = 'dashboard/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
        return render(request, self.template_name, {'form': form})
