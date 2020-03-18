from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('finches/', views.finches_index, name='index'),
  path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
  path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
  path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
  path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
  path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('finches/<int:finch_id>/add_photo/', views.add_photo, name='add_photo'),
  path('finches/<int:finch_id>/assoc_poop/<int:poop_id>/', views.assoc_poop, name='assoc_poop'),
  path('finches/<int:finch_id>/unassoc_poop/<int:poop_id>/', views.unassoc_poop, name='unassoc_poop'),
  path('poops/', views.PoopList.as_view(), name='poops_index'),
  path('poops/<int:pk>/', views.PoopDetail.as_view(), name='poops_detail'),
  path('poops/create/', views.PoopCreate.as_view(), name='poops_create'),
  path('poops/<int:pk>/update/', views.PoopUpdate.as_view(), name='poops_update'),
  path('poops/<int:pk>/delete/', views.PoopDelete.as_view(), name='poops_delete'),
]