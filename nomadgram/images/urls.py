from . import views
from django.conf.urls import url




app_name = "images"
urlpatterns = [
    url(
        regex=r'^all/$',
        view=views.Feed.as_view(),
        name='feed'
    ),
    url(
        regex=r'(?P<image_id>[0-9]+)/like/',
        view=views.LikeImage.as_view(),
        name='like_image'

    )

    ]


#/images/3/like

#0 create the url and the view
#1 take the id from the url
#2 we want to find an image with this id
#3 we want to create a like for that image
