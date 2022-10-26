from django.shortcuts import render, redirect

from new_expenses_tracker.web.forms import NoProfileForm, CreateExpenseForm, EditProfileForm, DeleteProfileForm, \
    EditExpenseForm, DeleteExpenseForm
from new_expenses_tracker.web.models import Profile, Expense


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    expenses = Expense.objects.all()
    expenses_sum = sum(e.price for e in expenses)
    budget_left = profile.budget - expenses_sum

    context = {
        'profile': profile,
        'expenses': expenses,
        'budget_left': budget_left,
    }

    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'GET':
        form = CreateExpenseForm()
    else:
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')

    context = {
        'form': form,
    }
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expenses = Expense.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = EditExpenseForm(request.POST, request.FILES, instance=expenses)
        if form.is_valid():
            form.save()
            return redirect('show index')

    else:
        form = EditExpenseForm(instance=expenses)

    context = {
        'form': form,
        'expenses': expenses,
        'pk': pk,
    }
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expenses = Expense.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, request.FILES, instance=expenses)
        if form.is_valid():
            form.save()
            return redirect('show index')

    else:
        form = DeleteExpenseForm(instance=expenses)

    context = {
        'form': form,
        'expenses': expenses,
        'pk': pk,
    }
    return render(request, 'expense-delete.html', context)


def show_profile(request):
    profile = get_profile()
    expense = Expense.objects.all()
    expenses_sum = sum(e.price for e in expense)
    budget_left = profile.budget - expenses_sum

    context = {
        'profile': profile,
        'expense_count': len(expense),
        'budget_left': budget_left,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')

    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('create profile')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)


def create_profile(request):

    if request.method == 'POST':
        form = NoProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = NoProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)
