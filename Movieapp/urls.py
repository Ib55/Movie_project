



from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('movie<slug:key>',views.oneMovie,name='oneMovie'),
    path('actor<slug:key>',views.oneActor,name='oneActor'),
    path('director<slug:key>',views.oneDirector,name='oneDirector')
]
