import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

from django.http.response import HttpResponse
from django.shortcuts import (render, redirect,)
from django import forms
from myapp.models import Posting
from .forms import PostingForm

def index(request):
  form = PostingForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      return redirect('myapp:index')
  new_text = Posting.objects.all().order_by('-id')
  contexts = {
    'form':form,
    'new_text':new_text,
  }
  return render(request, 'index.html', contexts)