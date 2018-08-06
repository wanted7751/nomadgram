from . import views
from django.conf.urls import url




app_name = "images"
urlpatterns = [
    url(
        regex=r'^all/$',
        view=views.ListAllImages.as_view(),
        name='all_images'
    )
]
