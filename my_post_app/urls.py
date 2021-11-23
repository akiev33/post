from django.urls import path

from my_post_app.views import (get_post, detail_post, delete_post, create_post, new_create, model_form_post, create_image)

urlpatterns = [
    path('', get_post, name='post'),
    path('detail/<int:pk>/', detail_post, name='detail'),
    path('delete/<int:pk>/', delete_post, name='delete'),
    path('create/', create_post, name='delete'),
    path('new-create/', new_create, name='new_create'),
    path('update-post/<int:pk>/', model_form_post, name='update'),
    path('create-image/', create_image, name='image'),
]
