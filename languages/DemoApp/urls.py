from django.urls import path
from DemoApp import views
urlpatterns = [
    path('',views.home,name="hm"),
    path('login/',views.login,name='log'),
    path('signup/',views.signu,name='sig'),
    path('otp/',views.otp,name='pt'),
    path('dashboard/',views.dash,name='das'),
    path('text/',views.tet,name='tex'),
    path('profile/',views.prof,name='pro'), 
    path('settings/',views.sets,name='set'),
    path('logout/',views.logot,name='lot'),
    path('voice/',views.vmoice,name='voce'),
    path('voicetrans/',views.mapc,name="tam"),
    path('history/',views.histo,name='his'),
    path('ocrs/',views.ocrs,name='oss'),
    path('vtrans/',views.vtran,name='vts'),
    path('translated/',views.voicet,name='vps'),
    path('accunt/',views.acct,name='act'),
    path('otplogin/',views.otss,name='otp'),
    path('verify_otp/', views.verify_otp, name='vot'),
    path('password/', views.passw, name='pas'),
    
    

]