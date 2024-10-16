from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.index, name='index'),
    path('homepage/view/', views.view, name='view'),
    path('homepage/view/database/',views.database, name='database'),
    path('homepage/view/database/course/',views.course, name='course'),
    path('homepage/newmentor/',views.mentor,name='mentor'),
    path('homepage/view/database/course/update_course/<str:code>',views.update_course,name='update_course'),
    path('homepage/view/database/course/update_course/save_update_course/<str:code>',views.save_update_course,name='save_update_course'),
    path('homepage/newmentor/update_mentor/<str:menid>',views.update_mentor,name='update_mentor'),
    path('homepage/newmentor/update_mentor/save_update_mentor/<str:menid>',views.save_update_mentor,name='save_update_mentor'),
    path('homepage/view/database/course/delete_course/<str:code>',views.delete_course,name='delete_course'),
    path('homepage/newmentor/delete_mentor/<str:menid>',views.delete_mentor,name='delete_mentor'),
    path('homepage/search_course/',views.search_course,name='search_course'),
    path('homepage/search_course/<str:code',views.search_course,name='search_course'),
    path('homepage/search_mentor/',views.search_mentor,name='search_mentor'),
    path('homepage/search_mentor/<str:code',views.search_mentor,name='search_mentor'),

]