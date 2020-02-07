from django.contrib import admin
from django.urls import path, include
from products import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.product_home,name="product_home"),
    path('accounts/',include('accounts.urls')),
]
