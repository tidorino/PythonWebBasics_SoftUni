from django.shortcuts import render


def show_index(request):
    return render(request, 'bootstrap_html/index.html')
