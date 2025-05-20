from django.urls import path
from . import views


urlpatterns = [
    path('submit/daily/', views.submit_daily, name='submit_daily'),
    path('submit/weekly/', views.submit_weakly, name='submit_weekly'),
    path('submit/monthly/', views.submit_monthly, name='submit_monthly'),
    path('submit/yearly/', views.submit_yearly, name='submit_yearly'),
    path('submit/long/', views.submit_long, name='submit_long'),

]