from django.shortcuts import render


def index(request):
    return render(request, 'home-with-profile.html')


def index_no_profile(request):
    return render(request, 'home-no-profile.html')


def create_expense(request):
    return render(request, 'expense-create.html')


def delete_expense(request, pk):
    return render(request, 'expense-delete.html')


def edit_expense(request, pk):
    return render(request, 'expense-edit.html')


def profile_page(request):
    return render(request, 'profile.html')


def delete_profile_page(request):
    return render(request, 'profile-delete.html')


def edit_profile_page(request):
    return render(request, 'profile-edit.html')

