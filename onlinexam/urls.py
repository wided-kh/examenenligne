from django.urls import path,include
from django.contrib import admin
from exam import views
from django.contrib.auth.views import LogoutView,LoginView
urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('teacher/',include('teacher.urls')),
    path('student/',include('student.urls')),
    


    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='exam/logout.html'),name='logout'),
    path('contactus', views.contactus_view),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),


]
