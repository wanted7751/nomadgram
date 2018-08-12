from django.urls import path
from . import views
from django.conf.urls import url


app_name = "users"
urlpatterns = [
    url(
        regex=r'^explore/$',
        view=views.ExploreUsers.as_view(),
        name='ExploreUsers'
    ),
]