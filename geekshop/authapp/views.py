# from django.contrib import auth
# from django.shortcuts import HttpResponseRedirect
# from django.shortcuts import render
# from django.urls import reverse
#
#
# def login(request):
#     title = 'вход'
#     login_form = ShopUserForm(data=request.POST)
#     if request.method == 'POST' and login_form.is_valid():
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = auth.authenticate(username=username, password=password)
#         if user and user.is_active:
#             auth.login(request, user)
#             return HttpResponseRedirect(reverse('index'))
#
#     context = {'title': title, 'login_form': login_form}
#     return render(request, 'templates/templates/login.html', context=context)
#
#
#
# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))