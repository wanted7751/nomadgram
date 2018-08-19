from . import views
from django.conf.urls import url

app_name = "notifications"
urlpatterns = [
    url(
        regex=r'^$',
        view=views.Notifications.as_view(),
        name='notifications'
    ),

]


