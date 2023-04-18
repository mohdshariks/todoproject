from django.urls import path
from . import views
urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cvbhome',views.Tasklistview.as_view(),name='cvbhome'),
    path('cvdetails/<int:pk>/',views.TaskDetailview.as_view(),name='cvdetails'),
    path('cvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cvupdate'),
    path('cvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cvdelete'),
]