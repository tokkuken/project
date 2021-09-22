from django.urls import path,include
from .views import index,post,answer,stop,start,signup,logout,score,scorelist,master

urlpatterns = [
    path('',index, name="index"),
    path('post',post,name="post"),
    path('answer',answer,name="answer"),
    path('stop',stop,name='stop'),
    path('start',start,name='start'),
    path('signup',signup,name='signup'),
    path('logout',logout,name='logout'),
    path('score',score,name='score'),
    path('scorelist',scorelist,name="scorelist"),
    path('master',master,name="master")

]
