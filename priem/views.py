# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .forms import DataForm
import dataProcessing as dp

def index(request):
    if request.POST:
        form = DataForm(request.POST)
        res = dp.processing(form)
        html = u'''<!DOCTYPE html>
                    <html lang="ru">
                    <head>
                        <link rel="stylesheet" type="text/css" href="../../static/priem/style/bootstrap.min.css">
                        <link rel="stylesheet" type="text/css" href="../../static/priem/style/style.css">
                        <link rel="stylesheet" type="text/css" href="../../static/priem/style/style_res.css">
                        <script src="../../static/priem/js/jquery-1.11.3.min.js"></script>
                        <script src="../../static/priem/js/bootstrap.min.js"></script>
                        <script src="../../static/priem/js/script.js"></script>
                        <meta charset="utf-8">
                        <title>Веб-калькулятор</title>
                    </head>''' + u'''<body>
                        <div class=" header">
                            <img src="../../static/priem/images/tsu.png">
                            <h1 class="header-main"><b>Калькулятор баллов ЕГЭ</b></h1>
                        </div> %s <br><br>
                        <div align="center">
                            <a href="" class="btn btn-lg btn-success" role="button">Посчитать ещё</a>
                        </div>
                        <br><br><br><br>
                        </body></html>''' % res
        return HttpResponse(html)

    
    form = DataForm()

    template = 'priem/index.html'
    context = {'form': form}
    return render(request, template, context)

# from django.contrib import auth
# from django.shortcuts import redirect
# from django.views.generic.simple import direct_to_template

# def user_login_view(request):
#     form = UserLoginForm(request.POST or None)
#     context = { 'form': form, }
#     if request.method == 'POST' and form.is_valid():
#         username = form.cleaned_data.get('username', None)
#         password = form.cleaned_data.get('password', None)
#         user = auth.authenticate(username=username, password=password)
#         if user and user.is_active:
#             auth.login(request, user)
#             return redirect('index_page')
#     return direct_to_template(request, 'form.html', context)