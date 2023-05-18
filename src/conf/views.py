from django.shortcuts import render
from datetime import datetime


def index(request):
    return render(request, 'mercadona/base.html', context={"date":datetime.today()})