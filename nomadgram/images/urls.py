from . import views
from django.conf.urls import url




app_name = "images"
urlpatterns = [
    url(
        regex=r'^all/$',
        view=views.Feed.as_view(),
        name='feed'
    ),
    ]
