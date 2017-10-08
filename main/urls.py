from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'accept_data', views.accept_data,  name='accept_data'),
]