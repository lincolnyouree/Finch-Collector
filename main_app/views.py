from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Poop, Photo
from .forms import FeedingForm
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'finchescollectors'

def add_photo(request, finch_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, finch_id=finch_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/finches/'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  poops_finch_doesnt_have = Poop.objects.exclude(id__in = finch.poops.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', {
    'finch': finch, 'feeding_form': feeding_form,
    'poops': poops_finch_doesnt_have
  })

def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)

def assoc_poop(request, finch_id, poop_id):
  Poop.objects.get(id=finch_id).poops.add(poop_id)
  return redirect('detail', finch_id=finch_id)

def unassoc_poop(request, finch_id, poop_id):
  Finch.objects.get(id=finch_id).poops.remove(poop_id)
  return redirect('detail', finch_id=finch_id)

class PoopList(ListView):
  model = Poop

class PoopDetail(DetailView):
  model = Poop

class PoopCreate(CreateView):
  model = Poop
  fields = '__all__'

class PoopUpdate(UpdateView):
  model = Poop
  fields = ['name', 'color']

class PoopDelete(DeleteView):
  model = Poop
  success_url = '/poops/'