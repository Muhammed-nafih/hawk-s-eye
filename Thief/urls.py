"""Thief_Detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.log),
     path('log_post', views.log_post),
     path('admin_home', views.admin_home),
     path('police_add', views.police_add),
     path('police_add_post', views.police_add_post),
     path('view_police', views.view_police),
     path('update_police/<id>', views.update_police),
     path('update_police_post/<id>', views.update_police_post),
     path('delete_police/<id>', views.delete_police),
     path('add_criminal_category', views.add_criminal_category),
     path('add_criminal_category_post', views.add_criminal_category_post),
     path('view_category', views.view_category),
     path('delete_category/<id>', views.delete_category),
     path('view_detection_details', views.view_detection_details),
     path('view_criminals', views.view_criminals),
     path('view_user', views.view_user),
     path('view_complaint', views.view_complaint),
     path('view_complaint_post', views.view_complaint_post),
     path('view_complaint_post1', views.view_complaint_post1),
     path('logout', views.logout),

######################################################################################
     path('police_home',views.police_home),
     path('view_profile',views.view_profile),
     path('add_criminal',views.add_criminal),
     path('add_criminal_post',views.add_criminal_post),
     path('view_criminal',views.view_criminal),
     path('update_criminal/<id>',views.update_criminal),
     path('update_criminal_post/<id>',views.update_criminal_post),
     path('delete_criminal/<id>',views.delete_criminal),
     path('add_crimehistory/<id>',views.add_crimehistory),
     path('add_crimehistory_post/<id>',views.add_crimehistory_post),
     path('delete_history/<id>',views.delete_history),
     path('view_users',views.view_users),
     path('view_crminal_alert',views.view_crminal_alert),

##############################################################################

     path('user_registration', views.user_registration),
     path('regpost', views.regpost),
     path('email_already_exist', views.email_already_exist),
     path('user_home',views.user_home),
     path('user_view_profile',views.user_view_profile),
     path('user_view_police',views.user_view_police),
     path('user_view_criminals', views.user_view_criminals),
     path('user_view_crimehistory/<id>', views.user_view_crimehistory),
     path('add_camera', views.add_camera),
     path('add_camera_post', views.add_camera_post),
     path('user_view_camera', views.user_view_camera),
     path('delete_camera/<cid>',views.delete_camera),
     path('user_add_familiar_person',views.user_add_familiar_person),
     path('user_add_familiar_person_post',views.user_add_familiar_person_post),
     path('user_view_familiar_person',views.user_view_familiar_person),
     path('user_delete_familiar_person/<fid>',views.user_delete_familiar_person),
     path('user_update_familiar_persons/<fid>',views.user_update_familiar_persons),
     path('user_update_familiar_person_post/<fid>',views.user_update_familiar_person_post),
     path('user_view_comp',views.user_view_comp),
     path('add_complaint',views.add_complaint),
     path('add_complaint_post',views.add_complaint_post),
     path('user_view_alert/<t>',views.user_view_alert),
     

]
