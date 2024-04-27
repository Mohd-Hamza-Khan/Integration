from django.urls import path
from accounts import views

urlpatterns = [ 
    path('log',views.index, name="log"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('register/',views.register, name='register'),
]