from django.urls import path
from  .views import Tasklist,TaskDetail,TaskCreate,TaskEdit,TaskDelete,CustomLoginView,RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    path('',Tasklist.as_view(),name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create/',TaskCreate.as_view(),name='create-task'),
    path('task-update/<int:pk>/', TaskEdit.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-del')
] 