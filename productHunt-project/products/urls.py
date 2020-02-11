from django.urls import path, include
from products import views

urlpatterns = [
    path('create/',views.create_blog,name="create"),
]
