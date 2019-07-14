from django.conf.urls import url
from playgames import views

urlpatterns = [
    url(r'^$', views.PlayPageView.as_view()),
    url(r'^playgames/$', views.userAPI.as_view()),
    url(r'^api/stones/$', views.getStones.as_view()),
]
