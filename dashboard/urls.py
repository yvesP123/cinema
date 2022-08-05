from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboards,name='dashboards'),
    path('add/',views.add,name='add'),
    path('Hide/<int:id>',views.Hide,name='Hide')  ,
    path('restore/id=<int:id>',views.restore,name='restore')  ,
    path('delete/id=<int:id>',views.delete,name='delete')  ,
    path('profile',views.profile,name='profile'),
    path('edit/id=<int:id>',views.edit,name='edit')  ,
    path('update/<int:id>',views.update,name='update')  ,
    path('search/',views.search,name='search')  ,
    path('logout/',views.logout,name='logout')  ,
    path('trash/',views.trash,name='trash'), 
    path('favorite/<str:get_username>',views.favorite,name='favorite'),
    

]
