from django.urls import path

from .views import IndexView, PostView, AuthorView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/', PostView.as_view(), name='post'),
    path('author/', AuthorView.as_view(), name='author'),
]
