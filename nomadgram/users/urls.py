from django.urls import path
from . import views
from django.conf.urls import url


app_name = "users"
urlpatterns = [
    url(
        regex=r'^explore/$',
        view=views.ExploreUsers.as_view(),
        name='Explore_Users'
    ),
    url(
        regex=r'^(?P<user_id>[0-9]+)/follow/$',
        view=views.FollowUser.as_view(), 
        name='follow_user'
    ),
    url(
        regex=r'^(?P<user_id>[0-9]+)/unfollow/$',
        view=views.UnFollowUser.as_view(),
        name='unfollow_user'
    ),
    url(
        regex=r'^(?P<username>\w+)/followers/$',
        view=views.UserFollowers.as_view(),
        name='user_followers'
    ),
    url(
        regex=r'^(?P<username>\w+)/following/$',
        view=views.UserFollowing.as_view(),
        name='user_following'
    ),
    url(
        regex=r'^search/$',
        view=views.Search.as_view(),
        name='user_following'
    ),
    #search가 이름이 될 수 있으니 users/search 와 users/username url의 순서를 바꿔줌.
    url(
        regex=r'^(?P<username>\w+)/$',
        view=views.UserProfile.as_view(),
        name='user_profile'
    ),
    url(
        regex=r'^(?P<username>\w+)/password',
        view=views.ChangePassword.as_view(),
        name='change'
    ),
    url(
        regex=r'^login/facebook/$',
        view=views.FacebookLogin.as_view(), 
        name='fb_login'
        ),
]
