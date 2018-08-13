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
    url(
        regex=r'^(?P<user_id>[0-9]+)/follow/$',
        view=views.FollowUser.as_view(), 
        name='follow_user'
    ),
]
