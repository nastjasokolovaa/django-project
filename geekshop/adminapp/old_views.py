# ---------------------------------users-----------------------------------------
# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админка/пользователи'
#
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     context = {
#         'title': title,
#         'objects': users_list
#     }
#
#     return render(request, 'users/users.html', context=context)


# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     title = 'пользователи/создание'
#
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('adminapp:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#
#     context = {
#         'title': title,
#         'update_form': user_form,
#     }
#
#     return render(request, 'users/user_create_update.html', context)

# @user_passes_test(lambda u: u.is_superuser)
# def user_update(request, pk):
#     title = 'пользователи/редактирование'
#
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('adminapp:user_update', args=[edit_user.pk]))
#     else:
#         edit_form = ShopUserEditForm(instance=edit_user)
#
#     context = {
#         'title': title,
#         'update_form': edit_form,
#     }
#
#     return render(request, 'users/user_create_update.html', context)



# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     title = 'пользователи/удаление'
#
#     delete_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         delete_user.is_active = False
#         delete_user.save()
#         return HttpResponseRedirect(reverse('adminapp:users'))
#
#     context = {
#        'title': title,
#        'user_to_delete': delete_user,
#     }
#
#     return render(request, 'users/user_delete.html', context)

# ---------------------------------------------category----------------------

# @user_passes_test(lambda u: u.is_superuser)
# def categories(request, pk=None):
#     title = 'админка/категории'
#
#     if pk is None:
#         categories_list = ProductCategory.objects.all()
#         context = {
#             'title': title,
#             'categories': categories_list
#         }
#         return render(request, 'categories/categories.html', context)
#     else:
#         category = get_object_or_404(ProductCategory, pk=pk)
#         context = {
#             'title': title,
#             'category': category,
#         }
#         return render(request, 'categories/category.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#
#     title = 'админка/создание категории'
#
#     if request.method == 'POST':
#         category_form = ProductCategoryEditForm(request.POST, request.FILES)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('adminapp:categories'))
#     else:
#         category_form = ProductCategoryEditForm()
#
#     context = {
#         'title': title,
#         'category_form': category_form,
#     }
#
#     return render(request, 'categories/category_create_update.html', context=context)


# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     title = 'админка/редактирование категории'
#
#     edit_category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         category_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('adminapp:categories'))
#     else:
#         category_form = ProductCategoryEditForm(instance=edit_category)
#
#     context = {
#         'title': title,
#         'category_form': category_form,
#     }
#     return render(request, 'categories/category_create_update.html', context=context)


# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     title = 'админка/удаление категории'
#
#     delete_category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         delete_category.is_active = False
#         delete_category.save()
#         return HttpResponseRedirect(reverse('adminapp:categories'))
#
#     context = {
#         'title': title,
#         'category_to_delete': delete_category,
#     }
#
#     return render(request, 'categories/category_delete.html', context)

# -------------------------------products-----------------
# @user_passes_test(lambda u: u.is_superuser)
# def products(request, pk, page=1):
#     title = 'админка/продукты'
#
#     if pk == 0:
#         products_list = Product.objects.all().order_by('name')
#         category = {'name': 'все', 'pk': '0'}
#     else:
#         category = get_object_or_404(ProductCategory, pk=pk)
#         products_list = Product.objects.filter(category__pk=pk).order_by('name')
#
#     paginator = Paginator(products_list, 2)
#
#     try:
#         products_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(1)
#
#     context = {
#         'title': title,
#         'category': category,
#         'objects': products_paginator,
#     }
#
#     return render(request, 'products/products_.html', context)

# @user_passes_test(lambda u: u.is_superuser)
# def product_read(request, pk):
#     title = 'админка/подробнее о продукте'
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'title': title,
#         'product': product,
#     }
#
#     return render(request, 'products/product.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def product_create(request, pk):
#     title = 'админка/создание продукта'
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         product_form = ProductsEditForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('adminapp:products', args=[pk]))
#     else:
#         product_form = ProductsEditForm(initial={'category': category})
#
#     context = {
#         'title': title,
#         'product_form': product_form,
#         'category': category,
#     }
#
#     return render(request, 'products/product_create_update.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request, pk):
#     title = 'админка/редактирование продукта'
#
#     edit_product = get_object_or_404(Product, pk=pk)
#     category = edit_product.category
#     if request.method == 'POST':
#         product_form = ProductsEditForm(request.POST, request.FILES, instance=edit_product)
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('adminapp:products', args=[edit_product.pk]))
#     else:
#         product_form = ProductsEditForm(instance=edit_product)
#
#     context = {
#         'title': title,
#         'product_form': product_form,
#         'category': category,
#     }
#
#     return render(request, 'products/product_create_update.html', context)

# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#     title = 'админка/удаление продукта'
#
#     delete_product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         delete_product.is_active = False
#         delete_product.save()
#         return HttpResponseRedirect(reverse('adminapp:products', args=[delete_product.category.pk]))
#
#     context = {
#         'title': title,
#         'product_to_delete': delete_product,
#     }
#
#     return render(request, 'products/product_delete.html', context)
