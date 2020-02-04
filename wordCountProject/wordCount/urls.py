from . import check
from django.urls import path

urlpatterns = [
    path('',check.home,name='home'),
    path('count_file/',check.count_file,name='count_file'),
    path('count_text/',check.count_text,name='count_input')
]
