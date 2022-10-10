from django.shortcuts import render, redirect

from expenses_tracker.web.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, EditExpenseForm
from expenses_tracker.web.models import Profile, Expense


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]

    return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(e.price for e in expenses)
    context = {
        'profile': profile,
        'expenses': expenses,
        'budget_left': budget_left,
    }

    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()

    contex = {
        'form': form,
        'no_profile': True,
    }

    return render(request, 'home-no-profile.html', contex)


def create_expense(request):
    return render(request, 'expense-create.html')


def delete_expense(request, pk):
    return render(request, 'expense-delete.html')


def edit_expense(request, pk):
    expenses = Expense.objects.all()
    if request.method == 'POST':
        form = EditExpenseForm(request.POST, request.FILES, instance=expenses)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditExpenseForm(instance=expenses)

    contex = {
        'form': form,
    }

    return render(request, 'expense-edit.html', contex)


def show_profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(e.price for e in expenses)
    expenses_count = len(expenses)

    context = {
        'profile': profile,
        'expenses_count': expenses_count,
        'budget_left': budget_left,
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=profile)

    contex = {
        'form': form,
    }

    return render(request, 'profile-delete.html', contex)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditProfileForm(instance=profile)

    contex = {
        'form': form,
    }
    return render(request, 'profile-edit.html', contex)

