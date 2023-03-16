from django.urls import path, include
from .import views
app_name='movieapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('movi/<int:movi_id>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]