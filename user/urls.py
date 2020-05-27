from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('changepassword/', views.change_password, name='change_password'),
    path('comments/', views.yorum_listele, name='yorum_listele'),
    path('deletecomment/<int:id>',views.deletecomment, name='deletecomment'),
    path('usergezi/', views.user_gezi, name='user_gezi'),
    path('usergezi/addgezi/', views.add_gezi, name='add_gezi'),

]

