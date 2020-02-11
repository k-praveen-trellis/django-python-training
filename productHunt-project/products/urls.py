from django.urls import path, include
from products import views

urlpatterns = [
    path('create/',views.create_blog,name="create"),
    path('<int:product_id>',views.detail,name="detail"),
    path('<int:product_id>/upvote',views.upvote,name="upvote"),
    path('search',views.search,name="search")
]
